# CLAUDE.md – NYC Taxi Routes

> Projektspezifische Anweisungen für Claude Code.
> Ergänzt die globale CLAUDE.md aus dem wgnd-workspace.

---

## Projekt

| Feld | Inhalt |
| :--- | :--- |
| Slug | `nyc-taxi-routes` |
| Paket | `nyc_taxi_routes` (Import mit Underscores) |
| Typ | DA — Data Analysis |
| Stack | Pandas · Scikit-learn · Matplotlib/Seaborn · Plotly · Folium · Jupyter · wgnd-toolkit |

## Kontext-Einstieg

1. `PROCESS_LOG.md` lesen — aktueller Projektstand
2. `ROADMAP.md` lesen — offene Phasen und Tasks
3. Globale `CLAUDE.md` aus `/Users/kaywiegand/Workspace/` gilt weiterhin

## Projektspezifische Hinweise

- Herkunft: StackFuel Übungsprojekt (Modul 2 / Kapitel 7) — Original-Aufgabenstellung in [`docs/infos.md`](docs/infos.md)
- Geo-Klassifikation (JFK/NYC/Other) über `nyc_taxi_routes.utils.JFK`/`.NYC` (Bounding Boxes) — zentral, nicht in Notebooks dupliziert
- `nyc_taxi_routes.notebook` bündelt alle projektspezifischen Imports (Cleaning, Feature Engineering, Geo-Viz) für den `from nyc_taxi_routes.notebook import *`-Einstieg in Notebooks
- Package hieß bis 2026-07-11 `ny_taxi_routes` (ohne "c") — bei älteren externen Referenzen beachten
