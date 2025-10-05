# 📘 GhostVault Sync — Handleiding

> **Automatische back-up & GitHub-synchronisatie voor GhostVault**  
> Ondersteunt **Windows (.bat)** en **macOS/Linux (.sh)**

---

## 🔹 Wat doet GhostVault Sync?
GhostVault Sync combineert twee functies in één actie:
1. 💾 **Lokale back-up:**  
   Maakt een tijdstempel-kopie van je map `Projects/` in  
   `Backups/auto/Projects_YYYY-MM-DD_HH-MM`.
2. 🚀 **GitHub-sync:**  
   Voert automatisch uit:  
   ```
   git add .
   git commit -m "Auto-sync <datum/tijd>"
   git pull --rebase origin main
   git push
   ```

Je project wordt dus **veilig lokaal bewaard én geüpload naar GitHub** met één commando.

---

## 🪟 Gebruik op Windows
1. Dubbelklik `ghostvault_sync_full.bat`  
   *(of in PowerShell: `.\ghostvault_sync_full.bat`)*  
2. Wacht tot je “✅ GhostVault volledig gesynchroniseerd met GitHub!” ziet.  
3. Klaar! De nieuwste versie staat op GitHub en je lokale back-up is gemaakt.

---

## 🍏 Gebruik op macOS of Linux
1. Open Terminal in je GhostVault-map:
   ```bash
   cd ~/GhostVault/GhostVault_Starter
   chmod +x ghostvault_sync_full.sh   # eenmalig
   ./ghostvault_sync_full.sh
   ```
2. Je ziet de meldingen voor back-up en sync verschijnen.  
3. Controleer daarna je GitHub-repo — alles is bijgewerkt.

---

## 🧠 Tip: automatische editorinstelling
Voorkom dat Git de Vim-editor opent:
```bash
git config --global core.editor "notepad"    # Windows
git config --global core.editor "nano"       # macOS/Linux
```

---

## ⚙️ Veelvoorkomende meldingen
| Melding | Betekenis | Oplossing |
|----------|------------|-----------|
| `LF will be replaced by CRLF` | Git zet regelafbrekingen om naar Windows-stijl | Negeer |
| `nothing to commit, working tree clean` | Geen nieuwe bestanden | Alles up-to-date |
| `rejected (fetch first)` | Remote bevat nieuwere versies | Eerst `git pull --rebase origin main` |

---

## 🧩 Structuurvoorbeeld
```
GhostVault_Starter/
│
├─ Projects/
│   ├─ GhostCoach/
│   └─ ...
├─ Backups/
│   └─ auto/
│       └─ Projects_YYYY-MM-DD_HH-MM/
├─ ghostvault_sync_full.bat
├─ ghostvault_sync_full.sh
└─ README_sync.md
```

---

## ✨ Credits
Created by **Jochem Jacobs**  
💡 Project: [GhostVault](https://github.com/GhostToolsGT/GhostVault) — onderdeel van het **Ghost.Tools-ecosysteem**
