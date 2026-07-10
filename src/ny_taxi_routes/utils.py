"""
utils.py
--------
Allgemeine Hilfsfunktionen:
  - Timer / Decorator
  - Datei-Helfer
  - Logging-Shortcut
  - Geo-Coordinaten / -Bounds
"""

import time
import logging
from pathlib import Path
from functools import wraps
import pandas as pd
from collections import namedtuple


logger = logging.getLogger(__name__)


def timer(func):
    """Decorator: misst und loggt die Laufzeit einer Funktion."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        logger.info(f"{func.__name__} abgeschlossen in {elapsed:.2f}s")
        return result
    return wrapper


def ensure_dir(path: Path) -> Path:
    """Erstellt Verzeichnis, falls nicht vorhanden. Gibt Pfad zurück."""
    path = Path(path)
    path.mkdir(parents=True, exist_ok=True)
    return path


def list_files(directory: Path, pattern: str = "*") -> list[Path]:
    """Gibt alle Dateien in einem Verzeichnis zurück, die dem Muster entsprechen."""
    return sorted(Path(directory).glob(pattern))



GeoBounds = namedtuple('CityBounds', ['name', 'lat_min', 'lat_max', 'lon_min', 'lon_max'])
JFK = GeoBounds("JFK", 40.62666, 40.66018, -73.80822, -73.76599)
NYC = GeoBounds("NYC", 40.5774, 40.9176, -74.15, -73.7004)
def is_coord_in_bounds(lat, lon, bounds):
    """
    Prüft, ob eine Koordinate innerhalb definierter Grenzen liegt.
    
    Args:
        lat (float): Der Breitengrad des Punktes.
        lon (float): Der Längengrad des Punktes.
        bounds (tuple): Ein NamedTuple mit 'lat_min', 'lat_max', 'lon_min', 'lon_max'.
        
    Returns:
        bool: True, wenn der Punkt innerhalb der Box liegt, sonst False.
    """
    lat_ok = bounds.lat_min <= lat <= bounds.lat_max
    lon_ok = bounds.lon_min <= lon <= bounds.lon_max
    
    return lat_ok and lon_ok

def get_geo_mask(df, bounds, prefix="pickup"):
    """
    Erstellt eine boolesche Maske für einen Datensatz basierend auf GeoBounds.
    """
    return (
        df[f"{prefix}_latitude"].between(bounds.lat_min, bounds.lat_max) &
        df[f"{prefix}_longitude"].between(bounds.lon_min, bounds.lon_max)
    )



