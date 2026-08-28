# BACKLOG.md – NYC Taxi Routes

Projektspezifische offene Tasks und Todos.
Nie mitten in einer Session den Kontext wechseln — hier notieren, gesammelt abarbeiten.

Prio: `1` = hoch · `2` = mittel · `3` = niedrig

---

| # | Beschreibung | Prio | Entdeckt in |
| :--- | :--- | :--- | :--- |
| 10 | **Pages-URL geht erst nach Merge nach `main` auf 200** — `.github/workflows/pages.yml` triggert nur auf `push` zu `main`. Der Portfolio-Commit liegt auf `claude/nyc-taxi-portfolio-setup-84c0b9`. Nach Merge läuft der Deploy-Workflow, dann `https://kaywiegand.github.io/nyc-taxi-routes/` prüfen. | 1 | Portfolio-Aufbereitung 2026-08-28 |
| 11 | **Notebook-Header entsprechen nicht dem Standard** — alle 5 Notebooks: `# Title` ok, aber `**UPPERCASE SUBTITLE**` + `---` + `## Inhalt`-ToC fehlen (`project-case check` Schritt 5b). Kosmetisch, blockiert Portfolio nicht. | 3 | Portfolio-Aufbereitung 2026-08-28 |
| 3 | `ny-taxi-routes_prep.parquet` (Export-Dateiname in `02_preparation.ipynb`/`03_analysis.ipynb`) nutzt noch alte Slug-Schreibweise ohne "c" — auf `nyc-taxi-routes_prep.parquet` umbenennen für Konsistenz mit Package/Ordner. Kosmetisch, kein Bug. | 3 | Fundament-Nachzug 2026-07-11 |
| 5 | **wgnd-Toolkit API-Drift**: `01_exploration.ipynb` Cell 37 nutzt `cfg.PALETTE_DIVERGENT` — Attribut existiert in der aktuell gepinnten `wgnd@main`-Version nicht mehr (`AttributeError` bei Re-Run). Notebook hat gespeicherte Outputs von einem älteren wgnd-Stand, schlägt aber bei frischer Ausführung fehl. Betrifft evtl. weitere Projekte mit `wgnd @ git+...@main` (ungepinnt). Fix: entweder wgnd auf festen Tag/Commit pinnen, oder Cell auf aktuelle wgnd-API migrieren. | 2 | Content-Fertigstellung 2026-07-11 |
| 6 | Kernelspec-Metadata aller Notebooks nennt noch `DAN_NewYork-Taxi-Routes` als Kernel-Namen (Altlast vom ursprünglichen `.venv`-Setup vor der Umbenennung). Kosmetisch — beim nächsten Kernel-Reregistrieren (`python -m ipykernel install ... --name nyc_taxi_routes`) korrigieren. | 3 | Content-Fertigstellung 2026-07-11 |
| 7 | Absolute Flottengröße des Taxiunternehmers ist im Datensatz nicht enthalten — `04_insights.ipynb`-Empfehlungen sind relative Gewichtungsfaktoren, keine Stückzahlen. Für eine harte Empfehlung müsste die Gesamtflottengröße erhoben werden. | 3 | Content-Fertigstellung 2026-07-11 |

---

## Erledigt ✅

| # | Beschreibung | Erledigt |
| :--- | :--- | :--- |
| 1 | Offene Business-Fragen 4–7 (Pickup-Standorte, JFK-Anteil Wochentag, Wochentags-/Uhrzeit-Verteilung) | ✅ 2026-07-11 — `03_analysis.ipynb`, echte Outputs via `nbconvert --execute` |
| 2 | `04_insights.ipynb` — Executive Summary + Flottenempfehlung | ✅ 2026-07-11 |
| 8 | `/project-case slides` + `report` | ✅ 2026-08-28 — `public/md/slides.yaml` (10 Kapitel), Views + Hub regeneriert, alter Stub in `public/archive/v1/` |
| 4 | `public/index.html` mit echten Findings befüllen | ✅ 2026-08-28 — Hub wird aus `slides.yaml` `hub`-Block generiert (`generate_index_from_portfolio.py`) |
| 9 | Kein Git-Remote konfiguriert | ✅ 2026-07-11 — `origin` auf `git@github.com:kaywiegand/nyc-taxi-routes.git` gesetzt, alle 5 Commits gepusht |
