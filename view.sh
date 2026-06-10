#!/usr/bin/env bash

set -euo pipefail

if command -v hugo >/dev/null 2>&1; then
  hugo --gc --minify --cleanDestinationDir -b http://127.0.0.1:1313/
elif [ ! -f public/index.html ]; then
  echo "ERROR: Hugo is not installed and public/index.html has not been built."
  echo "Install Hugo 0.162.0 Extended, then run: pnpm build"
  exit 1
fi

if ! command -v node >/dev/null 2>&1; then
  echo "ERROR: Node.js is required for the optimized production preview."
  exit 1
fi

exec node scripts/serve-production.mjs
