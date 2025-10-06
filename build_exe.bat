@echo off
cd /d "%~dp0"
python -m PyInstaller --onefile --noconsole --name GhostVault --icon=ghost_icon.ico ghostvault_app.py
copy /Y ".\dist\GhostVault.exe" ".\GhostVault.exe"
echo ✅ Build klaar. Druk op een toets om te sluiten.
pause