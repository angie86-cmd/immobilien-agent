# Agent Validation Summary

## Input files

- Source CSV: `C:\dev\immobilien-agent\tests\fixtures\raw\20260702_offers_Leipzig.csv`
- Agent output: `C:\dev\immobilien-agent\reports\20260702_offers_leipzig_agent_v3_6.csv`
- Liquidity audit: `C:\dev\immobilien-agent\reports\20260702_offers_Leipzig_liquidity_audit.csv`

## Result overview

| Validation result | Count |
| --- | --- |
| EXCLUSION_SUPPORTED_BY_STALE_HIGH_ROI_RISK | 9 |
| EXCLUSION_SUPPORTED_BY_STALE_LISTING_RISK | 70 |
| LIKELY_VALID_EXCLUSION | 202 |
| NEEDS_MANUAL_CONFIRMATION | 4 |
| OK | 48 |

## Potential False Negatives

_Keine Objekte._

## Exclusions supported by stale listing risk

| Ort | Adresse | Preis | ROI | Tage online | Score final | Agent decision | Audit category | Exclusion reason | Link |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Leipzig | Seehausener Allee 40, 04356 Leipzig | 96500 | 5 | 1511 | 25 | AUSSCHLIESSEN | Altinserat-Risiko: sehr lange online | Score final <55 nach Liquiditäts-Malus/Risiko | https://www.immometrica.com/de/offer/13315647 |
| Wiederitzsch | Martinshöhe 8A, 04158 Leipzig | 114500 | 5.5 | 1249 | 23 | AUSSCHLIESSEN | Altinserat-Risiko: sehr lange online | Score final <55 nach Liquiditäts-Malus/Risiko | https://www.immometrica.com/de/offer/15315328 |
| Paunsdorf | Hermelinplatz 10, 04329 Heiterblick, Leipzig | 140000 | 5.4 | 1064 | 25 | AUSSCHLIESSEN | Altinserat-Risiko: sehr lange online | Score final <55 nach Liquiditäts-Malus/Risiko | https://www.immometrica.com/de/offer/16798679 |
| Lindenau | Josephstr. 39, 04177 Leipzig | 110600 | 4.5 | 989 | 17 | AUSSCHLIESSEN | Altinserat-Risiko: sehr lange online | Score final <55 nach Liquiditäts-Malus/Risiko | https://www.immometrica.com/de/offer/17374691 |
| Großzschocher | Bismarckstr. 29, 04249 Leipzig | 130000 | 5.4 | 965 | 29 | AUSSCHLIESSEN | Altinserat-Risiko: sehr lange online | Score final <55 nach Liquiditäts-Malus/Risiko | https://www.immometrica.com/de/offer/17565630 |
| Engelsdorf | 04319 Leipzig (Engelsdorf) | 99500 | 4.4 | 1360 | 17 | AUSSCHLIESSEN | Altinserat-Risiko: sehr lange online | Score final <55 nach Liquiditäts-Malus/Risiko | https://www.immometrica.com/de/offer/17845425 |
| Eutritzsch | 04129 Leipzig - Eutritzsch 04129 Leipzig - Eutritzsch | 120000 | 4.7 | 924 | 30 | AUSSCHLIESSEN | Altinserat-Risiko: sehr lange online | Score final <55 nach Liquiditäts-Malus/Risiko | https://www.immometrica.com/de/offer/18122865 |
| Mockau-Nord | Mockauer Straße 55, 04357 Mockau-Süd, Leipzig | 140000 | 5.2 | 897 | 27 | AUSSCHLIESSEN | Altinserat-Risiko: sehr lange online | Score final <55 nach Liquiditäts-Malus/Risiko | https://www.immometrica.com/de/offer/18343393 |
| Burghausen-Rückmarsdorf | Lindenpark 1, 04178 Leipzig | 119500 | 4.2 | 867 | 19 | AUSSCHLIESSEN | Altinserat-Risiko: sehr lange online | Score final <55 nach Liquiditäts-Malus/Risiko | https://www.immometrica.com/de/offer/18659684 |
| Leipzig | Alte Gärtnerei 4, 04288 Leipzig | 135000 | 5.3 | 835 | 23 | AUSSCHLIESSEN | Altinserat-Risiko: sehr lange online | Score final <55 nach Liquiditäts-Malus/Risiko | https://www.immometrica.com/de/offer/18993542 |
| Leipzig | Slevogtstr. 18, 04159 Leipzig | 114000 | 4.9 | 799 | 27 | AUSSCHLIESSEN | Altinserat-Risiko: sehr lange online | Score final <55 nach Liquiditäts-Malus/Risiko | https://www.immometrica.com/de/offer/19347632 |
| Stötteritz | Schlesierstr. 43, 04299 Leipzig | 117000 | 4.4 | 785 | 20 | AUSSCHLIESSEN | Altinserat-Risiko: sehr lange online | Score final <55 nach Liquiditäts-Malus/Risiko | https://www.immometrica.com/de/offer/19490949 |
| Paunsdorf | Am Bauernteich 1, 04328 Paunsdorf, Leipzig | 150000 | 4.6 | 770 | 22 | AUSSCHLIESSEN | Altinserat-Risiko: sehr lange online | Score final <55 nach Liquiditäts-Malus/Risiko | https://www.immometrica.com/de/offer/19625220 |
| Leipzig | 04356 Leipzig - Seehausen 04356 Leipzig - Seehausen | 79000 | 5.7 | 716 | 21 | AUSSCHLIESSEN | Altinserat-Risiko: sehr lange online | Score final <55 nach Liquiditäts-Malus/Risiko | https://www.immometrica.com/de/offer/20173878 |
| Leipzig | 04356 Leipzig - Seehausen 04356 Leipzig - Seehausen | 126000 | 5.2 | 716 | 23 | AUSSCHLIESSEN | Altinserat-Risiko: sehr lange online | Score final <55 nach Liquiditäts-Malus/Risiko | https://www.immometrica.com/de/offer/20173879 |
| Leipzig | Außenring 34, 04158 Leipzig | 123000 | 5.7 | 639 | 29 | AUSSCHLIESSEN | Altinserat-Risiko: sehr lange online | Score final <55 nach Liquiditäts-Malus/Risiko | https://www.immometrica.com/de/offer/20932775 |
| Leipzig | Robinienweg 6, 04158 Leipzig | 131550 | 4.5 | 639 | 18 | AUSSCHLIESSEN | Altinserat-Risiko: sehr lange online | Score final <55 nach Liquiditäts-Malus/Risiko | https://www.immometrica.com/de/offer/20933890 |
| Leipzig | Außenring 32, 04158 Leipzig | 127000 | 5.3 | 630 | 31 | AUSSCHLIESSEN | Altinserat-Risiko: sehr lange online | Score final <55 nach Liquiditäts-Malus/Risiko | https://www.immometrica.com/de/offer/21019841 |
| Leipzig | Scheumannstr. 6, 04347 Leipzig | 148200 | 4.2 | 611 | 24 | AUSSCHLIESSEN | Altinserat-Risiko: sehr lange online | Score final <55 nach Liquiditäts-Malus/Risiko | https://www.immometrica.com/de/offer/21196112 |
| Böhlitz-Ehrenberg | Leipziger Str. 113, 04178 Leipzig (Böhlitz-Ehrenberg) | 122000 | 5.6 | 610 | 25 | AUSSCHLIESSEN | Altinserat-Risiko: sehr lange online | Score final <55 nach Liquiditäts-Malus/Risiko | https://www.immometrica.com/de/offer/21230610 |
| Leipzig | Maulwurfweg 3, 04329 Leipzig | 99000 | 5.7 | 598 | 27 | AUSSCHLIESSEN | Altinserat-Risiko: sehr lange online | Score final <55 nach Liquiditäts-Malus/Risiko | https://www.immometrica.com/de/offer/21353310 |
| Anger-Crottendorf | Herrnhuter Str. 7, 04318 Anger-Crottendorf, Leipzig | 119000 | 4.9 | 583 | 22 | AUSSCHLIESSEN | Altinserat-Risiko: sehr lange online | Score final <55 nach Liquiditäts-Malus/Risiko | https://www.immometrica.com/de/offer/21493807 |
| Leipzig | Melanchthonstraße 4, 04315 Neustadt-Neuschönefeld, Leipzig | 149000 | 4.1 | 568 | 25 | AUSSCHLIESSEN | Altinserat-Risiko: sehr lange online | Score final <55 nach Liquiditäts-Malus/Risiko | https://www.immometrica.com/de/offer/21636567 |
| Stötteritz | 04299 Leipzig (Stötteritz) | 139000 | 4.7 | 568 | 22 | AUSSCHLIESSEN | Altinserat-Risiko: sehr lange online | Score final <55 nach Liquiditäts-Malus/Risiko | https://www.immometrica.com/de/offer/21638729 |
| Leipzig | Püchauer Str. 5, 04318 Leipzig | 136000 | 4.5 | 538 | 18 | AUSSCHLIESSEN | Altinserat-Risiko: sehr lange online | Score final <55 nach Liquiditäts-Malus/Risiko | https://www.immometrica.com/de/offer/21876611 |
| Heiterblick | 04329 Leipzig - Paunsdorf 04329 Leipzig - Paunsdorf | 99000 | 4.7 | 534 | 20 | AUSSCHLIESSEN | Altinserat-Risiko: sehr lange online | Score final <55 nach Liquiditäts-Malus/Risiko | https://www.immometrica.com/de/offer/21917485 |
| Anger-Crottendorf | 04318 Leipzig - Sellerhausen-Stünz 04318 Leipzig - Sellerhausen-Stünz | 125000 | 4.6 | 497 | 20 | AUSSCHLIESSEN | Altinserat-Risiko: sehr lange online | Score final <55 nach Liquiditäts-Malus/Risiko | https://www.immometrica.com/de/offer/22353449 |
| Großzschocher | Buttergasse 10a, 04249 Großzschocher, Leipzig | 135000 | 5.7 | 489 | 33 | AUSSCHLIESSEN | Altinserat-Risiko: sehr lange online | Score final <55 nach Liquiditäts-Malus/Risiko | https://www.immometrica.com/de/offer/22432315 |
| Paunsdorf | 04328 Paunsdorf, Leipzig | 146000 | 4 | 486 | 16 | AUSSCHLIESSEN | Altinserat-Risiko: sehr lange online | Score final <55 nach Liquiditäts-Malus/Risiko | https://www.immometrica.com/de/offer/22457594 |
| Großzschocher | Buttergasse 10a, 04249 Großzschocher, Leipzig | 95000 | 5.3 | 471 | 29 | AUSSCHLIESSEN | Altinserat-Risiko: sehr lange online | Score final <55 nach Liquiditäts-Malus/Risiko | https://www.immometrica.com/de/offer/22621360 |
| Volkmarsdorf | Kapellenstraße 18, 04315 Neustadt-Neuschönefeld, Leipzig | 138000 | 4.2 | 463 | 15 | AUSSCHLIESSEN | Altinserat-Risiko: sehr lange online | Score final <55 nach Liquiditäts-Malus/Risiko | https://www.immometrica.com/de/offer/22706475 |
| Möckern | Toskastr. 10 d, 04159 Leipzig (Möckern) | 94500 | 5.3 | 461 | 31 | AUSSCHLIESSEN | Altinserat-Risiko: sehr lange online | Score final <55 nach Liquiditäts-Malus/Risiko | https://www.immometrica.com/de/offer/22736222 |
| Leipzig | Bischofstr. 25, 04179 Leipzig | 65000 | 6.4 | 454 | 28 | NUR MIT RÜCKFRAGEN | Altinserat-Renditefalle: hohe ROI, aber sehr lange online | Altinserat-Renditefalle / stark prüfen | https://www.immometrica.com/de/offer/22834954 |
| Lausen-Grünau | An der Kotsche 27, 04207 Lausen-Grünau, Leipzig | 115000 | 4.2 | 451 | 27 | AUSSCHLIESSEN | Altinserat-Risiko: sehr lange online | Score final <55 nach Liquiditäts-Malus/Risiko | https://www.immometrica.com/de/offer/22862595 |
| Lausen-Grünau | An der Kotsche 25, 04207 Lausen-Grünau, Leipzig | 120000 | 4 | 451 | 26 | AUSSCHLIESSEN | Altinserat-Risiko: sehr lange online | Score final <55 nach Liquiditäts-Malus/Risiko | https://www.immometrica.com/de/offer/22862971 |
| Wahren | Toskastr. 10 d, 04159 Möckern, Leipzig | 94500 | 5.7 | 422 | 31 | AUSSCHLIESSEN | Altinserat-Risiko: sehr lange online | Score final <55 nach Liquiditäts-Malus/Risiko | https://www.immometrica.com/de/offer/23142126 |
| Thekla | Tauchaer Straße 79, 04349 Thekla, Leipzig | 150000 | 4.7 | 374 | 23 | AUSSCHLIESSEN | Altinserat-Risiko: sehr lange online | Score final <55 nach Liquiditäts-Malus/Risiko | https://www.immometrica.com/de/offer/23627173 |
| Neulindenau | Gröpplerstraße 100 B, 04179 Neulindenau, Leipzig | 143000 | 4.8 | 371 | 20 | AUSSCHLIESSEN | Altinserat-Risiko: sehr lange online | Score final <55 nach Liquiditäts-Malus/Risiko | https://www.immometrica.com/de/offer/23662818 |
| Leipzig | Georg-Schwarz-Str. 60, 04177 Leipzig | 129000 | 4.8 | 365 | 16 | AUSSCHLIESSEN | Altinserat-Risiko: sehr lange online | Score final <55 nach Liquiditäts-Malus/Risiko | https://www.immometrica.com/de/offer/23721913 |
| Wiederitzsch | 04158 Wiederitzsch, Leipzig | 127000 | 5.4 | 356 | 31 | AUSSCHLIESSEN | Altinserat-Risiko: sehr lange online | Score final <55 nach Liquiditäts-Malus/Risiko | https://www.immometrica.com/de/offer/23814618 |
| Mölkau | 04316 Leipzig (Mölkau) | 68000 | 6.1 | 344 | 16 | AUSSCHLIESSEN | Altinserat-Renditefalle: hohe ROI, aber sehr lange online | Wohnfläche < 30 m² | https://www.immometrica.com/de/offer/23928970 |
| Böhlitz-Ehrenberg | Heinrich-Heine-Str. 76, 04178 Leipzig Böhlitz-Ehrenberg | 66000 | 6.6 | 344 | 26 | NUR MIT RÜCKFRAGEN | Altinserat-Renditefalle: hohe ROI, aber sehr lange online | Altinserat-Renditefalle / stark prüfen | https://www.immometrica.com/de/offer/23934267 |
| Leipzig | Hermelinstr. 4, 04329 Leipzig | 149750 | 4.8 | 338 | 30 | AUSSCHLIESSEN | Altinserat-Risiko: sehr lange online | Score final <55 nach Liquiditäts-Malus/Risiko | https://www.immometrica.com/de/offer/24001439 |
| Leipzig | Hauptstr. 48C, 04288 Leipzig | 120000 | 6 | 335 | 39 | NUR MIT RÜCKFRAGEN | Altinserat-Renditefalle: hohe ROI, aber sehr lange online | Altinserat-Renditefalle / stark prüfen | https://www.immometrica.com/de/offer/24032094 |
| Leipzig | Engelsdorfer Str. 140, 04316 Leipzig | 138000 | 5 | 324 | 22 | AUSSCHLIESSEN | Altinserat-Risiko: sehr lange online | Score final <55 nach Liquiditäts-Malus/Risiko | https://www.immometrica.com/de/offer/24140917 |
| Knautkleeberg-Knauthain | 04249 Leipzig | 130000 | 6 | 317 | 29 | NUR MIT RÜCKFRAGEN | Altinserat-Renditefalle: hohe ROI, aber sehr lange online | Altinserat-Renditefalle / stark prüfen | https://www.immometrica.com/de/offer/24200892 |
| Leipzig | Christoph-Probst-Str. 5, 04159 Leipzig | 137000 | 5 | 314 | 29 | AUSSCHLIESSEN | Altinserat-Risiko: sehr lange online | Score final <55 nach Liquiditäts-Malus/Risiko | https://www.immometrica.com/de/offer/24243603 |
| Zentrum-Nordwest | Friedrich-Ebert-Str., 04105 Leipzig (Zentrum-Nordwest) | 130000 | 4.4 | 313 | 14 | AUSSCHLIESSEN | Altinserat-Risiko: sehr lange online | Score final <55 nach Liquiditäts-Malus/Risiko | https://www.immometrica.com/de/offer/24249920 |
| Gohlis-Mitte | 04157 Leipzig - Gohlis-Mitte 04157 Leipzig - Gohlis-Mitte | 80000 | 6 | 311 | 26 | NUR MIT RÜCKFRAGEN | Altinserat-Renditefalle: hohe ROI, aber sehr lange online | Altinserat-Renditefalle / stark prüfen | https://www.immometrica.com/de/offer/24266189 |
| Böhlitz-Ehrenberg | Pestalozzistr. 70, 04178 Leipzig (Böhlitz-Ehrenberg) | 95000 | 5.5 | 310 | 23 | AUSSCHLIESSEN | Altinserat-Risiko: sehr lange online | Score final <55 nach Liquiditäts-Malus/Risiko | https://www.immometrica.com/de/offer/24273512 |
| Leipzig | Eschenweg 2, 04178 Leipzig | 75000 | 5.3 | 310 | 32 | AUSSCHLIESSEN | Altinserat-Risiko: sehr lange online | Score final <55 nach Liquiditäts-Malus/Risiko | https://www.immometrica.com/de/offer/24276302 |
| Paunsdorf | Am Bauernteich 1, 04328 Paunsdorf, Leipzig | 145000 | 4.5 | 310 | 23 | AUSSCHLIESSEN | Altinserat-Risiko: sehr lange online | Score final <55 nach Liquiditäts-Malus/Risiko | https://www.immometrica.com/de/offer/24280087 |
| Knautkleeberg-Knauthain | Giordano-Bruno-Str. 28, 04249 Leipzig | 130000 | 5.9 | 299 | 37 | AUSSCHLIESSEN | Altinserat-Risiko: sehr lange online | Score final <55 nach Liquiditäts-Malus/Risiko | https://www.immometrica.com/de/offer/24395570 |
| Burghausen-Rückmarsdorf | 04178 Leipzig - Burghausen-Rückmarsdorf 04178 Leipzig - Burghausen-Rückmarsdorf | 120000 | 4.2 | 297 | 13 | AUSSCHLIESSEN | Altinserat-Risiko: sehr lange online | Score final <55 nach Liquiditäts-Malus/Risiko | https://www.immometrica.com/de/offer/24411610 |
| Eutritzsch | Bonhoefferstraße 6, 04129 Eutritzsch, Leipzig | 150000 | 4.4 | 293 | 17 | AUSSCHLIESSEN | Altinserat-Risiko: sehr lange online | Score final <55 nach Liquiditäts-Malus/Risiko | https://www.immometrica.com/de/offer/24460593 |
| Seehausen | 04356 Seehausen, Leipzig | 126000 | 5 | 290 | 21 | AUSSCHLIESSEN | Altinserat-Risiko: sehr lange online | Score final <55 nach Liquiditäts-Malus/Risiko | https://www.immometrica.com/de/offer/24486978 |
| Stötteritz | 04299 Leipzig (Stötteritz) | 135000 | 4.6 | 284 | 22 | AUSSCHLIESSEN | Altinserat-Risiko: sehr lange online | Score final <55 nach Liquiditäts-Malus/Risiko | https://www.immometrica.com/de/offer/24546607 |
| Grünau-Nord | Am kleinen Feld 30, 04205 Leipzig | 99000 | 6.2 | 283 | 19 | NUR MIT RÜCKFRAGEN | Altinserat-Renditefalle: hohe ROI, aber sehr lange online | Altinserat-Renditefalle / stark prüfen | https://www.immometrica.com/de/offer/24562963 |
| Leipzig | Klasingstr. 44B, 04315 Leipzig | 130000 | 4.4 | 282 | 13 | AUSSCHLIESSEN | Altinserat-Risiko: sehr lange online | Score final <55 nach Liquiditäts-Malus/Risiko | https://www.immometrica.com/de/offer/24575903 |
| Böhlitz-Ehrenberg | Leipziger Str. 115, 04178 Leipzig (Böhlitz-Ehrenberg) | 134000 | 5.4 | 269 | 23 | AUSSCHLIESSEN | Altinserat-Risiko: sehr lange online | Score final <55 nach Liquiditäts-Malus/Risiko | https://www.immometrica.com/de/offer/24703587 |
| Leipzig | Ernst-Guhr-Str. 7, 04319 Leipzig | 148000 | 4.2 | 247 | 11 | AUSSCHLIESSEN | Altinserat-Risiko: sehr lange online | Score final <55 nach Liquiditäts-Malus/Risiko | https://www.immometrica.com/de/offer/24943988 |
| Leipzig | Laubestr. 1, 04159 Leipzig | 90000 | 5.5 | 247 | 27 | AUSSCHLIESSEN | Altinserat-Risiko: sehr lange online | Score final <55 nach Liquiditäts-Malus/Risiko | https://www.immometrica.com/de/offer/24945214 |
| Möckern | Faradaystr. 9, 04159 Leipzig (Möckern) | 145000 | 4.1 | 240 | 13 | AUSSCHLIESSEN | Altinserat-Risiko: sehr lange online | Score final <55 nach Liquiditäts-Malus/Risiko | https://www.immometrica.com/de/offer/25022284 |
| Leipzig | Ernst-Guhr-Str. 7, 04319 Leipzig | 149900 | 4.5 | 239 | 17 | AUSSCHLIESSEN | Altinserat-Risiko: sehr lange online | Score final <55 nach Liquiditäts-Malus/Risiko | https://www.immometrica.com/de/offer/25035907 |
| Leipzig | Walter-Markov-Ring 4, 04288 Leipzig | 138000 | 4.4 | 226 | 21 | AUSSCHLIESSEN | Altinserat-Risiko: sehr lange online | Score final <55 nach Liquiditäts-Malus/Risiko | https://www.immometrica.com/de/offer/25183208 |
| Leipzig | Georg-Schwarz-Str. 89, 04179 Leipzig | 89000 | 5.9 | 223 | 33 | AUSSCHLIESSEN | Altinserat-Risiko: sehr lange online | Score final <55 nach Liquiditäts-Malus/Risiko | https://www.immometrica.com/de/offer/25392872 |
| Heiterblick | Maulwurfweg 5, 04329 Heiterblick, Leipzig | 110000 | 5.3 | 219 | 19 | AUSSCHLIESSEN | Altinserat-Risiko: sehr lange online | Score final <55 nach Liquiditäts-Malus/Risiko | https://www.immometrica.com/de/offer/25422884 |
| Anger-Crottendorf | 04318 Leipzig (Anger-Crottendorf) | 140250 | 4.3 | 217 | 14 | AUSSCHLIESSEN | Altinserat-Risiko: sehr lange online | Score final <55 nach Liquiditäts-Malus/Risiko | https://www.immometrica.com/de/offer/25444671 |
| Plagwitz | Einsteinstr. 5, 04229 Plagwitz, Leipzig | 125000 | 5.1 | 212 | 29 | AUSSCHLIESSEN | Altinserat-Risiko: sehr lange online | Score final <55 nach Liquiditäts-Malus/Risiko | https://www.immometrica.com/de/offer/25488927 |
| Zentrum-Ost | 04317 Leipzig (Reudnitz-Thonberg) | 140000 | 4.7 | 211 | 29 | AUSSCHLIESSEN | Altinserat-Risiko: sehr lange online | Score final <55 nach Liquiditäts-Malus/Risiko | https://www.immometrica.com/de/offer/25506330 |
| Leipzig | Felsenbirnenstr. 10, 04329 Leipzig | 149000 | 4.2 | 211 | 22 | AUSSCHLIESSEN | Altinserat-Risiko: sehr lange online | Score final <55 nach Liquiditäts-Malus/Risiko | https://www.immometrica.com/de/offer/25510378 |
| Gohlis-Süd | Georg-Schumann-Str. 131, 04155 Leipzig | 84150 | 6.1 | 210 | 31 | NUR MIT RÜCKFRAGEN | Altinserat-Renditefalle: hohe ROI, aber sehr lange online | Altinserat-Renditefalle / stark prüfen | https://www.immometrica.com/de/offer/25524288 |
| Gohlis-Süd | Georg-Schumann-Str. 131, 04155 Leipzig | 74700 | 6.1 | 210 | 29 | NUR MIT RÜCKFRAGEN | Altinserat-Renditefalle: hohe ROI, aber sehr lange online | Altinserat-Renditefalle / stark prüfen | https://www.immometrica.com/de/offer/25524300 |
| Leipzig | Wilhelm-Plesse-Str. 28, 04157 Leipzig | 120000 | 5.8 | 209 | 27 | AUSSCHLIESSEN | Altinserat-Risiko: sehr lange online | Score final <55 nach Liquiditäts-Malus/Risiko | https://www.immometrica.com/de/offer/25529853 |
| Wahren | Paul-Ernst-Straße 23, 04159 Leipzig (Wahren) | 129000 | 4.4 | 205 | 12 | AUSSCHLIESSEN | Altinserat-Risiko: sehr lange online | Score final <55 nach Liquiditäts-Malus/Risiko | https://www.immometrica.com/de/offer/25565140 |
| Seehausen | Seehausener Str. 34, 04356 Seehausen, Leipzig | 80000 | 5.1 | 199 | 5 | AUSSCHLIESSEN | Altinserat-Risiko: sehr lange online | Wohnfläche < 30 m² | https://www.immometrica.com/de/offer/25615123 |
| Altlindenau | 04177 Altlindenau, Leipzig | 148000 | 4.7 | 196 | 30 | AUSSCHLIESSEN | Altinserat-Risiko: sehr lange online | Score final <55 nach Liquiditäts-Malus/Risiko | https://www.immometrica.com/de/offer/25648502 |
| Leipzig | Uhlandstr. 15, 04177 Leipzig | 119000 | 4.8 | 195 | 18 | AUSSCHLIESSEN | Altinserat-Risiko: sehr lange online | Score final <55 nach Liquiditäts-Malus/Risiko | https://www.immometrica.com/de/offer/25656906 |
| Wahren | 04159 Leipzig / Wahren (Wahren) | 135000 | 4.9 | 181 | 34 | AUSSCHLIESSEN | Altinserat-Risiko: sehr lange online | Score final <55 nach Liquiditäts-Malus/Risiko | https://www.immometrica.com/de/offer/25730666 |

## Stale high-ROI traps

| Ort | Adresse | Preis | ROI | Tage online | Score final | Agent decision | Audit category | Exclusion reason | Link |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Leipzig | Bischofstr. 25, 04179 Leipzig | 65000 | 6.4 | 454 | 28 | NUR MIT RÜCKFRAGEN | Altinserat-Renditefalle: hohe ROI, aber sehr lange online | Altinserat-Renditefalle / stark prüfen | https://www.immometrica.com/de/offer/22834954 |
| Mölkau | 04316 Leipzig (Mölkau) | 68000 | 6.1 | 344 | 16 | AUSSCHLIESSEN | Altinserat-Renditefalle: hohe ROI, aber sehr lange online | Wohnfläche < 30 m² | https://www.immometrica.com/de/offer/23928970 |
| Böhlitz-Ehrenberg | Heinrich-Heine-Str. 76, 04178 Leipzig Böhlitz-Ehrenberg | 66000 | 6.6 | 344 | 26 | NUR MIT RÜCKFRAGEN | Altinserat-Renditefalle: hohe ROI, aber sehr lange online | Altinserat-Renditefalle / stark prüfen | https://www.immometrica.com/de/offer/23934267 |
| Leipzig | Hauptstr. 48C, 04288 Leipzig | 120000 | 6 | 335 | 39 | NUR MIT RÜCKFRAGEN | Altinserat-Renditefalle: hohe ROI, aber sehr lange online | Altinserat-Renditefalle / stark prüfen | https://www.immometrica.com/de/offer/24032094 |
| Knautkleeberg-Knauthain | 04249 Leipzig | 130000 | 6 | 317 | 29 | NUR MIT RÜCKFRAGEN | Altinserat-Renditefalle: hohe ROI, aber sehr lange online | Altinserat-Renditefalle / stark prüfen | https://www.immometrica.com/de/offer/24200892 |
| Gohlis-Mitte | 04157 Leipzig - Gohlis-Mitte 04157 Leipzig - Gohlis-Mitte | 80000 | 6 | 311 | 26 | NUR MIT RÜCKFRAGEN | Altinserat-Renditefalle: hohe ROI, aber sehr lange online | Altinserat-Renditefalle / stark prüfen | https://www.immometrica.com/de/offer/24266189 |
| Grünau-Nord | Am kleinen Feld 30, 04205 Leipzig | 99000 | 6.2 | 283 | 19 | NUR MIT RÜCKFRAGEN | Altinserat-Renditefalle: hohe ROI, aber sehr lange online | Altinserat-Renditefalle / stark prüfen | https://www.immometrica.com/de/offer/24562963 |
| Gohlis-Süd | Georg-Schumann-Str. 131, 04155 Leipzig | 84150 | 6.1 | 210 | 31 | NUR MIT RÜCKFRAGEN | Altinserat-Renditefalle: hohe ROI, aber sehr lange online | Altinserat-Renditefalle / stark prüfen | https://www.immometrica.com/de/offer/25524288 |
| Gohlis-Süd | Georg-Schumann-Str. 131, 04155 Leipzig | 74700 | 6.1 | 210 | 29 | NUR MIT RÜCKFRAGEN | Altinserat-Renditefalle: hohe ROI, aber sehr lange online | Altinserat-Renditefalle / stark prüfen | https://www.immometrica.com/de/offer/25524300 |

## Needs Due Diligence

| Ort | Adresse | Preis | ROI | Tage online | Score final | Agent decision | Audit category | Exclusion reason | Link |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Böhlitz-Ehrenberg | Pestalozzistr. 70, 04178 Leipzig (Böhlitz-Ehrenberg) | 103000 | 6 | 139 | 48 | AUSSCHLIESSEN | Stale Listing Due Diligence: alt, aber eventuell prüfbar | Score final <55 nach Liquiditäts-Malus/Risiko | https://www.immometrica.com/de/offer/26215138 |
| Knautkleeberg-Knauthain | 04249 Leipzig - Knautkleeberg-Knauthain 04249 Leipzig - Knautkleeberg-Knauthain | 130000 | 6.3 | 86 | 44 | AUSSCHLIESSEN | Stale Listing Due Diligence: alt, aber eventuell prüfbar | Score final <55 nach Liquiditäts-Malus/Risiko | https://www.immometrica.com/de/offer/26831639 |
| Wiederitzsch | Zur Loberaue 15, 04356 Leipzig | 120000 | 6.3 | 64 | 45 | AUSSCHLIESSEN | Stale Listing Due Diligence: alt, aber eventuell prüfbar | Score final <55 nach Liquiditäts-Malus/Risiko | https://www.immometrica.com/de/offer/27096370 |
| Stötteritz | 04299 Leipzig - Stötteritz 04299 Leipzig - Stötteritz | 115000 | 6.4 | 64 | 51 | AUSSCHLIESSEN | Stale Listing Due Diligence: alt, aber eventuell prüfbar | Score final <55 nach Liquiditäts-Malus/Risiko | https://www.immometrica.com/de/offer/27102179 |

## Interpretation

- **POTENTIAL_FALSE_NEGATIVE**: Der Agent könnte zu aggressiv gefiltert haben.
- **EXCLUSION_SUPPORTED_BY_STALE_HIGH_ROI_RISK**: Der Ausschluss ist wahrscheinlich nachvollziehbar, weil alte Angebote mit hoher ROI oft ernste verdeckte Risiken haben.
- **EXCLUSION_SUPPORTED_BY_STALE_LISTING_RISK**: Der Ausschluss wird durch das Altinserat-Risiko gestützt.
- **NEEDS_DUE_DILIGENCE_STALE_LISTING**: Das Objekt ist nicht automatisch ausgeschlossen, seine lange Inseratsdauer verlangt aber starke Vorsicht.
- **NEEDS_DUE_DILIGENCE / NEEDS_MANUAL_CONFIRMATION**: Risiko oder Ausschlussgrund muss manuell bestätigt werden.
- **LIKELY_VALID_EXCLUSION**: Der Ausschluss ist wahrscheinlich mit dem Liquiditäts-Audit konsistent.
- **OK**: Es besteht kein Konflikt zwischen Agentenentscheidung und Audit.

`manual_review_required` ist ein Prüfhinweis, keine Aussage, dass der Agent falsch lag.
