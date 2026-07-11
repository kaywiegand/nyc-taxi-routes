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
| Status | 🟢 Analyse + Insights vollständig — alle 9 Business-Fragen aus `docs/infos.md` beantwortet |
| Nächster Schritt | `/project-case check` — Portfolio-Aufbereitung |

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
- Datenexport-Dateiname `ny-taxi-routes_prep.parquet` (in `02_preparation.ipynb`/`03_analysis.ipynb`) nutzt noch die alte Slug-Schreibweise ohne "c" — kosmetisch, kein funktionaler Bug

**Nächster Schritt:** `/project-review` ausführen, danach je nach Ergebnis `/project-case check`.

---

### 2026-07-11 – Review (BEDINGT) + Content-Fertigstellung

**Kontext:** `/project-review` ergab BEDINGT — Fundament solide, aber Kernfrage nur zu 3/9 Aufgaben beantwortet, kein Key Visual im README, ein unaufgelöster Notebook-Fehler.

**Was gemacht wurde:**
- `01_exploration.ipynb` Cell 39 gefixt (`total_amount` existierte nicht in den Rohdaten — durch `fare_amount + tip_amount` + `is_weekend`-Split ersetzt, Logik standalone gegen die echten Daten verifiziert)
- Beim Versuch, das komplette Notebook neu auszuführen: **wgnd-Toolkit API-Drift entdeckt** — `cfg.PALETTE_DIVERGENT` existiert in der aktuell gepinnten `wgnd@main`-Version nicht mehr (Cell 37 schlägt bei Re-Run fehl, obwohl gespeicherte Outputs von einem älteren wgnd-Stand vorhanden sind). Dokumentiert in `BACKLOG.md` #5 — potenziell relevant für alle Projekte mit ungepinnter `wgnd @ git+...@main`-Dependency.
- Business-Fragen 4–7 aus `docs/infos.md` umgesetzt in `03_analysis.ipynb`: Pickup-Standort-Karte, JFK-Anteil pro Wochentag (Montag 2,60 % höchster, Samstag 1,44 % niedrigster), Wochentags-Verteilung Gesamt vs. JFK, Uhrzeit-Verteilung Gesamt vs. JFK — Notebook komplett via `nbconvert --execute` durchgelaufen, alle Outputs echt (keine erfundenen Zahlen)
- `04_insights.ipynb` geschrieben: Executive Summary + 5 evidenzbasierte Empfehlungen (Wochentag-/Uhrzeit-Gewichtung für Flottenplanung). Keine absolute Stückzahl möglich — Datensatz enthält keine Gesamtflottengröße (BACKLOG #7)
- README aktualisiert: Key Visual eingebettet, TL;DR + Results + Recommendations mit den finalen Zahlen befüllt, Status-Badge auf „Analysis complete"
- ROADMAP Phase 4 + 5 auf ✅ gesetzt, BACKLOG #1/#2 nach „Erledigt" verschoben

**Nächster Schritt:** `/project-case check` — Portfolio-Aufbereitung starten.

---
