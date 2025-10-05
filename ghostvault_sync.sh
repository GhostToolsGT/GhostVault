#!/usr/bin/env bash
# GhostVault automatische back-up (macOS/Linux)
# Pas SOURCE en TARGET aan indien nodig.
SOURCE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
TARGET="$SOURCE/Backups/auto"
mkdir -p "$TARGET"
STAMP=$(date +"%Y-%m-%d_%H-%M")
cp -R "$SOURCE/Projects" "$TARGET/Projects_$STAMP"
echo "Back-up gemaakt in $TARGET/Projects_$STAMP"
