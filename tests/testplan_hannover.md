# Testplan Hannover - Scoring-Vergleich Inseratsdauer

## Ziel

Prüfen, ob die Anpassung des Scorings bezüglich Inseratsdauer zu viele Objekte herausfiltert oder korrekt alte/problematische Inserate abwertet.

## Vergleich

- Baseline: Score ohne Liquiditäts-Malus
- Neue Version: Score mit Liquiditäts-Malus

## Zu prüfen

1. Welche Objekte wurden schlechter bewertet?
2. Welche Objekte sind unter eine Klassifikationsschwelle gefallen?
3. Welche Objekte wurden neu ausgeschlossen?
4. War der Ausschluss fachlich gerechtfertigt?
5. Gibt es mögliche False Negatives?
6. Ist Hannover aktuell tatsächlich unattraktiv oder der Filter zu streng?

## Audit-Tabelle

| ID | Score alt | Score neu | Differenz | Tage online | Klasse alt | Klasse neu | Ursache | Audit |
|---|---:|---:|---:|---:|---|---|---|---|

## Audit-Kategorien

- korrekt abgewertet
- berechtigt ausgeschlossen
- Grenzfall
- möglicher False Negative
- Datenmangel
- Markt aktuell schwach

## Ergebnisoptionen

- Scoring-Anpassung angemessen
- Scoring zu streng
- Markt aktuell unattraktiv
- weitere Kalibrierung nötig

## Entscheidungsfrage

Die zentrale Frage lautet:

Wurden interessante Objekte nur wegen langer Inseratsdauer zu stark abgestraft, oder bestätigt die neue Logik berechtigt, dass diese Objekte marktseitig schwach sind?