# BACKLOG.md – NYC Taxi Routes

Projektspezifische offene Tasks und Todos.
Nie mitten in einer Session den Kontext wechseln — hier notieren, gesammelt abarbeiten.

Prio: `1` = hoch · `2` = mittel · `3` = niedrig

---

| # | Beschreibung | Prio | Entdeckt in |
| :--- | :--- | :--- | :--- |
| 1 | **Offene Business-Fragen 4–7** aus `docs/infos.md`: Visualisierung Pickup-Standorte NYC · JFK-Anteil pro Wochentag (+ höchster/niedrigster Tag) · Wochentags-Verteilung Gesamt vs. JFK · Uhrzeit-Verteilung Gesamt vs. JFK. Notebook: `03_analysis.ipynb` (Next-Steps-Zelle). | 1 | Fundament-Nachzug 2026-07-11 |
| 2 | **`04_insights.ipynb` schreiben** — Executive Summary + Empfehlung, wie viele Taxis am JFK bereitgestellt werden sollten (Business-Frage 9). Aktuell nur Stub-Template. | 1 | Fundament-Nachzug 2026-07-11 |
| 3 | `ny-taxi-routes_prep.parquet` (Export-Dateiname in `02_preparation.ipynb`/`03_analysis.ipynb`) nutzt noch alte Slug-Schreibweise ohne "c" — auf `nyc-taxi-routes_prep.parquet` umbenennen für Konsistenz mit Package/Ordner. Kosmetisch, kein Bug. | 3 | Fundament-Nachzug 2026-07-11 |
| 4 | `public/index.html` mit echten Findings aus `03_analysis.ipynb`/`04_insights.ipynb` befüllen (aktuell generisches Scaffold-Template). | 2 | Fundament-Nachzug 2026-07-11 |
