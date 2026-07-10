"""
data/cleaning.py
----------------
Datenbereinigung: Masken und Cleaning-Pipeline.
"""

import pandas as pd
from wgnd.core._output import success, log, section_header


def get_cleaning_mask(df: pd.DataFrame) -> dict:
    """
    Definiert Reinigungsmasken basierend auf Business-Regeln.
    Gibt konsolidierte + Detail-Masken zurück (True = ungültig).
    """
    # 1. Finanzen: Mindesttarif NYC ($2.50), Cap für Ausreißer ($250)
    mask_fare = (df["fare_amount"] < 2.50) | (df["fare_amount"] > 250) | \
                (df["tip_amount"] < 0) | (df["tip_amount"] > 100)

    # 2. Physik: Fahrgastlimit (SUV = 6), Geisterfahrten (0 Pax), keine Distanz
    mask_phys = (df["passenger_count"] < 1) | (df["passenger_count"] > 6) | \
                (df["trip_distance"] <= 0)

    # 3. Business Scope: Fokus auf NYC Metro Area (max 70 Meilen)
    mask_dist = (df["trip_distance"] > 70)

    # 4. Geografie: Koordinaten außerhalb NYC oder Null Island
    mask_geo = ~(
        df["pickup_longitude"].between(-74.3, -73.6) &
        df["pickup_latitude"].between(40.4, 41.0) &
        df["dropoff_longitude"].between(-74.3, -73.6) &
        df["dropoff_latitude"].between(40.4, 41.0)
    )

    # 5. Logik: Technischer Defekt (viel Distanz für fast kein Geld)
    mask_logic = (df["trip_distance"] > 50) & (df["fare_amount"] < 10)

    combined_mask = mask_fare | mask_phys | mask_dist | mask_geo | mask_logic

    return {
        "combined": combined_mask,
        "details": {
            "Finance":   mask_fare,
            "Physics":   mask_phys,
            "Distance":  mask_dist,
            "Geography": mask_geo,
            "Logic":     mask_logic,
        },
    }


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """Führt die komplette Bereinigung inklusive Duplikate durch."""
    initial_count = len(df)
    df = df.drop_duplicates()
    dup_removed = initial_count - len(df)

    masks = get_cleaning_mask(df)
    combined_mask = masks["combined"]

    section_header('Data cleaning:')


    log(f"---  Duplicates: {dup_removed} exact rows removed")
    for name, mask in masks["details"].items():
        log(f"---  {name}: {mask.sum()} invalid/outlier rows identified")

    df_refined = df[~combined_mask].copy()
    log(f" ")
    success(f"Cleaning complete. Total rows removed: {initial_count - len(df_refined)}. Remaining rows for analysis: {len(df_refined)}.")

    return df_refined
