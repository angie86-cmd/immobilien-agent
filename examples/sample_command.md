# Beispiel-Command für Batchanalyse

Bitte analysiere die Datei nach SYSTEM v3.4.

## Wichtig

1. Starte mit AGENT 0 und gib zuerst den CSV-IMPORT-REPORT aus.
2. Wenn der Importstatus OK oder WARNUNG ist, führe AGENT 1 bis AGENT 4 aus.
3. Verwende den Liquiditäts-Malus basierend auf Tage online.
4. Erzeuge zusätzlich einen Filter-Audit, wenn Objekte durch den Liquiditäts-Malus unter eine Score-Schwelle fallen.
5. Gib keine Rankings, Scores oder Deep Dives aus, wenn der CSV-Import fehlschlägt.

## Gewünschter Output

- CSV-IMPORT-REPORT
- FILTER-REPORT
- ANALYSE-TABELLE sortiert nach Score final absteigend
- FILTER-AUDIT
- TOP-3 DEEP DIVE
- MAKLER-ANSCHREIBEN
- TECHNICAL EXPLANATION

## Pflichtspalten in der Analyse-Tabelle

| Spalte |
|---|
| ID |
| Stadt |
| Preis |
| €/m² |
| Alter in Tagen |
| Rendite |
| Score vor Malus |
| Liquiditäts-Malus |
| Score final |
| Klasse |
| Nächster Schritt |

## Zusätzlicher Prüfauftrag

Vergleiche Score vor Liquiditäts-Malus und Score final.

Dokumentiere, welche Objekte durch die Inseratsdauer schlechter bewertet wurden.

Markiere mögliche False Negatives.

## Spezifischer Hannover-Test

Führe zusätzlich einen Vorher/Nachher-Vergleich durch:

- Score ohne Liquiditäts-Malus
- Score mit Liquiditäts-Malus
- Differenz
- Änderung der Klassifikation
- fachliche Bewertung des Ausschlusses

Ziel:

Prüfen, ob zu viele Objekte ausgefiltert wurden oder ob Hannover aktuell tatsächlich keine attraktiven Kapitalanlageobjekte liefert.