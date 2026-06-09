#!/usr/bin/env bash

set -euo pipefail

if command -v hugo >/dev/null 2>&1; then
  echo "Preview: http://localhost:1313/"
  exec hugo server --disableFastRender
fi

if [ ! -f public/index.html ]; then
  echo "ERROR: Hugo is not installed and public/index.html has not been built."
  echo "Install Hugo 0.162.0 Extended, then run: pnpm build"
  exit 1
fi

echo "Hugo is not installed; serving the last generated site."
echo "Preview: http://localhost:1313/"
exec /usr/bin/python3 -m http.server 1313 --directory public
