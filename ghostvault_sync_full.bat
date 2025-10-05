@echo off
title GhostVault Full Sync
echo =====================================================
echo 🔁  GhostVault: automatische backup + GitHub sync
echo =====================================================

REM --- 1) BACKUP ---
set SOURCE=%~dp0
set TARGET=%~dp0Backups\auto
if not exist "%TARGET%" mkdir "%TARGET%"
set DATESTAMP=%DATE:~6,4%-%DATE:~3,2%-%DATE:~0,2%_%TIME:~0,2%-%TIME:~3,2%
set DATESTAMP=%DATESTAMP: =0%
xcopy "%SOURCE%Projects" "%TARGET%\Projects_%DATESTAMP%" /E /I /Y >nul
echo 💾 Backup gemaakt in: %TARGET%\Projects_%DATESTAMP%

REM --- 2) GIT SYNC ---
cd /d "%~dp0"
echo =====================================================
echo 🚀  GitHub synchronisatie gestart...

git add -A

REM Check of er iets te committen is
git diff --cached --quiet
if %errorlevel%==0 (
    echo ℹ️  Geen wijzigingen om te committen.
) else (
    git commit -m "Auto-sync %DATE% %TIME%"
)

REM Pull altijd (rebase), maar forceer geen editor
git pull --rebase --no-edit origin main

REM Push (ook als er niets te committen was)
git push

if %errorlevel% neq 0 (
    echo ⚠️  Er ging iets mis met de Git push. Controleer verbinding of login.
    exit /b 1
) else (
    echo ✅  GhostVault volledig gesynchroniseerd met GitHub!
    exit /b 0
)