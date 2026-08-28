# NYC Taxi Routes

**Projekt:** NYC Taxi Routes
**Beschreibung:** Technischer Deep Dive
**Autor:** Kay Wiegand
**Zielgruppe:** Data Scientists · Tech Leads · Interviewer
**Dauer:** 9 Minuten
**Zeitraum:** 300.000 Taxifahrten, NYC 2016
**GitHub:** [kaywiegand/nyc-taxi-routes](https://github.com/kaywiegand/nyc-taxi-routes)

---


---

### Einstieg

# NYC Taxi Routes

**Nachfrage- und Routenanalyse für die JFK-Flottenplanung**
**Data-Analysis-Projekt mit Routen-Klassifikation | 300.000 Taxifahrten, NYC 2016**

* **6.631** — Zeilen über Fehler- und Scope-Masken entfernt
* **2** — Bounding-Boxes klassifizieren jede Fahrt
* **9** — mögliche Routentypen
* **0** — Fehler-Outputs in 5 Notebooks

## Inhaltsübersicht
*Datenaufbereitung, Geo-Klassifikation und Methodik*

1. Daten und Bereinigung
2. Routen-Klassifikation
3. Geo-Bounds und Methodik
4. Grenzen


---

### Daten

## Ein Datensatz, 2016er Yellow-Taxi-Fahrten
*Aufbereiteter CSV-Auszug aus dem StackFuel-Übungsprojekt*

> Keine Fahrzeug-IDs, keine Flottengröße. Jede Empfehlung ist ein relativer Faktor auf den Wochenschnitt, keine Stückzahl.

## Messfehler von Geschäfts-Scope getrennt
*Zwei Arten von Masken, unterschiedlich begründet*

> 6.631 Zeilen entfernt, 2,2 % der Rohdaten. Klein genug, um die Verteilungen nicht zu verzerren, groß genug, um die Extremwerte aus den Kennzahlen zu halten.

## Abgeleitete Spalten für die Analyse
*features/engineering.py — Geo, Ökonomie, Zeit*

> Die Klassifikations- und Ökonomie-Spalten tragen die gesamte spätere Analyse. Sie entstehen einmal in der Preparation und werden exportiert.


---

### Routen

## Neun Routentypen aus zwei Gebieten
*Jede Fahrt bekommt ein Abfahrts- und ein Ankunftsgebiet: JFK, NYC oder Other*


## Wo die Fahrten beginnen
*Pickup- und Dropoff-Punkte, klassifiziert nach JFK / NYC / Other*



---

### Methodik

## Klassifikation über Bounding-Boxes
*nyc_taxi_routes.utils.JFK / .NYC — zentral definiert, nicht in Notebooks dupliziert*

> Ein Rechteck ist eine grobe Näherung an das Flughafengelände. Es fasst die Terminal-Vorfahrten sicher, greift am Rand aber auch angrenzende Straßen mit — bewusst in Kauf genommen für eine reproduzierbare, an einer Stelle nachlesbare Regel.

## Deskriptiv, relativ, reproduzierbar
*Drei bewusste Entscheidungen zum Vorgehen*

> Die Frage ist eine Anteils- und Verteilungsfrage, keine Prognose. Jede Vereinfachung ist dokumentiert und im Code an einer Stelle nachlesbar.


---

### Grenzen

## Was diese Analyse nicht leisten kann
*Aussagegrenzen, offen benannt*



---

### Ende

## NYC Taxi Routes
*Nachfrage- und Routenanalyse für die JFK-Flottenplanung<br>Data-Analysis-Projekt mit Routen-Klassifikation | 300.000 Taxifahrten, NYC 2016*

> Eine Nische richtig einordnen
