@echo off
REM GhostVault automatische back-up (Windows)
REM Pas SOURCE en TARGET aan indien nodig.
set SOURCE=%~dp0
set TARGET=%~dp0Backups\auto

if not exist "%TARGET%" mkdir "%TARGET%"
set DATESTAMP=%DATE:~6,4%-%DATE:~3,2%-%DATE:~0,2%_%TIME:~0,2%-%TIME:~3,2%
set DATESTAMP=%DATESTAMP: =0%

xcopy "%SOURCE%Projects" "%TARGET%\Projects_%DATESTAMP%" /E /I /Y >nul
echo Back-up gemaakt in %TARGET%\Projects_%DATESTAMP%
