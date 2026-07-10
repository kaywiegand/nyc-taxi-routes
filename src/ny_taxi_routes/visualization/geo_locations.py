import pandas as pd
import matplotlib.pyplot as plt
from ny_taxi_routes.utils import JFK, NYC
from wgnd.core.theme import mpl_style
from wgnd.core.config import cfg



def show_geo_locations_map(df, colors=None):

    style = mpl_style()

    colors = colors or {
        "OTHER": cfg.ACTIVE_PALETTE[1],
        "JFK":   cfg.ACTIVE_PALETTE[5],
        "NYC":   cfg.ACTIVE_PALETTE[9],
    }

    SCATTER_KWARGS_OTHER = dict(alpha=0.9, s=6.0, color=colors['OTHER'], linewidths=0)
    SCATTER_KWARGS_JFK   = dict(alpha=0.9, s=8.0, color=colors['JFK'],   linewidths=0)
    SCATTER_KWARGS_NYC   = dict(alpha=0.2, s=1.0, color=colors['NYC'],   linewidths=0)

    # Absolute Minima und Maxima über alle Bounds hinweg
    # Für Longitude (X-Achse):
    # Der westlichste Punkt ist das MINIMUM (z.B. -74.3)
    # Der östlichste Punkt ist das MAXIMUM (z.B. -73.6)
    all_lon_min = min(JFK.lon_min, NYC.lon_min)
    all_lon_max = max(JFK.lon_max, NYC.lon_max)

    # Für Latitude (Y-Achse):
    # Der südlichste Punkt ist das MINIMUM (z.B. 40.4)
    # Der nördlichste Punkt ist das MAXIMUM (z.B. 41.1)
    all_lat_min = min(JFK.lat_min, NYC.lat_min)
    all_lat_max = max(JFK.lat_max, NYC.lat_max)

    # Limits mit Puffer (z.B. 0.05 Grad), damit nichts am Rand klebt
    x_lims = (all_lon_min - 0.05, all_lon_max + 0.05)
    y_lims = (all_lat_min - 0.05, all_lat_max + 0.05)

    fig, axs = plt.subplots(1,2,figsize=(10,10), constrained_layout=True)
    axs = axs.flatten()            

    departures_nyc = df[ (df["departure"]=="NYC" ) ]
    departures_jfk = df[ (df["departure"]=="JFK" ) ]
    departures_oth = df[ (df["departure"]=="OTHER" ) ]

    arrival_nyc = df[df["arrival"] == "NYC"]
    arrival_jfk = df[df["arrival"] == "JFK"]
    arrival_oth = df[df["arrival"] == "OTHER"]

    # ── Departures ────────────────────────────────────────────────────────────
    axs[0].scatter(departures_oth["pickup_longitude"],  departures_oth["pickup_latitude"],  label="OTHER", **SCATTER_KWARGS_OTHER)
    axs[0].scatter(departures_jfk["pickup_longitude"],  departures_jfk["pickup_latitude"],  label="JFK",   **SCATTER_KWARGS_JFK)
    axs[0].scatter(departures_nyc["pickup_longitude"],  departures_nyc["pickup_latitude"],  label="NYC",   **SCATTER_KWARGS_NYC)
    axs[0].set_title("Departures", **style["title"])

    # ── Arrivals ──────────────────────────────────────────────────────────────
    axs[1].scatter(arrival_oth["dropoff_longitude"],  arrival_oth["dropoff_latitude"],  label="OTHER", **SCATTER_KWARGS_OTHER)
    axs[1].scatter(arrival_jfk["dropoff_longitude"],  arrival_jfk["dropoff_latitude"],  label="JFK",   **SCATTER_KWARGS_JFK)
    axs[1].scatter(arrival_nyc["dropoff_longitude"],  arrival_nyc["dropoff_latitude"],  label="NYC",   **SCATTER_KWARGS_NYC)
    axs[1].set_title("Arrivals", **style["title"])

    # ── Gemeinsames Styling ───────────────────────────────────────────────────
    for ax in axs:
        ax.set_xlim(x_lims)
        ax.set_ylim(y_lims)
        ax.set_aspect("equal", adjustable="box")
        ax.set_xlabel("Longitude", **style["label"])
        ax.set_ylabel("Latitude",  **style["label"])
        ax.legend(markerscale=3, loc="upper right")
        ax.grid(False)
        ax.spines[["left", "bottom"]].set_color(cfg.CHART_AXIS)

    plt.show()