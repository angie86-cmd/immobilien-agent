# Architektur - Immobilien Kapitalanlage Agent

## Zielarchitektur

ImmoMetrica E-Mail / CSV / Export

↓  

AGENT 0 - CSV Import & Parser Validation Agent

↓  

AGENT 1 - Email & CSV Filter Agent

↓  

AGENT 2 - Kapitalanlage Analyst Agent

↓  

AGENT 3 - Safety & Due Diligence Agent

↓  

AGENT 4 - Final Summary Agent

## Prinzipien

- Keine Investmentanalyse ohne erfolgreichen Import.
- Keine erfundenen Scores.
- Datenlücken werden markiert, nicht geraten.
- Liquiditäts-Malus ist Risikosignal, kein pauschaler Ausschluss.
- Cluster und Duplikate müssen sichtbar markiert werden.
- Makler-Kommunikation immer auf Deutsch, semiformal.
- Filter-Audit prüft aktiv mögliche False Negatives.
- Alte Inserate können Verhandlungschancen sein, wenn Rendite, Lage und Datenlage plausibel sind.

## Agentenverantwortung

| Agent | Verantwortung |
|---|---|
| AGENT 0 | Import, Parser, technische Validierung |
| AGENT 1 | Strukturierung, ID, Duplikate, Hard Filter |
| AGENT 2 | Rendite, Cashflow, Score, Liquiditäts-Malus |
| AGENT 3 | Safety, Due Diligence, Maklerfragen |
| AGENT 4 | Entscheidungsvorlage, Tabellen, Deep Dive, Filter-Audit |

## Datenfluss

| Schritt | Input | Output |
|---|---|---|
| Import | CSV / E-Mail / Export | strukturierte Tabelle |
| Filter | strukturierte Tabelle | bereinigte Objektliste |
| Analyse | Objektliste | Kennzahlen und Scores |
| Safety | Scores + Objektdaten | Risiken und Rückfragen |
| Summary | vollständige Analyse | Entscheidungsvorlage |

## Technische Leitplanken

1. CSV-Dateien dürfen nie blind als Komma-CSV gelesen werden.
2. ImmoMetrica kann Semikolon-CSV liefern.
3. UTF-8-SIG muss unterstützt werden.
4. Deutsche Zahlenformate müssen normalisiert werden.
5. Fehlende Daten dürfen nicht geraten werden.
6. Kein Score ohne valide Mindestdaten.
7. Jeder Ausschluss muss begründet werden.