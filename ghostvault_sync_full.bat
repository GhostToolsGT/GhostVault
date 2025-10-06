@echo off
title GhostVault Full Sync
chcp 65001 >nul
setlocal enableextensions
echo =====================================================
echo 🔁  GhostVault: automatische backup + GitHub sync
echo =====================================================

REM --- 1) BACKUP ---
set "SOURCE=%~dp0"
set "TARGET=%~dp0Backups\auto"
if not exist "%TARGET%" mkdir "%TARGET%"
set "DATESTAMP=%DATE:~6,4%-%DATE:~3,2%-%DATE:~0,2%_%TIME:~0,2%-%TIME:~3,2%"
set "DATESTAMP=%DATESTAMP: =0%"

echo GV_STEP:BACKUP_START
xcopy "%SOURCE%Projects" "%TARGET%\Projects_%DATESTAMP%" /E /I /Y >nul
echo GV_STEP:BACKUP_DONE
echo 💾 Backup gemaakt in: %TARGET%\Projects_%DATESTAMP%

REM --- 2) GIT SYNC ---
cd /d "%~dp0"
echo =====================================================
echo 🚀  GitHub synchronisatie gestart...

echo GV_STEP:ADD_START
git add -A

REM Check of er iets te committen is
git diff --cached --quiet
if %errorlevel%==0 (
    echo ℹ️  Geen wijzigingen om te committen.
    echo GV_STEP:COMMIT_DONE
) else (
    git commit -m "Auto-sync %DATE% %TIME%"
    echo GV_STEP:COMMIT_DONE
)

echo GV_STEP:PULL_START
git pull --rebase --no-edit origin main
if %errorlevel% neq 0 (
    echo ⚠️  Pull gaf een fout.
)
echo GV_STEP:PULL_DONE

echo GV_STEP:PUSH_START
git push
if %errorlevel% neq 0 (
    echo ⚠️  Push gaf een fout.
    echo GV_STEP:PUSH_FAIL
    endlocal & exit /b 1
) else (
    echo GV_STEP:PUSH_DONE
    echo ✅  GhostVault volledig gesynchroniseerd met GitHub!
    endlocal & exit /b 0
)