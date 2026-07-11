"""
test_features.py
-----------------
Tests für das Feature Engineering (features/engineering.py).
"""

import pandas as pd
from nyc_taxi_routes.features.engineering import (
    add_geo_routes,
    add_economic_metrics,
    add_time_features,
    add_scaling,
)
from nyc_taxi_routes.utils import JFK


def _sample_df():
    jfk_lat = (JFK.lat_min + JFK.lat_max) / 2
    jfk_lon = (JFK.lon_min + JFK.lon_max) / 2
    return pd.DataFrame({
        "pickup_longitude": [jfk_lon, -73.98],
        "pickup_latitude": [jfk_lat, 40.75],
        "dropoff_longitude": [-73.96, -73.96],
        "dropoff_latitude": [40.77, 40.77],
        "fare_amount": [20.0, 10.0],
        "tip_amount": [2.0, 1.0],
        "tolls_amount": [5.0, 0.0],
        "trip_distance": [10.0, 5.0],
        "pickup_hour": [8, 22],
        "pickup_weekday": [5, 1],
    })


def test_add_geo_routes_classifies_jfk_pickup():
    result = add_geo_routes(_sample_df())
    assert result["departure"].iloc[0] == "JFK"
    assert result["departure"].iloc[1] == "NYC"
    assert result["route"].iloc[0] == "JFK-NYC"


def test_add_economic_metrics_computes_yield_and_tolls_flag():
    result = add_economic_metrics(_sample_df())
    assert result["total_yield"].iloc[0] == 22.0
    assert result["price_per_mile"].iloc[0] == 2.2
    assert result["has_tolls"].tolist() == [1, 0]


def test_add_time_features_flags_weekend():
    result = add_time_features(_sample_df())
    assert result["is_weekend"].tolist() == [1, 0]
    assert result["time_slot"].iloc[0] == "Morning Rush"
    assert result["time_slot"].iloc[1] == "Late Night"


def test_add_scaling_creates_log_columns():
    df = add_economic_metrics(_sample_df())
    result = add_scaling(df)
    assert "trip_distance_log" in result.columns
    assert "fare_amount_log" in result.columns
