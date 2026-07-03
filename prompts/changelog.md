# Changelog

## v3.6

Datum: 2026-07-03

- Zielstadt-Logik durch Zielmarkt-/Zielregion-Logik ersetzt; Hannover-Batches schließen Region Hannover und umliegende Kommunen ein.
- Sehr alte Angebote mit attraktiver ROI als Altinserat-Risiko beziehungsweise Altinserat-Renditefalle statt automatisch als möglichen False Negative eingeordnet.
- Filter-Audit um getrennte Kategorien für stale listing risk, stale high-ROI traps, Due Diligence und berechtigte Ausschlüsse erweitert.
- Bedeutung von `manual_review_required` als Prüfhinweis statt Fehlerurteil präzisiert.

## v3.5

Datum: 2026-07-03

- Kanonischen Prompt vereinheitlicht.
- `system-current.md` als einzige Quelle für Repository und ChatGPT Project Instructions eingeführt.
- Identischen versionierten Stand als `system-v3.5.md` abgelegt.
- Unter dem Zeichenlimit der ChatGPT Project Instructions gehalten.
- v3.4 als vorherigen ausführlichen Entwurf archiviert; v3.5/system-current ist aktiv.

## v3.4

Datum: 2026-07-02

- AGENT 0 für CSV Import & Parser Validation ergänzt.
- Standard-CSV, deutsches Semikolon-CSV, Tabulator, UTF-8-SIG und deutsche Zahlenformate festgelegt.
- CSV-IMPORT-REPORT als Voraussetzung jeder Investmentanalyse eingeführt.
- Liquiditäts-Malus als Score-Malus statt Hard Filter präzisiert.
- Score vor Malus, Malus und finaler Score separat ausgewiesen.
- Filter-Audit und Prüfung möglicher False Negatives ergänzt.
- Python-Beispielparser ergänzt.

## v3.3

- Robusten CSV-Parser in die Systemanweisungen aufgenommen.
- ImmoMetrica-Dateien werden nicht mehr pauschal als Komma-CSV behandelt.
- Parsingfehler dürfen nicht zu erfundenen Rankings führen.

## v3.2

- Multi-Agenten-Workflow eingeführt.
- Liquiditäts-Malus über Tage online ergänzt.
- Relaxed Hard-Exclusion und 100-Punkte-Scoring-Modell eingeführt.
