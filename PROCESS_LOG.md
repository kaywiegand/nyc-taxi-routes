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
| Status | 🟢 Portfolio-Case live — slides.yaml + 3 Views + Hub auf `main`, GitHub Pages unter `https://kaywiegand.github.io/nyc-taxi-routes/` (HTTP 200) |
| Nächster Schritt | Portfolio-Status in `docs/PROJECTS.md` auf `✅ portfolio-ready` setzen; optional `/project-case audit-communication` |

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

### 2026-07-11 – Re-Review (JA) + /project-case check + story

**Kontext:** Nach Content-Fertigstellung erneut `/project-review` angefragt, um den Effekt der Fixes zu prüfen.

**Was gemacht wurde:**
- **`/project-review` erneut ausgeführt → JA** (vorher BEDINGT): alle 5 Notebooks fehlerfrei (0 Error-Outputs), Key Visual im README, MD-Kohärenz weiterhin durchgängig, Git sauber. Einzige Restpunkte: `public/index.html` noch Platzhalter (erwartbar vor `/project-case`) und die bereits dokumentierten kosmetischen BACKLOG-Punkte.
- **`/project-case check`** (Skill: `wgnd-skills/project-case`) durchgeführt: 8-Dimensionen-Scorecard — Story & Relevanz ✅, Struktur & Files ⚠️ (kein `public/*.html` > 50 KB), Kohärenz ✅, Analyse-Qualität ✅, ML-Qualität n.a., Code & Architektur ✅, Artefakte ⚠️ (kein Hub-Inhalt, `portfolio.md` fehlte noch), Reproduzierbarkeit ✅. Ergebnis: **Bereit für Story-Phase: JA** — Lücken sind exakt das, was `story`/`slides`/`report` produzieren, kein inhaltlicher Mangel.
- **`/project-case story`** ausgeführt: `public/md/portfolio.md` geschrieben — Kernthese, 6 Key Findings (JFK-Anteil, Umsatz-Premium, Wochentag-Skew, Uhrzeit-Muster, Routen-Dominanz, Cleaning-Impact), 5 Empfehlungen, Figures-Inventar. Alle Zahlen 1:1 aus `03_analysis.ipynb`/`02_preparation.ipynb` — keine erfundenen Werte. Kernthese von Kay bestätigt.
- Commits: `docs: PROJECTS — ...` (Workspace-Ebene, bereits vorher), `docs: project-case story — portfolio.md ...`

**Bekannt: kein Git-Remote konfiguriert** — `git remote -v` liefert nichts. Für einen späteren Push muss zuerst ein Remote (GitHub-Repo) angelegt/verknüpft werden.

**Nächster Schritt (nächste Session, von Kay explizit als eigener Task benannt):**
`/project-case slides` — Dialog-Modus: StoryView Kapitel für Kapitel aufbauen (Bezug auf `portfolio.md`-Findings), dann Overview/TechView per Wiederverwendung ableiten, Tabellen-Review vor dem Schreiben. Danach `/project-case report` (mechanisch: `make portfolio` — archive → json → html → index → md → matrix).

---

### 2026-08-28 – Portfolio-Case: slides.yaml + Views + Pages-Workflow

**Kontext:** `portfolio.md` stand (Story-Phase). Auftrag: `check` → `slides` → `report` → Pages-Workflow ergänzen → push.

**Was gemacht wurde:**
- **`/project-case check` → JA.** Fundament vollständig, Zahlen konsistent (300.000 − 6.631 = 293.369; JFK 5.649). Offene ⚠️ waren genau das, was `slides`/`report` produzieren.
- **`/project-case slides`** — `public/md/slides.yaml` als Single Source of Truth geschrieben. 10 Kapitel, 24 Slide-Einträge, Slide-Tabelle vorab von Kay abgenommen. View-Rollen nach Kay-Vorgabe (27.08.): Overview = Ergebnis + Empfehlungen ohne Methodik (10 Slides), StoryView = vollständig (20), TechView = technisch ohne Business-Empfehlungen (11). Auf Kay-Wunsch: alle TechView-Content-Slides sind auch in StoryView (nur Title/Agenda bleiben view-eigen).
- **Schema-Fallen aus dem Telefonica-Case vermieden:** `view_meta:`, `chart_refs.source` ohne `img/`-Präfix, `layout: image_left` auf dem Item, EINE Closing-Slide mit `role: closing` + `layout: split`, alle `statement` mit `layout: wide`/`lead_copy`, Text neben Charts in der `caption`. `validate_slides.py` grün.
- **`/project-case report`** — archive (alter Stub → `public/archive/v1/`) → json → html → index → md → matrix. Alle Artefakte in `public/`.
- **`.github/workflows/pages.yml`** von `fl-airport-company` kopiert (identisch mit telefonica). Fehlte hier — Ursache der 404 trotz aktiviertem Pages-Setting.
- `uv.lock` ergänzt (Lockfile gehört laut `.gitignore` in Git).
- Commit `1afe6dd` auf `claude/nyc-taxi-portfolio-setup-84c0b9`, gepusht.

**Deploy:** `HEAD:main` gepusht (Fast-Forward `e2ead39..93a38b4`, Kay explizit „auf main"). `pages.yml` lief zum ersten Mal, Deploy nach ~2 min durch. Verifiziert: Hub, alle 3 Views, `css/slides.css`, `img/*.png` → HTTP 200.

**Nächster Schritt:** `docs/PROJECTS.md` — Portfolio-Status auf `✅ portfolio-ready`.

---
