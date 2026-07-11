"""
test_data.py
------------
Tests für die Cleaning-Pipeline (data/cleaning.py).
Ausführen mit: pytest tests/
"""

import pandas as pd
from nyc_taxi_routes.data.cleaning import get_cleaning_mask, clean_data


def _valid_row(**overrides):
    row = {
        "fare_amount": 10.0,
        "tip_amount": 1.0,
        "passenger_count": 2,
        "trip_distance": 5.0,
        "pickup_longitude": -73.98,
        "pickup_latitude": 40.75,
        "dropoff_longitude": -73.96,
        "dropoff_latitude": 40.77,
    }
    row.update(overrides)
    return row


def test_get_cleaning_mask_flags_finance_errors():
    df = pd.DataFrame([_valid_row(fare_amount=1.0)])
    masks = get_cleaning_mask(df)
    assert masks["errors"]["Finance (Messfehler)"].iloc[0]
    assert masks["combined"].iloc[0]


def test_get_cleaning_mask_flags_geo_errors():
    df = pd.DataFrame([_valid_row(pickup_longitude=0.0, pickup_latitude=0.0)])
    masks = get_cleaning_mask(df)
    assert masks["errors"]["Geography (Messfehler)"].iloc[0]


def test_get_cleaning_mask_flags_business_scope():
    df = pd.DataFrame([_valid_row(fare_amount=300.0)])
    masks = get_cleaning_mask(df)
    assert masks["business"]["Fare/Tip (Business)"].iloc[0]
    assert not masks["errors"]["Finance (Messfehler)"].iloc[0]


def test_get_cleaning_mask_passes_valid_row():
    df = pd.DataFrame([_valid_row()])
    masks = get_cleaning_mask(df)
    assert not masks["combined"].iloc[0]


def test_clean_data_removes_duplicates_and_invalid_rows():
    df = pd.DataFrame([
        _valid_row(),
        _valid_row(),  # exact duplicate
        _valid_row(fare_amount=1.0),  # invalid: below minimum fare
    ])
    cleaned = clean_data(df)
    assert len(cleaned) == 1
