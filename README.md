# Immobilien Kapitalanlage Agent

Repository für die Versionierung der Prompts, Parser-Regeln, Scoring-Logik und Testprotokolle des Immobilien-Kapitalanlage-Agenten.

## Ziel

Der Agent analysiert ImmoMetrica-Daten als Kapitalanlage auf dem deutschen Markt.

## Aktuelle Architektur

1. AGENT 0 – CSV Import & Parser Validation Agent
2. AGENT 1 – Email & CSV Filter Agent
3. AGENT 2 – Kapitalanlage Analyst Agent
4. AGENT 3 – Safety & Due Diligence Agent
5. AGENT 4 – Final Summary Agent

## Aktuelle Version

System Prompt: v3.4

## Wichtige Änderungen in v3.4

- Robuster ImmoMetrica CSV-Parser
- Unterstützung für Standard-CSV, deutsches Semikolon-CSV und Tabulator
- UTF-8-SIG-Unterstützung wegen möglichem BOM
- Normalisierung deutscher Zahlenformate
- CSV-IMPORT-REPORT vor jeder Analyse
- Liquiditäts-Malus über Tage online
- Filter-Audit für Vorher/Nachher-Vergleich
- Explizite Prüfung, ob Objekte durch den Liquiditäts-Malus zu streng ausgefiltert wurden

## Nächster Prüfauftrag

Hannover-Test erneut prüfen:

- Vergleich vor und nach Anpassung des Scorings bezüglich Inseratsdauer
- Prüfen, welche Objekte schlechter bewertet oder herausgefiltert wurden
- False Negatives identifizieren
- Entscheiden, ob der Filter zu streng ist oder Hannover aktuell keine attraktiven Objekte liefert

## Grundprinzip

Keine Investmentanalyse ohne erfolgreichen CSV-Import.

Wenn die Datei nicht korrekt geparst werden kann, darf der Agent keine Scores, Rankings oder Deep Dives erzeugen.