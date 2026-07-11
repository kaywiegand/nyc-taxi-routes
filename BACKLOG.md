# BACKLOG.md – NYC Taxi Routes

Projektspezifische offene Tasks und Todos.
Nie mitten in einer Session den Kontext wechseln — hier notieren, gesammelt abarbeiten.

Prio: `1` = hoch · `2` = mittel · `3` = niedrig

---

| # | Beschreibung | Prio | Entdeckt in |
| :--- | :--- | :--- | :--- |
| 3 | `ny-taxi-routes_prep.parquet` (Export-Dateiname in `02_preparation.ipynb`/`03_analysis.ipynb`) nutzt noch alte Slug-Schreibweise ohne "c" — auf `nyc-taxi-routes_prep.parquet` umbenennen für Konsistenz mit Package/Ordner. Kosmetisch, kein Bug. | 3 | Fundament-Nachzug 2026-07-11 |
| 4 | `public/index.html` mit echten Findings aus `03_analysis.ipynb`/`04_insights.ipynb` befüllen (aktuell generisches Scaffold-Template). | 2 | Fundament-Nachzug 2026-07-11 |
| 5 | **wgnd-Toolkit API-Drift**: `01_exploration.ipynb` Cell 37 nutzt `cfg.PALETTE_DIVERGENT` — Attribut existiert in der aktuell gepinnten `wgnd@main`-Version nicht mehr (`AttributeError` bei Re-Run). Notebook hat gespeicherte Outputs von einem älteren wgnd-Stand, schlägt aber bei frischer Ausführung fehl. Betrifft evtl. weitere Projekte mit `wgnd @ git+...@main` (ungepinnt). Fix: entweder wgnd auf festen Tag/Commit pinnen, oder Cell auf aktuelle wgnd-API migrieren. | 2 | Content-Fertigstellung 2026-07-11 |
| 6 | Kernelspec-Metadata aller Notebooks nennt noch `DAN_NewYork-Taxi-Routes` als Kernel-Namen (Altlast vom ursprünglichen `.venv`-Setup vor der Umbenennung). Kosmetisch — beim nächsten Kernel-Reregistrieren (`python -m ipykernel install ... --name nyc_taxi_routes`) korrigieren. | 3 | Content-Fertigstellung 2026-07-11 |
| 7 | Absolute Flottengröße des Taxiunternehmers ist im Datensatz nicht enthalten — `04_insights.ipynb`-Empfehlungen sind relative Gewichtungsfaktoren, keine Stückzahlen. Für eine harte Empfehlung müsste die Gesamtflottengröße erhoben werden. | 3 | Content-Fertigstellung 2026-07-11 |

---

## Erledigt ✅

| # | Beschreibung | Erledigt |
| :--- | :--- | :--- |
| 1 | Offene Business-Fragen 4–7 (Pickup-Standorte, JFK-Anteil Wochentag, Wochentags-/Uhrzeit-Verteilung) | ✅ 2026-07-11 — `03_analysis.ipynb`, echte Outputs via `nbconvert --execute` |
| 2 | `04_insights.ipynb` — Executive Summary + Flottenempfehlung | ✅ 2026-07-11 |
