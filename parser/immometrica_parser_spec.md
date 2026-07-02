# ImmoMetrica CSV Parser Specification

## Problem

ImmoMetrica-Dateien können je nach Umgebung als Standard-CSV oder deutsches Excel-CSV interpretiert werden.

Ein falscher Parser mit Komma kann Fehler erzeugen wie:

`Expected X fields, saw Y`

## Ziel

Der Parser muss beide Formate akzeptieren:

- Standard-CSV mit Komma
- Deutsches CSV mit Semikolon
- Tabulator-getrennte Dateien

## Requirements

1. UTF-8-SIG verwenden.
2. Delimiter automatisch erkennen.
3. Semikolon zuerst testen.
4. Danach Komma testen.
5. Danach Tabulator testen.
6. Deutsche Zahlen normalisieren.
7. Import-Report erzeugen.
8. Bei Importfehler keine Investmentanalyse starten.
9. Bei Parserfehlern nicht abbrechen, sondern anderen Delimiter testen.
10. Spalten-Aliase für ImmoMetrica-Kernfelder unterstützen.

## Bekannter Datensatz

Datei:

`20260702_offers_Leipzig.csv`

Bekannte technische Eigenschaften:

| Eigenschaft | Wert |
|---|---:|
| Encoding | UTF-8 mit BOM |
| Delimiter | Semikolon |
| Zeilen gesamt | 334 |
| Datenobjekte | 333 |
| Spalten | 46 |

## Normalisierung

| Input | Output |
|---|---:|
| `7,8 %` | `7.8` |
| `68,0` | `68.0` |
| `150.000 €` | `150000` |
| `1.234,56` | `1234.56` |

## Kernspalten

- PLZ
- Ort
- Adresse
- Titel
- Kaufpreis oder Preis
- Wohnfläche oder Fläche
- ROI (s), ROI (i), Rendite oder Bruttorendite
- Tage online, Aktiv, Online seit oder Datum
- Hausgeld
- Bj oder Baujahr

## Import Report

Pflichtfelder:

| Feld | Beschreibung |
|---|---|
| Encoding | erkannte oder verwendete Codierung |
| Delimiter | `;`, `,` oder `\t` |
| Zeilen gesamt | Anzahl inklusive Header |
| Datenobjekte | Anzahl ohne Header |
| Spaltenanzahl | Anzahl erkannter Spalten |
| erkannte Kernspalten | Liste oder Anzahl |
| fehlerhafte Zeilen | Anzahl |
| stabile Spaltenanzahl | Ja / Nein |
| Importstatus | OK / WARNUNG / FEHLER |

## Importstatus

### OK

- Datei wurde stabil gelesen.
- Kernspalten wurden erkannt.
- Analyse darf starten.

### WARNUNG

- Datei wurde gelesen.
- Einzelne optionale Spalten fehlen.
- Analyse darf starten, aber Datenlücken müssen markiert werden.

### FEHLER

- Datei konnte nicht stabil gelesen werden.
- Keine Analyse.
- Keine Scores.
- Keine Rankings.
- Keine Deep Dives.

## Grundsatz

Ein Parserfehler darf niemals zu erfundenen Investment-Ergebnissen führen.

Wenn der Import fehlschlägt, muss der Agent den Fehler erklären und stoppen.