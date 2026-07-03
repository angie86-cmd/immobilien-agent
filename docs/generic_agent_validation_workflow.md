# Generischer Testablauf – Immobilien-Agent vs. Python Liquidity Audit

## Ziel

Dieser Ablauf validiert für eine beliebige Stadt oder einen beliebigen Zielmarkt, ob der Immobilien-Agent korrekt filtert, ob Ausschlüsse plausibel sind und ob mögliche False Negatives entstanden sind. Außerdem hilft er dabei, alte Angebote mit hoher ROI als mögliche Altinserat-Renditefallen zu erkennen, statt sie vorschnell als echte Chancen zu bewerten.

Hinter alten Inseraten mit hoher ROI können sich unter anderem folgende Risiken verbergen:

- Sanierungsstau
- Sonderumlagen
- problematische WEG
- Nießbrauchrecht
- Wohnrecht
- Erbbaurecht
- niedrige Instandhaltungsrücklage
- ungeklärtes Mietverhältnis
- sonstige rechtliche oder wirtschaftliche Lasten

Der Ablauf ist generisch und gilt beispielsweise für Hannover, Leipzig, Dresden, Magdeburg, Bremen, Berlin, Braunschweig und alle zukünftigen Zielmärkte.

## 1. Variablen pro Test festlegen

Vor jedem Test diese vier Werte festlegen:

```text
STADT = <Stadt oder Zielmarkt>
CSV_DATEI = <Dateiname der ImmoMetrica-Datei>
CSV_STEM = <Dateiname ohne .csv>
AGENT_VERSION = v3_6
```

Beispiel Leipzig:

```text
STADT = Leipzig
CSV_DATEI = 20260702_offers_Leipzig.csv
CSV_STEM = 20260702_offers_Leipzig
AGENT_VERSION = v3_6
```

Erwartete Pfade:

```text
tests/fixtures/raw/<CSV_DATEI>
reports/<CSV_STEM>_agent_v3_6.csv
reports/<CSV_STEM>_liquidity_audit.csv
reports/<CSV_STEM>_agent_vs_liquidity_audit.csv
reports/<CSV_STEM>_agent_vs_liquidity_audit_summary.md
```

## 2. Umgebung vorbereiten

PowerShell öffnen und das Repository sowie die virtuelle Umgebung aktivieren:

```powershell
cd C:\dev\immobilien-agent
.\.venv\Scripts\Activate.ps1
git status
```

Danach den Parser Smoke Test ausführen:

```powershell
python .\tests\smoke_parser_test.py
```

Erwartetes Ergebnis:

```text
ALL PARSER SMOKE TESTS PASSED
```

> **Warnung:** Wenn der Smoke Test fehlschlägt, nicht mit der Agentenvalidierung fortfahren. Zuerst den Import- oder Parserfehler beheben.

## 3. Python Liquidity Audit ausführen

Generischer Befehl:

```powershell
python .\src\liquidity_audit.py --input .\tests\fixtures\raw\<CSV_DATEI>
```

Beispiel Leipzig:

```powershell
python .\src\liquidity_audit.py --input .\tests\fixtures\raw\20260702_offers_Leipzig.csv
```

Der Lauf erzeugt:

```text
reports/<CSV_STEM>_liquidity_audit.csv
```

Audit visuell öffnen:

```powershell
Import-Csv .\reports\<CSV_STEM>_liquidity_audit.csv -Delimiter ';' |
Out-GridView -Title "<STADT> Liquidity Audit"
```

Zusammenfassung nach Audit-Kategorie anzeigen:

```powershell
Import-Csv .\reports\<CSV_STEM>_liquidity_audit.csv -Delimiter ';' |
Group-Object audit_kategorie |
Select-Object Count, Name |
Format-Table -AutoSize
```

## 4. Agentenprüfung im ChatGPT-Projekt starten

Im ChatGPT-Projekt **Immobilien - Screener & Agents** einen neuen Chat öffnen.

Diese Datei hochladen:

```text
C:\dev\immobilien-agent\tests\fixtures\raw\<CSV_DATEI>
```

Anschließend den Prompt aus dem nächsten Abschnitt vollständig einfügen und die Platzhalter `<CSV_DATEI>` und `<STADT>` ersetzen.

## 5. Generischer Prompt für den Agenten

```text
Bitte analysiere die Datei <CSV_DATEI> nach SYSTEM v3.6 / SYSTEM CURRENT.

Ziel:
Ich möchte den <STADT>-Test vollständig und reproduzierbar durchführen und danach mit dem Python Liquidity Audit vergleichen.

Verbindliche Regeln:
1. Starte mit AGENT 0 und gib den CSV-IMPORT-REPORT aus.
2. Wenn der Importstatus OK oder WARNING ist, führe AGENT 1 bis AGENT 4 vollständig aus.
3. Verwende den Liquiditäts-Malus auf Basis von „Tage online“.
4. Der Liquiditäts-Malus ist kein Hard Filter.
5. Sehr alte Inserate mit hoher ROI sind nicht automatisch mögliche False Negatives. Sie können Altinserat-Renditefallen sein.
6. Erfinde keine Werte. Fehlende Daten müssen als UNVOLLSTÄNDIG / RÜCKFRAGEN markiert werden.
7. Stadtteile, Ortsteile und gültige regionale Orte innerhalb des Zielmarkts <STADT> dürfen nicht fälschlich als falsche Stadt ausgeschlossen werden.
8. Prüfe, ob zu viele Objekte ausgeschlossen wurden oder ob der Markt aktuell tatsächlich schwach ist.
9. Erstelle einen FILTER-AUDIT und ordne die Fälle, soweit zutreffend, diesen Kategorien zu:
   - berechtigt ausgeschlossen
   - Grenzfall
   - möglicher False Negative
   - Altinserat-Risiko
   - Altinserat-Renditefalle
   - Datenmangel
   - Markt aktuell schwach

Liefere genau diese Ausgabeblöcke:

A) CSV-IMPORT-REPORT

B) FILTER-REPORT

C) ANALYSE-TABELLE der Top 30 nach Score final

Verwende diese Spalten:
ID | link_immometrica | Stadt/Markt | Ort | Adresse | Preis | Wfl. | ROI (s) | Tage online | Score vor Malus | Liquiditäts-Malus | Score final | Klasse | Agent Decision | Exclusion Reason | Nächster Schritt

D) AUSSCHLUSS- UND GRENZFALL-TABELLE

Verwende diese Spalten:
ID | link_immometrica | Ort | Adresse | Preis | ROI (s) | Tage online | Liquiditäts-Malus | Score vor Malus | Score final | Klasse vorher | Klasse final | Audit-Kommentar

E) TOP-3 DEEP DIVE

F) FILTER-AUDIT-FAZIT

G) MASCHINENLESBARE CSV-TABELLE

Block G muss echter, semikolongetrennter CSV-Text sein, keine Markdown-Tabelle. Verwende exakt diesen Header:

dataset_label;link_immometrica;id;ort;adresse;titel;preis;wohnflaeche;roi_s;tage_online;score_vor_malus;liquiditaets_malus;score_final;klasse;agent_decision;exclusion_reason;risk_level;next_step

Für Block G gelten zusätzlich diese Regeln:
- Kopiere link_immometrica exakt aus der ImmoMetrica-Spalte „Details“.
- Erzeuge genau eine Zeile pro analysiertem Objekt.
- Falls die CSV-Ausgabe zu lang ist, teile sie in mehrere Teile auf.
- Wiederhole den Header nur im ersten Teil.
```

## 6. Agentenoutput lokal speichern

Diese Datei erstellen:

```text
reports/<CSV_STEM>_agent_v3_6.csv
```

Beispiel Leipzig:

```text
reports/20260702_offers_Leipzig_agent_v3_6.csv
```

Nur Block **G) MASCHINENLESBARE CSV-TABELLE** in die Datei übernehmen. Die Datei muss mit dem exakten CSV-Header aus dem Prompt beginnen.

Wenn der Agent mehrere Teile liefert:

- alle Datenzeilen in einer Datei zusammenführen
- den Header nur einmal behalten
- Markdown-Codezäune entfernen
- Markdown-Tabellentrenner entfernen

## 7. Agenten-CSV prüfen

CSV laden, Zeilenzahl prüfen und Spaltennamen anzeigen:

```powershell
$agent = Import-Csv .\reports\<CSV_STEM>_agent_v3_6.csv -Delimiter ';'
$agent.Count
$agent[0].PSObject.Properties.Name
```

CSV visuell öffnen:

```powershell
$agent | Out-GridView -Title "Agent v3.6 <STADT> Result"
```

## 8. Automatische Validierung ausführen

Generischer Befehl:

```powershell
python .\src\validate_agent_result.py --source .\tests\fixtures\raw\<CSV_DATEI> --agent .\reports\<CSV_STEM>_agent_v3_6.csv
```

Beispiel Leipzig:

```powershell
python .\src\validate_agent_result.py --source .\tests\fixtures\raw\20260702_offers_Leipzig.csv --agent .\reports\20260702_offers_Leipzig_agent_v3_6.csv
```

Die Validierung erzeugt:

```text
reports/<CSV_STEM>_agent_vs_liquidity_audit.csv
reports/<CSV_STEM>_agent_vs_liquidity_audit_summary.md
```

## 9. Validierungsergebnisse anzeigen

Markdown-Zusammenfassung öffnen:

```powershell
code .\reports\<CSV_STEM>_agent_vs_liquidity_audit_summary.md
```

Vollständige Vergleichstabelle öffnen:

```powershell
Import-Csv .\reports\<CSV_STEM>_agent_vs_liquidity_audit.csv -Delimiter ';' |
Out-GridView -Title "Agent vs Liquidity Audit - <STADT>"
```

Nur mögliche False Negatives anzeigen:

```powershell
Import-Csv .\reports\<CSV_STEM>_agent_vs_liquidity_audit.csv -Delimiter ';' |
Where-Object { $_.validation_result -eq "POTENTIAL_FALSE_NEGATIVE" } |
Out-GridView -Title "Potential False Negatives - <STADT>"
```

Zusammenfassung nach Validierungsergebnis anzeigen:

```powershell
Import-Csv .\reports\<CSV_STEM>_agent_vs_liquidity_audit.csv -Delimiter ';' |
Group-Object validation_result |
Select-Object Count, Name |
Format-Table -AutoSize
```

## 10. Interpretation der Validierung

| Validierungsergebnis | Bedeutung | Aktion |
|---|---|---|
| `POTENTIAL_FALSE_NEGATIVE` | Agent hat möglicherweise zu aggressiv ausgeschlossen | Deep Dive erforderlich |
| `EXCLUSION_SUPPORTED_BY_STALE_HIGH_ROI_RISK` | Ausschluss wird durch Altinserat + hohe ROI gestützt | Ausschluss meist plausibel, dokumentieren |
| `EXCLUSION_SUPPORTED_BY_STALE_LISTING_RISK` | Ausschluss wird durch sehr lange Online-Dauer gestützt | Ausschluss plausibel |
| `NEEDS_MANUAL_CONFIRMATION` | Ausschlussgrund oder Risiko muss manuell bestätigt werden | gezielt prüfen |
| `NEEDS_DUE_DILIGENCE_STALE_LISTING` | Nicht automatisch ausschließen, aber hohe Vorsicht | Unterlagen / WEG / Sonderumlagen prüfen |
| `LIKELY_VALID_EXCLUSION` | Ausschluss wahrscheinlich korrekt | keine weitere Prüfung nötig |
| `OK` | Kein Konflikt zwischen Agent und Audit | normal weiter |
| `MISSING_IN_AGENT_OUTPUT` | Objekt fehlt im Agentenoutput | prüfen, ob CSV-Ausgabe unvollständig war |
| `MISSING_IN_LIQUIDITY_AUDIT` | Objekt fehlt im Liquidity Audit | Parser/Audit prüfen |

`manual_review_required` bedeutet nicht automatisch, dass der Agent falsch lag. Bei alten Inseraten bedeutet es häufig: Ausschluss oder Downgrade ist plausibel, muss aber dokumentiert werden.

## 11. Commit nach erfolgreichem Test

Zuerst den Arbeitsbaum prüfen:

```powershell
git status
```

Reports hinzufügen:

```powershell
git add reports/<CSV_STEM>_liquidity_audit.csv
git add reports/<CSV_STEM>_agent_v3_6.csv
git add reports/<CSV_STEM>_agent_vs_liquidity_audit.csv
git add reports/<CSV_STEM>_agent_vs_liquidity_audit_summary.md
```

Falls Reports durch `.gitignore` ausgeschlossen sind:

```powershell
git add -f reports/<CSV_STEM>_liquidity_audit.csv
git add -f reports/<CSV_STEM>_agent_v3_6.csv
git add -f reports/<CSV_STEM>_agent_vs_liquidity_audit.csv
git add -f reports/<CSV_STEM>_agent_vs_liquidity_audit_summary.md
```

Commit erstellen und pushen:

```powershell
git commit -m "Validate <STADT> agent results against liquidity audit"
git push
```

Beispiel Leipzig:

```powershell
git commit -m "Validate Leipzig agent results against liquidity audit"
git push
```

## 12. Kurzablauf für Wiederholung

1. CSV in `tests/fixtures/raw/` ablegen.
2. Parser Smoke Test ausführen.
3. `liquidity_audit.py` für die CSV ausführen.
4. CSV im ChatGPT-Projekt vom Agenten analysieren lassen.
5. Block G als `reports/<CSV_STEM>_agent_v3_6.csv` speichern.
6. `validate_agent_result.py` ausführen.
7. Summary und Vergleich prüfen.
8. False Negatives und Altinserat-Risiken bewerten.
9. Reports committen.

## 13. Qualitätsregeln

- Keine Analyse ohne erfolgreichen CSV-Import.
- Keine Rankings aus fehlerhaft geparsten Daten.
- Keine fiktiven Renditen.
- Fehlende Daten als `UNVOLLSTÄNDIG / RÜCKFRAGEN` markieren.
- Lange Online-Dauer ist kein Hard Filter, aber ein starkes Risikosignal.
- Sehr alte High-ROI-Angebote sind häufig Altinserat-Renditefallen.
- `manual_review_required` ist ein Prüfhinweis, kein Beweis für einen Fehler des Agenten.
- Wenn der Agent alles ausschließt, muss geprüft werden, ob der Markt wirklich schwach ist oder ob False Negatives entstanden sind.
- Bei Zielmärkten dürfen Stadtteile, Ortsteile und zulässige Umlandorte nicht fälschlich als falsche Stadt ausgeschlossen werden.
