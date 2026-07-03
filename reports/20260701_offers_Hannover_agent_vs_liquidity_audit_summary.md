# Agent Validation Summary

## Input files

- Source CSV: `C:\dev\immobilien-agent\tests\fixtures\raw\20260701_offers_Hannover.csv`
- Agent output: `C:\dev\immobilien-agent\reports\20260701_offers_Hannover_agent_v3_5.csv`
- Liquidity audit: `C:\dev\immobilien-agent\reports\20260701_offers_Hannover_liquidity_audit.csv`

## Result overview

| Validation result | Count |
| --- | --- |
| LIKELY_VALID_EXCLUSION | 76 |
| OK | 3 |
| POTENTIAL_FALSE_NEGATIVE | 47 |

## Potential False Negatives

| Ort | Adresse | Preis | ROI | Tage online | Score final | Agent decision | Audit category | Exclusion reason | Link |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| List | Hinrichsring 12, 30177 Hannover | 99000 | 8.5 | 1098 | 34 | Ausschließen | möglicher False Negative: gute ROI, aber stark altes Inserat | ⚠️ CLUSTER gleiche Straße + PLZ | https://www.immometrica.com/de/offer/16526363 |
| Alt-Laatzen | Flemingstraße, 30880 Laatzen (Laatzen-Mitte) | 105000 | 6.9 | 943 | 27 | Ausschließen | möglicher False Negative: gute ROI, aber stark altes Inserat | Stadt/Ort nicht in Whitelist: Laatzen; ⚠️ CLUSTER gleiche Straße + PLZ | https://www.immometrica.com/de/offer/17902470 |
| Barsinghausen | Allerweg 1, 30890 Barsinghausen | 98000 | 6.7 | 625 | 29 | Ausschließen | möglicher False Negative: gute ROI, aber stark altes Inserat | Stadt/Ort nicht in Whitelist: Barsinghausen; Hausgeld fehlt | https://www.immometrica.com/de/offer/21068810 |
| Linden-Mitte | Am Ihmeufer 3, 30449 Hannover | 75000 | 12.2 | 453 | 7 | Ausschließen | möglicher False Negative: gute ROI, aber stark altes Inserat | IHME-ZENTRUM-FALLE / Ihme-Risiko | https://www.immometrica.com/de/offer/22840770 |
| Burgwedel | Pappelweg 7b, 30938, Burgwedel | 89000 | 5.4 | 415 | 3 | Ausschließen | Grenzfall: attraktive ROI, aber sehr lange online | Stadt/Ort nicht in Whitelist: Burgwedel | https://www.immometrica.com/de/offer/23204182 |
| Badenstedt | Ziesenißstr. 22, 30455 Badenstedt, Hannover | 137900 | 5.0 | 412 | 18 | Ausschließen | Grenzfall: attraktive ROI, aber sehr lange online |  | https://www.immometrica.com/de/offer/23246720 |
| Hannover | Ihmeplatz 6, 30449 Hannover | 57000 | 13.9 | 406 | 16 | Ausschließen | möglicher False Negative: gute ROI, aber stark altes Inserat | IHME-ZENTRUM-FALLE / Ihme-Risiko; ⚠️ CLUSTER gleiche Straße + PLZ | https://www.immometrica.com/de/offer/23307683 |
| Springe | Steinberg 57, 31832 Springe | 99000 | 5.7 | 401 | 31 | Ausschließen | Grenzfall: attraktive ROI, aber sehr lange online | Stadt/Ort nicht in Whitelist: Springe; ⚠️ CLUSTER gleiche Straße + PLZ | https://www.immometrica.com/de/offer/23358818 |
| Hannover | Ihmeplatz 1, 30449 Linden-Mitte, Hannover | 80000 | 6.4 | 390 | 0 | Ausschließen | möglicher False Negative: gute ROI, aber stark altes Inserat | IHME-ZENTRUM-FALLE / Ihme-Risiko; SANIERUNGSSTAU / renovierungsbedürftig; ⚠️ CLUSTER gleiche Straße + PLZ | https://www.immometrica.com/de/offer/23481254 |
| Mittelfeld | Washingtonweg 1A, 30519 Mittelfeld, Hannover | 75000 | 6.6 | 379 | 25 | Ausschließen | möglicher False Negative: gute ROI, aber stark altes Inserat | Wohnfläche < 30 m²; Hausgeld fehlt; ⚠️ CLUSTER gleiche Straße + PLZ | https://www.immometrica.com/de/offer/23582066 |
| Hannover | Washingtonweg 1A, 30519 Mittelfeld, Hannover | 95000 | 5.8 | 378 | 27 | Ausschließen | Grenzfall: attraktive ROI, aber sehr lange online | Hausgeld fehlt; ⚠️ CLUSTER gleiche Straße + PLZ | https://www.immometrica.com/de/offer/23582360 |
| Alt-Laatzen | Flemingstr. 2, 30880 Laatzen | 125000 | 6.5 | 356 | 17 | Ausschließen | möglicher False Negative: gute ROI, aber stark altes Inserat | Stadt/Ort nicht in Whitelist: Laatzen | https://www.immometrica.com/de/offer/23814589 |
| Davenstedt | Wegsfeld 42, 30455 Hannover (Davenstedt) | 110000 | 6.4 | 350 | 0 | Ausschließen | möglicher False Negative: gute ROI, aber stark altes Inserat | SANIERUNGSSTAU / renovierungsbedürftig; ⚠️ CLUSTER gleiche Straße + PLZ | https://www.immometrica.com/de/offer/23865621 |
| Wettbergen | Berliner Str. 17, 30457 Hannover | 139000 | 5.7 | 290 | 28 | Ausschließen | Grenzfall: attraktive ROI, aber sehr lange online |  | https://www.immometrica.com/de/offer/24486651 |
| Empelde | Breite Str. 17 C, 30952 Ronnenberg (Empelde) | 115000 | 5.2 | 283 | 13 | Ausschließen | Grenzfall: attraktive ROI, aber sehr lange online | Stadt/Ort nicht in Whitelist: Ronnenberg; ⚠️ CLUSTER gleiche Straße + PLZ | https://www.immometrica.com/de/offer/24550381 |
| Vahrenwald | 30165 Hannover - Vahrenwald-List 30165 Hannover - Vahrenwald-List | 119000 | 5.9 | 272 | 16 | Ausschließen | Grenzfall: attraktive ROI, aber sehr lange online |  | https://www.immometrica.com/de/offer/24681000 |
| Alt-Langenhagen | Kurt-Schumacher-Allee 45, 30851 Langenhagen | 145000 | 5.4 | 268 | 6 | Ausschließen | Grenzfall: attraktive ROI, aber sehr lange online | Stadt/Ort nicht in Whitelist: Langenhagen | https://www.immometrica.com/de/offer/24711918 |
| Hannover | In der Steinbreite 89, 30455 Hannover | 145000 | 5.2 | 245 | 20 | Ausschließen | Grenzfall: attraktive ROI, aber sehr lange online | Hausgeld fehlt | https://www.immometrica.com/de/offer/24968487 |
| Hannover | Lauckerthof 7, 30419 Hannover | 114000 | 5.9 | 239 | 14 | Ausschließen | Grenzfall: attraktive ROI, aber sehr lange online | ⚠️ CLUSTER gleiche Straße + PLZ; ⚠️ DUBLETTE nahezu gleiche Daten | https://www.immometrica.com/de/offer/25037940 |
| Ahlem | Am Dornbusch 1, 30453 Ahlem, Hannover | 99000 | 5.2 | 232 | 11 | Ausschließen | Grenzfall: attraktive ROI, aber sehr lange online | Wohnfläche < 30 m² | https://www.immometrica.com/de/offer/25117890 |
| Alt-Laatzen | 30880 Niedersachsen - Laatzen 30880 Niedersachsen - Laatzen | 99000 | 5.3 | 230 | 20 | Ausschließen | Grenzfall: attraktive ROI, aber sehr lange online | Stadt/Ort nicht in Whitelist: Laatzen | https://www.immometrica.com/de/offer/25137728 |
| Burgdorf | Liebermannstr. 13, 31303 Burgdorf | 119000 | 5.3 | 224 | 16 | Ausschließen | Grenzfall: attraktive ROI, aber sehr lange online | Stadt/Ort nicht in Whitelist: Burgdorf | https://www.immometrica.com/de/offer/25205348 |
| Hannover | Washingtonweg 1A, 30519 Hannover | 70000 | 6.9 | 223 | 0 | Ausschließen | möglicher False Negative: gute ROI, aber stark altes Inserat | SANIERUNGSSTAU / renovierungsbedürftig; ⚠️ CLUSTER gleiche Straße + PLZ | https://www.immometrica.com/de/offer/25392464 |
| Sahlkamp | 30179 Hannover (Sahlkamp) | 130000 | 5.6 | 199 | 21 | Ausschließen | Grenzfall: attraktive ROI, aber sehr lange online |  | https://www.immometrica.com/de/offer/25610093 |
| Garbsen-Mitte | 30823 Garbsen / Havelse (Havelse) | 125000 | 5.0 | 186 | 10 | Ausschließen | Grenzfall: attraktive ROI, aber sehr lange online | Stadt/Ort nicht in Whitelist: Garbsen; Hausgeld fehlt | https://www.immometrica.com/de/offer/25698195 |
| Laatzen-Mitte | Flemingstraße 2, 30880, Laatzen | 115000 | 6.4 | 166 | 30 | Ausschließen | möglicher False Negative: gute ROI, aber stark altes Inserat | Stadt/Ort nicht in Whitelist: Laatzen; ⚠️ CLUSTER gleiche Straße + PLZ | https://www.immometrica.com/de/offer/25883174 |
| Alt-Laatzen | Otto-Hahn-Str. 13, 30880 Laatzen (Laatzen-Mitte) | 84900 | 6.1 | 150 | 32 | Ausschließen | möglicher False Negative: gute ROI, aber stark altes Inserat | Stadt/Ort nicht in Whitelist: Laatzen; ⚠️ CLUSTER gleiche Straße + PLZ | https://www.immometrica.com/de/offer/26062724 |
| Hannover | Hinrichsring 15A, 30177 Hannover | 125000 | 6.7 | 138 | 42 | Ausschließen | möglicher False Negative: gute ROI, aber stark altes Inserat | ⚠️ CLUSTER gleiche Straße + PLZ | https://www.immometrica.com/de/offer/26210423 |
| Bemerode | Bindingweg 1, 30559 Bemerode, Hannover | 134000 | 6.9 | 134 | 37 | Ausschließen | möglicher False Negative: gute ROI, aber stark altes Inserat |  | https://www.immometrica.com/de/offer/26248930 |
| Hannover | Vahrenheider Markt 8, 30179 Hannover | 89000 | 6.4 | 133 | 0 | Ausschließen | möglicher False Negative: gute ROI, aber stark altes Inserat | SANIERUNGSSTAU / renovierungsbedürftig | https://www.immometrica.com/de/offer/26279319 |
| List | Hinrichsring 12, 30177 Hannover | 110000 | 6.9 | 125 | 37 | Ausschließen | möglicher False Negative: gute ROI, aber stark altes Inserat | ⚠️ CLUSTER gleiche Straße + PLZ | https://www.immometrica.com/de/offer/26355234 |
| Alt-Laatzen | Otto-Hahn-Str. 15, 30880 Laatzen | 98500 | 6.0 | 121 | 0 | Ausschließen | möglicher False Negative: gute ROI, aber stark altes Inserat | Stadt/Ort nicht in Whitelist: Laatzen; SANIERUNGSSTAU / renovierungsbedürftig; ⚠️ CLUSTER gleiche Straße + PLZ | https://www.immometrica.com/de/offer/26403777 |
| Hannover | Plauener Str. 25, 30179 Hannover | 85000 | 6.1 | 111 | 46 | Ausschließen | möglicher False Negative: gute ROI, aber stark altes Inserat | Hausgeld fehlt; ⚠️ CLUSTER gleiche Straße + PLZ | https://www.immometrica.com/de/offer/26551035 |
| Linden-Nord | Stärkestr. 16, 30451 Hannover | 125000 | 6.7 | 110 | 51 | Ausschließen | möglicher False Negative: gute ROI, aber stark altes Inserat | Hausgeld fehlt | https://www.immometrica.com/de/offer/26567000 |
| Alt-Langenhagen | Im Hohen Felde 15, 30853 Langenhagen | 119000 | 6.1 | 104 | 33 | Ausschließen | möglicher False Negative: gute ROI, aber stark altes Inserat | Stadt/Ort nicht in Whitelist: Langenhagen | https://www.immometrica.com/de/offer/26625176 |
| Springe | Steinberg 57, 31832 Springe | 80000 | 7.4 | 99 | 1 | Ausschließen | möglicher False Negative: gute ROI, aber stark altes Inserat | Stadt/Ort nicht in Whitelist: Springe; SANIERUNGSSTAU / renovierungsbedürftig; ⚠️ CLUSTER gleiche Straße + PLZ | https://www.immometrica.com/de/offer/26676332 |
| Linden-Süd | 30449 Linden-Süd, Hannover | 75000 | 6.8 | 94 | 41 | Ausschließen | möglicher False Negative: gute ROI, aber stark altes Inserat | Hausgeld fehlt | https://www.immometrica.com/de/offer/26748834 |
| Hannover | Engelsburg 1, 30629 Hannover | 127000 | 6.4 | 92 | 42 | Ausschließen | möglicher False Negative: gute ROI, aber stark altes Inserat |  | https://www.immometrica.com/de/offer/26760964 |
| Barsinghausen | Berliner Str. 5, 30890 Barsinghausen | 110000 | 6.6 | 91 | 39 | Ausschließen | möglicher False Negative: gute ROI, aber stark altes Inserat | Stadt/Ort nicht in Whitelist: Barsinghausen | https://www.immometrica.com/de/offer/26795490 |
| Springe | 31832, Springe | 79900 | 7.7 | 88 | 47 | Ausschließen | möglicher False Negative: gute ROI, aber stark altes Inserat | Stadt/Ort nicht in Whitelist: Springe; ⚠️ DUBLETTE nahezu gleiche Daten | https://www.immometrica.com/de/offer/26810947 |
| Hannover | Metzhof 3, 30659 Hannover | 68000 | 8.4 | 76 | 38 | Ausschließen | möglicher False Negative: gute ROI, aber stark altes Inserat | MAKLER-WARNFLOSKEL | https://www.immometrica.com/de/offer/26953836 |
| Mittelfeld | 30519 Hannover (Mittelfeld) | 65000 | 6.7 | 71 | 37 | Ausschließen | möglicher False Negative: gute ROI, aber stark altes Inserat |  | https://www.immometrica.com/de/offer/27006750 |
| Bemerode | Bemeroder Anger 17, 30539 Hannover | 135000 | 6.2 | 70 | 46 | Ausschließen | möglicher False Negative: gute ROI, aber stark altes Inserat |  | https://www.immometrica.com/de/offer/27015947 |
| Sahlkamp | Sahlkamp 21, 30179 Hannover | 99000 | 6.7 | 70 | 5 | Ausschließen | möglicher False Negative: gute ROI, aber stark altes Inserat | SANIERUNGSSTAU / renovierungsbedürftig | https://www.immometrica.com/de/offer/27031880 |
| Linden-Nord | Ottenstraße 10a, 30451 Linden-Nord, Hannover | 48000 | 13.5 | 68 | 0 | Ausschließen | möglicher False Negative: gute ROI, aber stark altes Inserat | BLOCKER: ROI >10 % und Hausgeld >6 €/m²; SANIERUNGSSTAU / renovierungsbedürftig; MAKLER-WARNFLOSKEL | https://www.immometrica.com/de/offer/27041063 |
| Ronnenberg | Breite Str. 17C, 30952 Ronnenberg | 108000 | 6.9 | 68 | 44 | Ausschließen | möglicher False Negative: gute ROI, aber stark altes Inserat | Stadt/Ort nicht in Whitelist: Ronnenberg; Hausgeld fehlt | https://www.immometrica.com/de/offer/27043910 |
| Ronnenberg | 30952 Niedersachsen - Ronnenberg 30952 Niedersachsen - Ronnenberg | 108000 | 6.2 | 69 | 44 | Ausschließen | möglicher False Negative: gute ROI, aber stark altes Inserat | Stadt/Ort nicht in Whitelist: Ronnenberg; Hausgeld fehlt | https://www.immometrica.com/de/offer/27049357 |

## Needs Due Diligence

_Keine Objekte._

## Interpretation

- **POTENTIAL_FALSE_NEGATIVE**: Der Agent hat ein Objekt ausgeschlossen, das laut Liquiditäts-Audit nicht ungeprüft verworfen werden sollte.
- **NEEDS_DUE_DILIGENCE**: Der Agent hat das Objekt nicht ausgeschlossen, aber das Audit erkennt ein Alters-/Liquiditätsrisiko.
- **LIKELY_VALID_EXCLUSION**: Der Ausschluss ist wahrscheinlich mit dem Liquiditäts-Audit konsistent.
- **OK**: Es besteht kein Konflikt zwischen Agentenentscheidung und Audit.
