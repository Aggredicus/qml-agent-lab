#!/usr/bin/env bash

# Archive and optionally delete a branch safely
# Usage:
#   bash scripts/archive_branch.sh <branch-name>
#
# This script:
# 1. Creates archive/<branch>
# 2. Pushes it to origin
# 3. Optionally deletes the original branch locally and remotely

set -e

BRANCH_NAME="$1"

if [ -z "$BRANCH_NAME" ]; then
  echo "Usage: bash scripts/archive_branch.sh <branch-name>"
  exit 1
fi

ARCHIVE_NAME="archive/$BRANCH_NAME"

echo "Creating archive branch: $ARCHIVE_NAME"

git fetch origin

git branch "$ARCHIVE_NAME" "origin/$BRANCH_NAME" || git branch "$ARCHIVE_NAME" "$BRANCH_NAME"

git push origin "$ARCHIVE_NAME"

read -p "Delete original branch '$BRANCH_NAME'? (y/n): " CONFIRM

if [ "$CONFIRM" = "y" ]; then
  echo "Deleting local branch..."
  git branch -D "$BRANCH_NAME" || true

  echo "Deleting remote branch..."
  git push origin --delete "$BRANCH_NAME" || true

  echo "Branch '$BRANCH_NAME' archived and deleted."
else
  echo "Branch archived but original retained."
fi
