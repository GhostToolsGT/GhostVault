#!/usr/bin/env bash
# ==============================================
# 🔁 GhostVault: automatische backup + GitHub sync
# ==============================================

SOURCE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
TARGET="$SOURCE/Backups/auto"

mkdir -p "$TARGET"
STAMP=$(date +"%Y-%m-%d_%H-%M")

echo "💾  Backup wordt gemaakt..."
cp -R "$SOURCE/Projects" "$TARGET/Projects_$STAMP" 2>/dev/null
echo "✅  Backup opgeslagen in: $TARGET/Projects_$STAMP"

echo "🚀  GitHub synchronisatie gestart..."
cd "$SOURCE" || exit 1

git add .
git commit -m "Auto-sync $(date)"
git pull --rebase origin main
git push

if [ $? -eq 0 ]; then
  echo "✅  GhostVault volledig gesynchroniseerd met GitHub!"
else
  echo "⚠️  Er ging iets mis met de Git push. Controleer verbinding of login."
fi

echo "=============================================="