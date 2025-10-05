@echo off
title GhostVault Full Sync
echo =====================================================
echo 🔁  GhostVault: automatische backup + GitHub sync
echo =====================================================

REM --- 1️⃣  MAAK LOKALE BACKUP ---
set SOURCE=%~dp0
set TARGET=%~dp0Backups\auto
if not exist "%TARGET%" mkdir "%TARGET%"
set DATESTAMP=%DATE:~6,4%-%DATE:~3,2%-%DATE:~0,2%_%TIME:~0,2%-%TIME:~3,2%
set DATESTAMP=%DATESTAMP: =0%

xcopy "%SOURCE%Projects" "%TARGET%\Projects_%DATESTAMP%" /E /I /Y >nul
echo 💾 Backup gemaakt in: %TARGET%\Projects_%DATESTAMP%

REM --- 2️⃣  SYNC MET GITHUB ---
echo =====================================================
echo 🚀  GitHub synchronisatie gestart...
cd /d "%~dp0"

git add .
git commit -m "Auto-sync %DATE% %TIME%"
git pull --rebase origin main
git push

if %errorlevel% neq 0 (
    echo ⚠️  Er ging iets mis met de Git push. Controleer verbinding of login.
) else (
    echo ✅  GhostVault volledig gesynchroniseerd met GitHub!
)

echo =====================================================
pause