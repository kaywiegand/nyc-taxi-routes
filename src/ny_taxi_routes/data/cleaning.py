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
    Gibt konsolidierte + Detail-Masken zurück (True = ungültig),
    getrennt nach Messfehler (technisch) und Business-Scope (inhaltlich).
    """
    # ── 🔴 MESSFEHLER: Technisch unmögliche oder fehlerhafte Datenpunkte ────────
    # Fare unter NYC-Mindesttarif oder negativer Tip → Logging-/Eingabefehler
    mask_err_finance = (df["fare_amount"] < 2.50) | (df["tip_amount"] < 0)

    # Passagiere <= 0 oder Distanz <= 0 → physikalisch unmöglich
    mask_err_phys = (df["passenger_count"] < 1) | (df["trip_distance"] <= 0)

    # GPS außerhalb NYC → Null-Island oder Sensor-Ausfall
    mask_err_geo = ~(
        df["pickup_longitude"].between(-74.3, -73.6) &
        df["pickup_latitude"].between(40.4, 41.0) &
        df["dropoff_longitude"].between(-74.3, -73.6) &
        df["dropoff_latitude"].between(40.4, 41.0)
    )

    # Hohe Distanz bei Minimalfarif → Sensor-Defekt
    mask_err_logic = (df["trip_distance"] > 50) & (df["fare_amount"] < 10)

    # ── 🟡 BUSINESS-SCOPE: Plausibel, aber außerhalb des Analyse-Scopes ─────────
    # Extrempreise / Trinkgeld → Black Swans, nicht planbar für Flottensteuerung
    mask_biz_fare = (df["fare_amount"] > 250) | (df["tip_amount"] > 100)

    # Passagiere > 6 → über NYC SUV-Regulierung (Mini-Bus)
    mask_biz_pax = df["passenger_count"] > 6

    # Distanz > 70 Meilen → außerhalb NYC/JFK-Kerngeschäft
    mask_biz_dist = df["trip_distance"] > 70

    mask_errors   = mask_err_finance | mask_err_phys | mask_err_geo | mask_err_logic
    mask_business = mask_biz_fare | mask_biz_pax | mask_biz_dist
    combined_mask = mask_errors | mask_business

    return {
        "combined": combined_mask,
        "errors": {
            "Finance (Messfehler)":   mask_err_finance,
            "Physics (Messfehler)":   mask_err_phys,
            "Geography (Messfehler)": mask_err_geo,
            "Logic (Messfehler)":     mask_err_logic,
        },
        "business": {
            "Fare/Tip (Business)":    mask_biz_fare,
            "Passengers (Business)":  mask_biz_pax,
            "Distance (Business)":    mask_biz_dist,
        },
    }


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """Führt die komplette Bereinigung inklusive Duplikate durch."""
    initial_count = len(df)
    df = df.drop_duplicates()
    dup_removed = initial_count - len(df)

    masks = get_cleaning_mask(df)
    combined_mask = masks["combined"]

    section_header('Data Cleaning')

    log(f"---  Duplicates: {dup_removed} exact rows removed")
    log(" ")
    log("🔴 Messfehler (technisch ungültig):")
    for name, mask in masks["errors"].items():
        log(f"     {name}: {mask.sum()} rows")
    log(" ")
    log("🟡 Business-Scope (außerhalb Analyse-Fokus):")
    for name, mask in masks["business"].items():
        log(f"     {name}: {mask.sum()} rows")

    df_refined = df[~combined_mask].copy()
    log(" ")
    success(f"Cleaning complete. Removed: {initial_count - len(df_refined)} rows. Remaining: {len(df_refined)}.")

    return df_refined
