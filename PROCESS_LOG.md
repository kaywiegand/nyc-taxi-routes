# PROCESS_LOG.md – NYC Taxi Routes

> Projektverlauf und AI-Kontext-Einstieg.
> Dieses File ist der Einstiegspunkt für neue Claude-Sessions.

---

## Projekt-Übersicht

| Feld | Inhalt |
| :--- | :--- |
| Projektname | NYC Taxi Routes |
| Typ | DA — Data Analysis |
| Herkunft | StackFuel Übungsprojekt (Modul 2 / Kapitel 7) — Original-Aufgabenstellung: [`docs/infos.md`](docs/infos.md) |
| Erstellt | 2026-04-21 (ursprünglicher Scaffold) · Fundament-Nachzug 2026-07-11 |
| Status | 🟢 EDA + Preparation abgeschlossen, Analyse teilweise beantwortet, Insights offen |
| Nächster Schritt | Offene Business-Fragen 4–7 (Visualisierungen Pickup-Standorte, Wochentag/Uhrzeit-Anteile) + Empfehlung in `04_insights.ipynb` |

---

## Verlauf

### 2026-04-21 – Projektstartup

- Projektstruktur mit dem DAN/DSC Scaffolding Generator aufgesetzt (Basis: Cookiecutter Data Science Template).
- EDA in `01_exploration.ipynb`, Preparation-Pipeline (Cleaning + Feature Engineering) in `02_preparation.ipynb` durchgeführt.
- Kernfrage (Anteil JFK-Abfahrten an Gesamtfahrten) in `03_analysis.ipynb` beantwortet.

### 2026-07-11 – Fundament-Nachzug (Portfolio-Vorbereitung)

**Kontext:** Projekt stand in `docs/PROJECTS.md` seit längerem als „cleanup nötig" — kein Git-Repo, kein aktuelles MD-Fundament (CLAUDE.md/ROADMAP/BACKLOG fehlten), Naming-Inkonsistenz (Ordner `nyc-taxi-routes` vs. Package `ny_taxi_routes`), mehrere Backup-Duplikate der Notebooks aus früheren Arbeitsständen.

**Was gemacht wurde:**
- Vollständiges Backup des Vorzustands (`nyc-taxi-routes_pre-init-backup_2026-07-11.tar.gz`, Workspace-Root)
- `wgnd-scaffolding`-Generator (Typ DA) auf den bestehenden Ordner laufen lassen → git-Repo + Erstcommit (dieses Projekt hatte zuvor **nie** ein Git-Repo)
- Package umbenannt: `ny_taxi_routes` → `nyc_taxi_routes` (konsistent mit Ordnernamen und Repo-Naming-Convention). Custom-Module (`data/cleaning.py`, `features/engineering.py`, `visualization/geo_locations.py`, Geo-Bounds `JFK`/`NYC` in `utils.py`) migriert und per Import-Test verifiziert.
- Notebook-Duplikate bereinigt: `01_exploration.ipynb` ← vollständigste Version (war als `__2` gesichert, 22 ausgeführte Zellen), `02_preparation.ipynb` ← vollständigste Version (war als `__1` gesichert, 6 ausgeführte Zellen). Ältere/unvollständige Duplikate gelöscht (Backup-Archiv hält die Originale zusätzlich vor).
- `03_analysis.ipynb`: echte, ausgeführte Analyse (JFK-Anteil an Gesamtfahrten) erhalten, generische Retail-Platzhalter-Zellen (Competition Analysis / Pricing & Rating / Cluster Analysis — Reste eines nicht angepassten Vorlagen-Templates, nie für dieses Projekt bearbeitet) entfernt. Offene Business-Fragen als Next-Steps-Zelle dokumentiert.
- `00_introduction.ipynb`: Platzhalter (TODO/Lorem-ipsum) durch echte Projektfakten aus `docs/infos.md` ersetzt (Szenario, Data Dictionary, Geo-Bounds).
- `pyproject.toml`: frisch generierte Version enthielt bereits `wgnd-toolkit`-Dependency + identische `da`/`ds`-Extras (nur `dan`/`dsc` umbenannt) — kein manueller Merge nötig.
- Altlasten entfernt: `notebooks/files.zip` + `notebooks/files/` (identisch zu bereits migrierten `src/`-Dateien), `project_decision_log.md` (Template, einzige echte Entscheidung hier übernommen).
- `route_distribution_log.png` von `notebooks/` nach `public/img/` verschoben (Konvention: Chart-Outputs gehören nach `public/`, nicht ins Notebook-Root), referenzierende `savefig()`-Aufrufe in `01_exploration.ipynb`/`02_preparation.ipynb` angepasst.
- `reports/` (alte Konvention) nach `public/` migriert (aktuelle Konvention: `public/img/`, `public/md/`, `public/index.html`).

**Bekannte offene Punkte (Details: `BACKLOG.md`):**
- Business-Fragen 4–7 aus `docs/infos.md` (Pickup-Standort-Visualisierung, Wochentag-/Uhrzeit-Anteile JFK vs. Gesamt) noch nicht bearbeitet
- `04_insights.ipynb` ist inhaltlich noch ein Stub — Executive Summary + Empfehlung ausstehend
- Datenexport-Dateiname `ny-taxi-routes_prep.parquet` (in `02_preparation.ipynb`/`03_analysis.ipynb`) nutzt noch die alte Slug-Schreibweise ohne "c" — kosmetisch, kein funktionaler Bug

**Nächster Schritt:** `/project-review` ausführen, danach je nach Ergebnis `/project-case check`.

---
