# Testplan Leipzig - CSV Parser und Batchanalyse

## Ziel

Validieren, dass die ImmoMetrica-Datei korrekt eingelesen wird und die Analyse reproduzierbar ist.

## Bekannter Datensatz

Datei:

`20260702_offers_Leipzig.csv`

Bekannte technische Eigenschaften:

| Kriterium | Erwartung |
|---|---|
| Encoding | UTF-8-SIG |
| Delimiter | Semikolon |
| Zeilen gesamt | 334 |
| Datenobjekte | 333 |
| Spalten | 46 |

## Prüfschritte

1. Parser erkennt Delimiter korrekt als Semikolon.
2. Parser erkennt Kernspalten.
3. Agent erzeugt CSV-IMPORT-REPORT.
4. Agent startet Analyse nur bei Importstatus OK oder WARNUNG.
5. Kein Ranking erzeugen, wenn Importstatus FEHLER.
6. Top-Objekte mit Originaldaten plausibilisieren.
7. Scores dürfen nur aus tatsächlich geparsten Daten berechnet werden.

## Erwarteter Import-Report

| Kriterium | Erwartung |
|---|---|
| Encoding | UTF-8-SIG |
| Delimiter | `;` |
| Datenobjekte | 333 |
| Spalten | 46 |
| Importstatus | OK |

## Regression Test

Der Parser darf nicht erneut mit folgendem Fehler abbrechen:

`Expected X fields, saw Y`

Falls dieser Fehler auftritt, muss automatisch mit einem anderen Delimiter weitergetestet werden.