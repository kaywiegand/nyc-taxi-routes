# Portfolio Summary — NYC Taxi Routes
<!-- Interface-Datei: Wird von /project-case story befüllt.
     Einzige Zahlenquelle für /project-case report und /project-case slides.
     KEINE Inhalte aus Notebooks kopieren — nur kuratierte Kernaussagen.
-->

---

## Project

```
name:       NYC Taxi Routes
slug:       nyc-taxi-routes
type:       DA
stage:      Phase 5 — Analysis + Insights complete, all 9 business questions answered
target:     JFK departure share (share of trips departing from JFK airport)
stack:      Python · Pandas · Scikit-learn · Matplotlib/Seaborn · Plotly · Folium · wgnd-toolkit · Jupyter
period:     300.000 Taxifahrten, NYC 2016
rows:       293,369 (cleaned, from 300,000 raw)
notebooks:  5
findings:   6
dashboard:  — (not deployed, DA project, no dashboard planned)
```

---

## Storyline

```
thesis:     JFK trips are a small (1.93%) but disproportionately valuable (~4x revenue) niche with
            strong weekday and hourly seasonality — a flat fleet allocation would systematically
            under-serve Mondays and early mornings while over-serving Saturdays.
hook:       A JFK trip earns roughly 4x the revenue of an average trip, yet only 1.93% of trips
            actually depart from there.
proof:      Route classification (JFK/NYC/Other) → revenue-share comparison → weekday breakdown →
            hourly breakdown — each step narrows the "how many taxis" question into concrete,
            time-sliced allocation factors.
so_what:    Fleet allocation should follow a weekday/hour-weighted schedule, not a flat share —
            captures the JFK revenue premium without stranding taxis during off-peak windows.
```

---

## Problem

```
kpi_name:   JFK departure share
kpi_ist:    1.93% (5,649 of 293,369 trips)
kpi_soll:   n/a — descriptive fleet-sizing question, not a target-vs-gap KPI
kpi_gap:    n/a
problem_statement: |
  A NYC taxi fleet operator wants to know how many taxis to station at JFK airport. JFK sits far
  from Manhattan's core business district, so taxis dropping passengers there take long to
  reposition — but JFK-bound passengers travel longer, more lucrative routes. The 2016 Yellow
  Taxi dataset (300k trips) is used to quantify JFK's actual share of business and its time
  patterns, to inform a fleet allocation that isn't just a flat percentage.
```

---

## Key Findings
<!-- Max 6 Findings — jeweils mit konkreter Zahl und Quelle-Notebook -->

### F1 — JFK Departure Share
```
finding:   Only a small fraction of all trips actually depart from JFK.
number:    1.93% (5,649 of 293,369 cleaned trips)
source:    03_analysis.ipynb
```

### F2 — JFK Revenue Premium
```
finding:   Trips touching JFK (pickup or dropoff) generate far more revenue per trip than average.
number:    7,613 trips (2.6%) generate 9.99% of fare revenue — ~4x an average trip
source:    03_analysis.ipynb
```

### F3 — Weekday Skew
```
finding:   JFK demand is not flat across the week — Monday leads, Saturday lags.
number:    Monday 2.60% JFK share (highest) vs. Saturday 1.44% (lowest); Monday is 1.35x
           overrepresented among JFK trips, Saturday 0.75x underrepresented
source:    03_analysis.ipynb
```

### F4 — Hourly Pattern
```
finding:   JFK's peak hour comes earlier than the network-wide peak, and early-morning JFK
           share runs far above general traffic at that hour.
number:    JFK peak 17:00 vs. network peak 18:00; 5–6am JFK share ~2x general traffic share
source:    03_analysis.ipynb
```

### F5 — Route Dominance
```
finding:   The overwhelming majority of trips and distance stay entirely within the NYC metro
           area — JFK is a small, distinct niche, not a core volume driver.
number:    97.21% of trips, 83.77% of distance are NYC→NYC
source:    03_analysis.ipynb
```

### F6 — Data Cleaning Impact
```
finding:   Cleaning removed a small but meaningful share of rows via technical-error and
           business-scope masks (duplicates, invalid geo/fare/distance/passenger values).
number:    6,631 rows removed (2.2% of 300,000 raw rows)
source:    02_preparation.ipynb
```

---

## Model Results
<!-- Nur befüllen wenn ML-Projekt (Typ DS) -->

n/a — DA project, no modeling in scope.

---

## Figures
<!-- Alle relevanten Exports in public/img/ — für Report und Slides -->

```yaml
geo:
  - img/pickup_locations_map.png           # Pickup/dropoff scatter, classified JFK/NYC/Other

temporal:
  - img/jfk_share_by_weekday.png           # JFK departure share per weekday, Monday highest
  - img/weekday_distribution_overall_vs_jfk.png  # Weekday distribution, all trips vs. JFK
  - img/hourly_distribution_overall_vs_jfk.png   # Hourly distribution, all trips vs. JFK

routes:
  - img/route_distribution_log.png         # Trip count per route type, log scale
```

---

## Recommendations

```
r1:
  title:  Monday uplift
  detail: Station ~35% more JFK taxis on Mondays than the weekly average — Monday accounts for
          20.61% of all JFK trips vs. only 15.24% of all trips (1.35x skew).

r2:
  title:  Saturday reduction
  detail: Reduce JFK presence ~25% on Saturdays vs. the weekly average — Saturday accounts for
          only 11.38% of JFK trips vs. 15.23% of all trips (0.75x skew).

r3:
  title:  Early-shift coverage
  detail: Double early-morning (5–7am) JFK coverage relative to general demand at that hour —
          JFK share is ~2x the overall traffic share during those hours (likely early flight
          departures).

r4:
  title:  Shift the evening peak
  detail: JFK's own peak hour is 17:00, an hour before the network-wide peak of 18:00 — schedule
          the JFK evening shift accordingly instead of following general traffic patterns.

r5:
  title:  Prioritize JFK return fares
  detail: Favor NYC→JFK return trips over idle repositioning — JFK-touching trips earn roughly
          4x an average trip's revenue.
```

---

## Status

```
generated_by:   /project-case story
generated_at:   2026-07-11
summary_version: 1
portfolio_check: ✅ passed
report_html:    ❌ pending
slides_html:    ❌ pending
dashboard:      ❌ not deployed — DA project, no dashboard planned
```
