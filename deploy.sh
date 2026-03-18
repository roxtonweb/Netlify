#!/usr/bin/env bash
set -e

# Usage: ./deploy.sh "Commit message"
MSG="${1:-Update site}"

git status

git add .
git commit -m "$MSG" || echo "Nothing to commit."
git push

echo "Pushed to GitHub. Netlify will auto‑deploy."
