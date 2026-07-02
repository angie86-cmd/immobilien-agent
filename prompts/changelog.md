# Changelog

## v3.4

Datum: 2026-07-02

Änderungen:

- AGENT 0 für CSV Import & Parser Validation ergänzt.
- Parser muss Standard-CSV, deutsches Semikolon-CSV und Tabulator akzeptieren.
- UTF-8-SIG und deutsche Zahlenformate verpflichtend.
- CSV-IMPORT-REPORT eingeführt.
- Investmentanalyse darf erst nach erfolgreichem Import starten.
- Liquiditäts-Malus präzisiert: kein Hard Filter, sondern Score-Malus und Risikosignal.
- Score vor Malus, Malus und Score final müssen separat ausgegeben werden.
- Filter-Audit für Hannover-Test ergänzt.
- Prüfung möglicher False Negatives ergänzt.
- Python-Beispielparser ergänzt.

## v3.3

Änderungen:

- Robuster CSV-Parser in die System-Instruktionen aufgenommen.
- ImmoMetrica CSV darf nicht mehr als reines Komma-CSV angenommen werden.
- Parsingfehler dürfen nicht mehr zu erfundenen Rankings führen.

## v3.2

Änderungen:

- Multi-Agenten-Modus mit vier Agenten.
- Liquiditäts-Malus über Tage online eingeführt.
- Relaxed Hard-Exclusion.
- Scoring-Modell mit 100 Punkten.