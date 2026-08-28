# NYC Taxi Routes

**Projekt:** NYC Taxi Routes
**Beschreibung:** Der komplette Projektverlauf
**Autor:** Kay Wiegand
**Zielgruppe:** Data Peers · Portfolio
**Dauer:** 14 Minuten
**Zeitraum:** 300.000 Taxifahrten, NYC 2016
**GitHub:** [kaywiegand/nyc-taxi-routes](https://github.com/kaywiegand/nyc-taxi-routes)

---


---

### Einstieg

# NYC Taxi Routes

**Nachfrage- und Routenanalyse für die JFK-Flottenplanung**
**Data-Analysis-Projekt mit Routen-Klassifikation | 300.000 Taxifahrten, NYC 2016**

* **293.369** — bereinigte Fahrten aus 300.000 Rohzeilen
* **1,93 %** — JFK-Abfahrtanteil
* **9,99 %** — des Fahrpreis-Umsatzes aus JFK-Fahrten
* **5** — nummerierte Notebooks, durchgehend reproduzierbar

## Inhaltsübersicht
*Der komplette Weg von den Rohdaten zu den Flotten-Empfehlungen*

1. Problem
2. Daten und Bereinigung
3. Routen-Klassifikation
4. Methodische Entscheidungen
5. JFK im Detail
6. Ergebnis
7. Empfehlungen
8. Grenzen


---

### Problem

## Wie viele Taxis gehören an den Flughafen JFK?
*Ein NYC-Taxiunternehmer plant seine Flotte*

> JFK liegt weit vom Zentrum
* **300.000** — Taxifahrten im Rohdatensatz, NYC 2016
* **1,93 %** — davon starten am JFK
* **keine** — Flottengröße im Datensatz — nur relative Faktoren möglich

## Keine Zielquote, sondern eine Verteilung
*Was der Auftrag genau verlangt*

> Der Auftrag nennt keine Sollgröße. Gesucht ist, wie stark die JFK-Nachfrage über Wochentag und Uhrzeit schwankt — daraus wird eine gewichtete Bereitstellung statt einer festen Zahl.
* **Anteil bestimmen**
  - Wie groß ist das JFK-Geschäft im Vergleich zum Gesamtvolumen.
  - Wie viel Umsatz hängt daran.
* **Schwankung bestimmen**
  - Wie sich der JFK-Anteil über die Woche verteilt.
  - Wie sich der JFK-Anteil über den Tag verteilt.


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


## Fast alles bleibt innerhalb der Stadt
*Finding F5 — NYC→NYC dominiert Volumen und Distanz*

* **97,21 %** — der Fahrten sind NYC→NYC
* **83,77 %** — der gefahrenen Distanz sind NYC→NYC
* **1,93 %** — der Fahrten starten am JFK
> JFK ist keine Volumen-Säule, sondern eine kleine, klar abgegrenzte Nische. Genau deshalb lohnt der zweite Blick auf ihren Wert.


---

### Methodik

## Klassifikation über Bounding-Boxes
*nyc_taxi_routes.utils.JFK / .NYC — zentral definiert, nicht in Notebooks dupliziert*

> Ein Rechteck ist eine grobe Näherung an das Flughafengelände. Es fasst die Terminal-Vorfahrten sicher, greift am Rand aber auch angrenzende Straßen mit — bewusst in Kauf genommen für eine reproduzierbare, an einer Stelle nachlesbare Regel.

## Deskriptiv, relativ, reproduzierbar
*Drei bewusste Entscheidungen zum Vorgehen*

> Die Frage ist eine Anteils- und Verteilungsfrage, keine Prognose. Jede Vereinfachung ist dokumentiert und im Code an einer Stelle nachlesbar.


---

### JFK im Detail

## 2,6 % der Fahrten, 10 % des Umsatzes
*Finding F2 — das JFK-Umsatz-Premium*

* **7.613** — Fahrten berühren den JFK (2,6 %)
* **9,99 %** — des Fahrpreis-Umsatzes entfallen darauf
* **~4×** — Umsatz je JFK-Fahrt gegenüber dem Durchschnitt
> Eine JFK-Fahrt ist rund viermal so viel wert wie eine durchschnittliche Fahrt. Die Nische ist klein im Volumen, aber überproportional im Ertrag.

## Montag trägt, Samstag fällt ab
*Finding F3 — die JFK-Nachfrage ist über die Woche nicht gleichverteilt*


## Die Wochenkurve im Direktvergleich
*Gesamtverkehr gegen JFK-Fahrten*


## Die JFK-Spitze kommt eine Stunde früher
*Finding F4 — der Tagesverlauf weicht vom Gesamtnetz ab*



---

### Ergebnis

## Kleine Nische, hoher Wert, klare Rhythmen
*Die Kernthese in einem Satz*

> JFK-Fahrten sind 1,93 % des Volumens, aber rund das Vierfache wert — mit starker Wochen- und Tagesschwankung.
* **1,93 %** — Anteil am Fahrtvolumen
* **~4×** — Umsatz je Fahrt
* **1,35× / 0,75×** — Montag über, Samstag unter dem Wochenschnitt


---

### Empfehlungen

## Fünf Maßnahmen für die Flottenplanung
*Direkt aus den vier JFK-Findings abgeleitet*



---

### Grenzen

## Was diese Analyse nicht leisten kann
*Aussagegrenzen, offen benannt*



---

### Ende

## NYC Taxi Routes
*Nachfrage- und Routenanalyse für die JFK-Flottenplanung<br>Data-Analysis-Projekt mit Routen-Klassifikation | 300.000 Taxifahrten, NYC 2016*

> Eine Nische richtig einordnen
