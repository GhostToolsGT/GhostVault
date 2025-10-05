# GhostVault — Universele AI Projectkluis (Lokale versie)

**Doel:** Een simpele, robuuste mapstructuur om al je AI-werk (ChatGPT, Gemini, Claude, etc.) veilig op te slaan, te structureren en te back-uppen — zonder Notion of betaalde tools.

## Snel starten
1. Pak deze zip uit op een vaste plek, bijv. `C:\Projects\GhostVault` of `~/GhostVault`.
2. Open de map `Projects/` en maak voor elk project een eigen map (of gebruik de meegeleverde).
3. Plak output uit AI (code, JSON, tekst) in `drafts/` of `exports/` en commit deze later naar je repo.
4. (Optioneel) Activeer automatische back-ups:
   - **Windows:** dubbelklik op `ghostvault_sync.bat` — of plan hem in via Taakplanner.
   - **macOS/Linux:** zie `ghostvault_sync.sh` en maak een cronjob.

## Mapstructuur
```
GhostVault/
├─ Projects/
│  ├─ <ProjectNaam>/
│  │  ├─ drafts/   # ruwe AI-output, ideëen, tussenversies
│  │  ├─ exports/  # geëxporteerde assets (pdf, txt, md, zip)
│  │  ├─ code/     # broncode
│  │  └─ media/    # afbeeldingen, audio, video
├─ Backups/
│  ├─ auto/        # automatische kopieën
│  └─ manual/      # handmatige snapshots
├─ Prompts/        # al je prompts en sjablonen
├─ Schemas/        # JSON schema's voor AI-workflows
└─ Docs/           # readme, changelog, versiehistorie
```

## Aanbevolen workflow
- **Tijdens bouwen:** plak alles wat je maakt in `drafts/` (datum in bestandsnaam).
- **Als iets 'klaar genoeg' is:** verplaats naar `exports/` of `code/` en commit naar GitHub.
- **Maak na elke sessie een manual backup:** kopieer de projectmap naar `Backups/manual/` met datum.

## Licentie
Vrij te gebruiken in eigen projecten. Voor commerciële template-versies: zie Notion Edition (later).
