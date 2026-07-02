# KI-Automatisierungs-Roadmap - Immobilien-Screener

## Phase 1 - MVP & Validierung

### Infrastruktur

- ChatGPT Plus
- Custom GPT oder Projekt-Chat
- Manuelle ImmoMetrica CSV-/E-Mail-Analyse

### Ziel

- Prompt validieren
- Parser prüfen
- Scoring fachlich kalibrieren
- Hannover- und Leipzig-Test reproduzierbar machen

### Status

Aktiv.

## Phase 2 - Automatischer Pförtner

### Infrastruktur

- Make.com
- Google Gemini API
- Gmail oder IMAP

### Ziel

- E-Mails automatisch empfangen
- Basisdaten extrahieren
- schlechte Objekte automatisch aussortieren
- nur interessante Objekte weiterleiten

### Wichtig

Der automatische Pförtner darf nur nach stabiler Phase-1-Kalibrierung aktiviert werden.

## Phase 3 - Auditor & Sekretär

### Infrastruktur

- Claude Desktop Pro
- Lokaler MCP-Server
- Playwright

### Ziel

- Login bei ImmoMetrica lokal durchführen
- Exposé-Daten vertiefen
- Cashflow genauer berechnen
- Makleranschreiben vorbereiten

### Datenschutzprinzip

Passwörter und lokale Sessions bleiben auf dem eigenen Rechner.

## Phase 4 - Dokumentenprüfung

### Infrastruktur

- Claude Project
- PDF-Analyse

### Ziel

- Wirtschaftsplan prüfen
- Eigentümerversammlungsprotokolle prüfen
- Energieausweis prüfen
- Sonderumlagen und Sanierungsstau erkennen

## Phase 5 - Investor Dashboard

### Infrastruktur

- Lovable.dev
- Supabase

### Ziel

- Status-Tracking
- Deal-Pipeline
- Scoring-Historie
- Cashflow-Visualisierung

## Kostenstrategie

| Tool | Phase | Kostenlogik |
|---|---|---|
| ChatGPT Plus | Phase 1 | bereits vorhanden |
| Google AI Studio / Gemini | Phase 2 | Free Tier nutzen |
| Make.com | Phase 2 | Free Plan testen |
| Claude Pro | Phase 3–4 | erst bei stabiler Vorfilterung |
| Lovable.dev | Phase 5 | erst nach Backend-Stabilität |

## Architekturprinzip

Lean & Safe Architecture:

- Erst manuell validieren.
- Dann low-cost automatisieren.
- Erst danach tiefere Tool-Integration.
- Kein Dashboard bauen, bevor Parser, Filter und Scoring stabil sind.