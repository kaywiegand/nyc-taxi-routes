"""
notebook.py
-----------
Zentraler Einstiegspunkt für alle Notebooks.
Importiere einmalig am Anfang jedes Notebooks:

    from ny_taxi_routes.notebook import *
    setup_plotting()
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

from wgnd.inspect import (
    inspect,
    inspect_missing,
    inspect_duplicates,
    inspect_outliers,
    inspect_outlier_detail,
    inspect_correlations,
)
from wgnd.core._output import success, warn, log, info_box, show_df, section_header
from wgnd.core.config import cfg

from ny_taxi_routes.config import PATHS, PROJECT_NAME, RANDOM_SEED
from ny_taxi_routes.settings import setup_plotting
from ny_taxi_routes.utils import GeoBounds, get_geo_mask, JFK, NYC
from ny_taxi_routes.data.cleaning import clean_data, get_cleaning_mask
from ny_taxi_routes.features.engineering import add_features, add_geo_routes, add_economic_metrics, add_time_features
from ny_taxi_routes.visualization.geo_locations import show_geo_locations_map

__all__ = [
    "pd", "np", "plt", "sns", "Path",
    "inspect", "inspect_missing", "inspect_duplicates",
    "inspect_outliers", "inspect_outlier_detail", "inspect_correlations",
    "success", "warn", "log", "info_box", "show_df", "section_header", "cfg",
    "PATHS", "PROJECT_NAME", "RANDOM_SEED", "setup_plotting",
    "GeoBounds", "get_geo_mask", "JFK", "NYC", 
    "clean_data", "get_cleaning_mask",
    "add_features", "add_geo_routes", "add_economic_metrics", "add_time_features", 
    "show_geo_locations_map",

]
