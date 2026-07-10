#### Übungsprojekt: Analyse von Taxidaten
Modul 2 | Kapitel 7 | Notebook 2

***
In dieser Praxisübung erhältst du ein relativ großes Datenset, welches Taxi-Fahrten in New York beinhaltet.

Das Datenset enthält 300000 Fahrten (Zeilen). An solchen Datensets zeigt sich die Stärke von Python. Excel z.B. kann nicht mit so vielen Zeilen arbeiten und würde außerdem bereits bei weniger Daten sehr viel Arbeitsspeicher verbrauchen, wodurch lange Wartezeiten entstehen können.

Am Ende der Übung hast du selbstständig:

* ein Datenset aufbereitet
* konkrete Fragen beantwortet und Visualisierungen erstellt

**Tipp:** Wir empfehlen dir, die Aufgaben zunächst in diesem Notebook mit relativ wenig Anleitung zu lösen. Bleibst du stecken, oder brauchst du mehr Hilfestellungen, kannst du zu *[Hilfestellung für Projekt: Analyse von Taxidaten](./x03-exercise.ipynb) (Kapitel 7)* wechseln. Da findest du das gleiche Projekt mit mehr Anleitung.
***

**Szenario:** Ein New Yorker Taxiunternehmer möchte die Anzahl seiner Taxis, welche am internationalen Flughafen JFK warten, optimieren.
Der Flughafen liegt deutlich abseits des Hauptgeschäftsgebiets Manhattan. Dadurch dauert es einerseits sehr lange, bis dort wartende Taxis für andere Gebiete verfügbar werden. Andererseits legen am Flughafen ankommende Gäste in der Regel weitere und somit lukrativere Strecken zurück. Wie viele Taxis sollte der Taxi-Unternehmer also am JFK-Flughafen bereitstellen?

Um seine Fragestellungen zu untersuchen, stellt er dir seine gesammelten Daten aus dem Jahr 2016 in der Datei *2016_Yellow_Taxi_prepared.csv* zur Verfügung.



Die folgenden Aufgaben gilt es zu lösen:

**1)** Daten einlesen, überprüfen und reinigen

**2)** Daten filtern

**3)** Wie hoch ist der Anteil an Taxis, die vom Flughafen (JFK) aus gebucht werden insgesamt? Diese Auswertung stellt also folgende Formel dar:

\begin{equation*}
Anteil_{\mathrm{JFK}} = \frac{Fahrten_\mathrm{JFK}}{Fahrten_\mathrm{überall}}
\end{equation*}

**4)** Wo werden Taxis in New York genommen? Erstelle eine Visualisierung der Startpunkte der Taxifahrten.

**5)** Wie hoch ist der Anteil an Taxis, die vom Flughafen aus gebucht werden pro Wochentag? An welchem Wochentag gibt es den höchsten Anteil und wann den niedrigsten? Diese Auswertung stellt also folgende Formel dar:

\begin{equation*}
Anteil_\mathrm{Wochentag,\ JFK} = \frac{Fahrten_\mathrm{Wochentag,\ JFK}}{Fahrten_\mathrm{Wochentag,\ überall}}
\end{equation*}

**6)** Erstelle eine Visualisierung, anhand derer man sieht, welchen Anteil ein **Wochentag** an der Anzahl der Fahrten insgesamt hat. Dies soll sowohl für die Fahrten vom Flughafen aus gemacht werden als auch für das Gesamtset, um etwaige Unterschiede erkennen zu können. Diese beiden Visualisierungen stellen also folgende Formeln dar:

\begin{equation*}
Anteil_{\mathrm{Wochentag,\ überall}} = \frac{Fahrten_\mathrm{Wochentag,\ überall}}{Fahrten_\mathrm{Alle\ Tage,\ überall}}
\end{equation*}

\begin{equation*}
Anteil_\mathrm{Wochentag,\ JFK} = \frac{Fahrten_\mathrm{Wochentag,\ JFK}}{Fahrten_\mathrm{Alle\ Tage,\ JFK}}
\end{equation*}



**7)** Erstelle eine Visualisierung, anhand derer man sieht, welchen Anteil eine **Uhrzeit** an der Anzahl der Fahrten insgesamt hat. Dies soll sowohl für die Fahrten vom Flughafen aus gemacht werden als auch für das Gesamtset, um etwaige Unterschiede erkennen zu können. Diese beiden Visualisierungen stellen also folgende Formeln dar:

\begin{equation*}
Anteil_{\mathrm{Uhrzeit,\ überall}} = \frac{Fahrten_\mathrm{Uhrzeit,\ überall}}{Fahrten_\mathrm{Alle\ Uhrzeiten,\ überall}}
\end{equation*}

\begin{equation*}
Anteil_\mathrm{Uhrzeit,\ JFK} = \frac{Fahrten_\mathrm{Uhrzeit,\ JFK}}{Fahrten_\mathrm{Alle\ Uhrzeiten,\ JFK}}
\end{equation*}

**8)** Individualisierung der Visualisierungen

**9)** Formulierung der Empfehlung

Wir wünschen dir viel Erfolg und vor allem Spaß bei der Bearbeitung der Aufgaben!


Bei der Bearbeitung der Aufgaben empfehlen wir dir, die vorgegebene Reihenfolge beizubehalten.

In diesem Notebook hast du viel Freiraum. Wir haben dir lediglich die oben genannten Schritte als Überschriften vorgegeben. Weiter unten findest du Beispielabbildungen für die visuellen Aufgabenstellungen. Wenn du zusätzliche Codezellen benötigst, so kannst du sie einfach neu hinzufügen (mit dem + in der oberen Leiste, neben dem Speichernknopf, siehe *[Ein erster Pythoneindruck](../../module-01/chapter-01-solutions/01-solution.ipynb) (Modul 1, Kapitel 1)*).

![New_Cell](2_07_02_button.png)

Probiere dich in dieser Übung einfach etwas aus. Falls du einmal nicht so recht weiterkommst, dann wirf einen Blick in die Übung *[Hilfestellung für Projekt: Analyse von Taxidaten](../chapter-07/03-exercise.ipynb)*.

Dort sind mehr Empfehlungen und Tipps zum Vorgehen gegeben. Welche dieser beiden Übungen du nutzt, um das Projekt abzuschließen, ist ganz dir überlassen. Bedenke immer, wenn du einmal mit dem Code nicht weiterkommst, dann sind Suchmaschinen deine besten Freunde! Wenn auch das nicht hilft, steht StackFuels Support dir natürlich auch noch zur Seite.


Die Daten sind folgendermaßen strukturiert:

Spaltennummer | Spaltenname       | Datenniveau           | Beschreibung
 ------------ | :---------:       | :---------:           | ------------:
0             | `'pickup_weekday'`    | kategorisch (ordinal) | Wochentag, an dem die Fahrt begonnen hat (0=Montag, 6=Sonntag)
1             | `'pickup_hour'`       | kategorisch (ordinal) | Stunde, in der die Fahrt begonnen hat
2             | `'pickup_longitude'`  | numerisch (`float`)   | Längengrad, bei dem die Fahrt begonnen hat
3             | `'pickup_latitude'`   | numerisch (`float`)   | Breitengrad, bei dem die Fahrt begonnen hat
4             | `'dropoff_longitude'` | numerisch (`float`)   | Längengrad, bei dem die Fahrt geendet hat
5             | `'dropoff_latitude'`  | numerisch (`float`)   | Breitengrad, bei dem die Fahrt geendet hat
6             | `'passenger_count'`   | kategorisch (ordinal) | Anzahl der Passagiere im Auto. Dieser Wert wird manuell erfasst
7             | `'trip_distance'`     | numerisch (`float`)   | Zurückgelegte Fahrtstrecke in Meilen.
8             | `'fare_amount'`       | numerisch (`float`)   | Betrag, den das Taxameter basierend auf Zeit und Strecke berechnet
9             | `'tip_amount'`        | numerisch (`float`)   | Trinkgeld, welches bei Kartenzahlung gegeben wird (0.00 bei Barzahlung)
10            | `'tolls_amount'`      | numerisch (`float`)   | Angefallene Maut-Gebühren
11            | `'payment_type'`      | kategorisch (nominal) | Art der Zahlung (1=Kreditkarte, 2=Bar, 3=keine Gebühr, 4=Streitigkeit)



Um zu bestimmen, welche Fahrten beim Flughafen JFK starten, erhältst du die folgenden Koordinaten:

Variable      | Wert              | Beschreibung  
------------- | :---------:       | ---------:           
`jfk_max_lat`   | `40.66018`          | Maximaler *Pickup*-Breitengrad der Flughafenfahrten 
`jfk_min_lat`   | `40.62666`          | Minimaler *Pickup*-Breitengrad der Flughafenfahrten 
`jfk_max_long`  | `-73.76599`         | Maximaler *Pickup*-Längengrad der Flughafenfahrten 
`jfk_min_long`  | `-73.80822`         | Minimaler *Pickup*-Längengrad der Flughafenfahrten   



Die Koordinaten von New York City lauten übrigens ungefähr so:

Variable      | Wert              | Beschreibung  
------------- | :---------:       | ---------:           
`nyc_max_lat`   | `40.9176`          | Maximaler Breitengrad von New York City
`nyc_min_lat`   | `40.5774`          | Minimaler Breitengrad von New York City 
`nyc_max_long`  | `-73.7004`         | Maximaler Längengrad von New York City
`nyc_min_long`  | `-74.15`         | Minimaler Längengrad von New York City



## **1)** Data Gathering and Cleaning
Bei dieser Teilaufgabe wirst du Wissen aus den folgenden Lektionen benötigen:

* *[Daten aufbereiten mit pandas](../chapter-01-solutions/05-solution.ipynb) (Kapitel 1)*
* *[Daten explorieren](../chapter-02-solutions/03-solution.ipynb) (Kapitel 2)*
* *[Datensätze mit NaNs reinigen](../chapter-03-solutions/03-solution.ipynb) (Kapitel 3)*
* *[Boolesche Maskierung](../chapter-04-solutions/06-solution.ipynb) (Kapitel 4)* 
* *[Daten in Excel-Datei speichern](../chapter-06-solutions/04-solution.ipynb) (Kapitel 6)*



**Achtung**: Der einzulesende Datensatz ist mit 300000 Taxifahrten relativ groß und benötigt daher auch relativ viele Ressourcen. Da die Codeausführung im Data Lab über einen Server läuft, kann es je nach derzeitiger Serverauslastung etwas länger dauern, bis die Datei eingelesen ist. Bitte öffne aufgrund der Größe diese Datei <u>nicht</u> im Editor des Data Labs!

Jedoch gibt es eine einfache Möglichkeit, den RAM-Bedarf selbst deutlich zu reduzieren. Die Funktion `pd.read_csv()` bietet den Parameter `dtype` an. Mit diesem kann jeder Spalte ein Datentyp manuell zugeordnet werden. Standardmäßig werden ganze Zahlen z.B. als `int64` eingelesen, d.h. jede Zahl benötigt 64 Bits im Speicher. Je größer dieser Wert, umso größere ganze Zahlen können gespeichert werden. Für Fließkommazahlen steigt die Genauigkeit, mit der sie gespeichert werden. Unsere Daten bewegen sich allerdings in einem Bereich, der solch eine große Speichergröße nicht benötigt. Werden die Zahlen z.B. als `int32` eingelesen, so wird nur noch die Hälfte an RAM vom DataFrame benötigt. Mit dem folgenden *dictionary* kannst du den Datensatz speicherarm einlesen:
```python
col_dtypes = {'pickup_weekday': 'int16', 
              'pickup_hour': 'int16', 
              'pickup_longitude': 'float32', 
              'pickup_latitude': 'float32', 
              'dropoff_longitude': 'float32', 
              'dropoff_latitude': 'float32', 
              'passenger_count': 'int16', 
              'trip_distance': 'float32', 
              'fare_amount': 'float32', 
              'tip_amount': 'float32', 
              'tolls_amount': 'float32', 
              'payment_type': 'int16'}

df = pd.read_csv('2016_Yellow_Taxi_prepared.csv', dtype=col_dtypes)
```

        
