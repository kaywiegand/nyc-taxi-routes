"""
features/engineering.py
-----------------------
Feature Engineering: Neue Spalten und Transformationen.
"""

import pandas as pd
import numpy as np
from ny_taxi_routes.utils import JFK, NYC
from wgnd.core._output import success, log, section_header


def add_geo_routes(df):
    """Klassifiziert Start, Ziel und die resultierende Route."""
    mask_pickup_jfk = df["pickup_longitude"].between(JFK.lon_min, JFK.lon_max) & \
                      df["pickup_latitude"].between(JFK.lat_min, JFK.lat_max)
    mask_pickup_nyc = df["pickup_longitude"].between(NYC.lon_min, NYC.lon_max) & \
                      df["pickup_latitude"].between(NYC.lat_min, NYC.lat_max)
    
    mask_dropoff_jfk = df["dropoff_longitude"].between(JFK.lon_min, JFK.lon_max) & \
                       df["dropoff_latitude"].between(JFK.lat_min, JFK.lat_max)
    mask_dropoff_nyc = df["dropoff_longitude"].between(NYC.lon_min, NYC.lon_max) & \
                       df["dropoff_latitude"].between(NYC.lat_min, NYC.lat_max)

    df["departure"] = np.select([mask_pickup_jfk, mask_pickup_nyc], ["JFK", "NYC"], default="OTHER")
    df["arrival"]   = np.select([mask_dropoff_jfk, mask_dropoff_nyc], ["JFK", "NYC"], default="OTHER")
    df["route"]     = df["departure"].astype(str) + "-" + df["arrival"].astype(str)
    
    # Als Kategorien speichern für bessere Performance
    df[["departure", "arrival", "route"]] = df[["departure", "arrival", "route"]].astype("category")
    return df

def add_economic_metrics(df):
    """Berechnet finanzielle Kennzahlen wie Yield und Effizienz."""
    df["total_yield"] = df["fare_amount"] + df["tip_amount"]
    # Vermeidung von Division durch Null (obwohl wir Distanz <= 0 schon gefiltert haben)
    df["price_per_mile"] = (df["total_yield"] / df["trip_distance"]).replace([np.inf, -np.inf], 0)
    df["has_tolls"] = (df["tolls_amount"] > 0).astype(int)
    return df

def add_time_features(df):
    """Erstellt zeitliche Segmente und Wochenend-Flags."""
    bins   = [0, 6, 11, 16, 20, 24]
    labels = ['Night', 'Morning Rush', 'Midday', 'Evening Rush', 'Late Night']

    # pickup_hour kann als category gecastet sein → int für pd.cut benötigt
    hour = df['pickup_hour'].astype(int)
    df['time_slot'] = pd.cut(hour, bins=bins, labels=labels, include_lowest=True, ordered=False)

    df['is_weekend'] = df['pickup_weekday'].astype(int).isin([5, 6]).astype(int)
    return df


def add_scaling(df):
    """
    Log-Transform für stark rechtsschiefe numerische Features.
    Erstellt neue *_log Spalten, behält Originale für Interpretierbarkeit.
    Relevant für distanz- oder regressionsbasierte Analysen.
    """
    skewed_cols = ['trip_distance', 'fare_amount', 'total_yield', 'price_per_mile']
    for col in skewed_cols:
        if col in df.columns:
            # log1p (= log(1+x)) vermeidet log(0) bei Nullwerten
            df[f'{col}_log'] = np.log1p(df[col])
    return df



def add_features(df):
    """
    Zentraler Orchestrator für das Feature Engineering.
    Ruft alle Sub-Funktionen nacheinander auf.
    """
    section_header('Feature Engineering: ')
    
    # Kopie erstellen, um Seiteneffekte zu vermeiden
    df_feat = df.copy()
    
    # Pipeline-Schritte
    log("---  Adding Geo-Location & Routes...")
    df_feat = add_geo_routes(df_feat)
    
    log("---  Adding Economic Metrics (Yield, Price per Mile)...")
    df_feat = add_economic_metrics(df_feat)
    
    log("---  Adding Temporal Features (Time Slots, Weekend-Flag)...")
    df_feat = add_time_features(df_feat)

    log("---  Adding Log-Transforms for skewed features (trip_distance, fare_amount, total_yield, price_per_mile)...")
    df_feat = add_scaling(df_feat)

    log(f" ")
    success("Feature Engineering complete. New columns added.")
    
    return df_feat