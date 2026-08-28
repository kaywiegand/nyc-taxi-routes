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

**Pflicht-Lesen, kein Skip — auch wenn die Session direkt in diesem Ordner startet:**

1. `/Users/kaywiegand/Workspace/CLAUDE.md` — globale Arbeitsanweisungen
2. `/Users/kaywiegand/Workspace/docs/personal/STYLE.md` — Kommunikationsregeln (u. a. keine Emojis)
3. `/Users/kaywiegand/Workspace/docs/CONVENTIONS.md` — Notebook-Konventionen, Wording, **Zahlenformat nach Sprache**
4. `PROCESS_LOG.md` — aktueller Projektstand
5. `ROADMAP.md` — offene Phasen und Tasks

**Zusätzlich vor Portfolio-Arbeit** (`/project-case slides` oder `report`):

6. `/Users/kaywiegand/Workspace/wgnd-skills/project-case/build-pipeline.md`, Abschnitte **1c** (Content-Item-Schema) und **1d** (Title- und Closing-Slides)

Grund für die explizite Auflistung (2026-08-28): Die Pflicht-Lesen-Liste in der globalen
`CLAUDE.md` greift nur, wenn die Session im Workspace-Root startet. Startet sie im Projekt,
wird sie übersprungen — genau so entstand die Schema-Drift im Telefonica-Case.

## Projektspezifische Hinweise

- Herkunft: StackFuel Übungsprojekt (Modul 2 / Kapitel 7) — Original-Aufgabenstellung in [`docs/infos.md`](docs/infos.md)
- Geo-Klassifikation (JFK/NYC/Other) über `nyc_taxi_routes.utils.JFK`/`.NYC` (Bounding Boxes) — zentral, nicht in Notebooks dupliziert
- `nyc_taxi_routes.notebook` bündelt alle projektspezifischen Imports (Cleaning, Feature Engineering, Geo-Viz) für den `from nyc_taxi_routes.notebook import *`-Einstieg in Notebooks
- Package hieß bis 2026-07-11 `ny_taxi_routes` (ohne "c") — bei älteren externen Referenzen beachten
