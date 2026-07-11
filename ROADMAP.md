# ROADMAP.md – NYC Taxi Routes

> Ausgangslage → Phasen → Ziel

---

## Ausgangslage

StackFuel-Übungsprojekt (Modul 2 / Kapitel 7): Ein NYC-Taxiunternehmer will wissen, wie viele Taxis er
am Flughafen JFK bereitstellen soll. Datensatz: 300.000 Taxifahrten, NYC 2016.
Volle Aufgabenstellung: [`docs/infos.md`](docs/infos.md).

---

## Phase 1 — Setup & Daten ✅ ABGESCHLOSSEN

- ✅ Projektstruktur (wgnd-scaffolding, Typ DA)
- ✅ Rohdaten geladen und geprüft (`00_introduction.ipynb`, `01_exploration.ipynb`)
- ✅ Fundament-Nachzug 2026-07-11: Git-Repo, aktuelle MD-Struktur, Package-Rename `nyc_taxi_routes`

## Phase 2 — EDA ✅ ABGESCHLOSSEN

- ✅ Explorative Datenanalyse (`01_exploration.ipynb`)
- ✅ Erste Visualisierungen
- ✅ Cleaning-Strategie + Feature-Ideen abgeleitet

## Phase 3 — Preparation & Feature Engineering ✅ ABGESCHLOSSEN

- ✅ Cleaning-Pipeline (`data/cleaning.py` — Messfehler vs. Business-Scope getrennt)
- ✅ Feature Engineering (`features/engineering.py` — Geo-Routen, ökonomische Kennzahlen, Zeit-Segmente, Log-Transforms)
- ✅ Export nach `data/processed/` (`02_preparation.ipynb`)

## Phase 4 — Analyse 🔄 TEILWEISE ABGESCHLOSSEN

- ✅ Kernfrage beantwortet: Anteil JFK-Abfahrten an Gesamtfahrten (`03_analysis.ipynb`)
- ⬜ Visualisierung der Pickup-Standorte in NYC
- ⬜ JFK-Anteil pro Wochentag (höchster/niedrigster Tag)
- ⬜ Wochentags-Verteilung Gesamt vs. JFK
- ⬜ Uhrzeit-Verteilung Gesamt vs. JFK

## Phase 5 — Communication & Insights ⬜ OFFEN

- ⬜ Executive Summary (`04_insights.ipynb`)
- ⬜ Empfehlung an den Taxiunternehmer formulieren
- ⬜ Public-Artefakte (`public/index.html`) mit echten Findings befüllen

---

## Ziel

Belastbare, mit Zahlen unterlegte Empfehlung, wie viele Taxis der Unternehmer am JFK bereitstellen sollte —
inklusive der zeitlichen Schwankungen (Wochentag/Uhrzeit), die die Flottenplanung steuern.
