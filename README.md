# Immobilien-Kapitalanlage-Agent

Repository für Prompt-Versionierung, Parser-Regeln, Scoring-Logik und Tests des Immobilien-Kapitalanlage-Agenten.

## Kanonische Agentenanweisung

[prompts/system-current.md](prompts/system-current.md) ist die **einzige aktive Quelle der Wahrheit** für das Agentenverhalten. Der vollständige Inhalt genau dieser Datei wird unverändert in die ChatGPT Project Instructions eingefügt. Es gibt keine separate Kompaktversion.

Die identische, versionierte Momentaufnahme liegt unter [prompts/system-v3.5.md](prompts/system-v3.5.md). Frühere Versionen, darunter v3.4, bleiben ausschließlich als historische Referenz erhalten.

## Workflow

1. AGENT 0 – CSV Import & Parser Validation
2. AGENT 1 – Email & CSV Filter
3. AGENT 2 – Kapitalanlage Analyst
4. AGENT 3 – Safety & Due Diligence
5. AGENT 4 – Final Summary

Grundsatz: Ohne erfolgreichen CSV-Import entstehen keine Scores, Rankings oder Deep Dives.

## Lokale Prüfungen

```powershell
python .\tests\smoke_parser_test.py
python .\src\liquidity_audit.py --input .\tests\fixtures\raw\<file>.csv
```
