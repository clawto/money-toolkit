#!/bin/bash
set -euo pipefail
PASS=0; FAIL=0
assert() { if [ $? -eq 0 ]; then PASS=$((PASS+1)); echo "  ✅ $1"; else FAIL=$((FAIL+1)); echo "  ❌ $1"; fi; }
echo "=== Money Toolkit Tests ==="
[ -f SKILL.md ]; assert "SKILL.md"
grep -q "^---" SKILL.md; assert "frontmatter"
[ -x scripts/compound.py ]; assert "compound.py"
[ -x scripts/arbitrage.py ]; assert "arbitrage.py"
[ -x scripts/defi-yield.py ]; assert "defi-yield.py"
[ -x scripts/gas-fee.py ]; assert "gas-fee.py"
! grep -r "ghp_\|gho_" scripts/ 2>/dev/null; assert "no secrets"
python3 scripts/compound.py 10000 1000 12 10 2>/dev/null; assert "compound.py runs"
python3 scripts/gas-fee.py 2>/dev/null; assert "gas-fee.py runs"
echo "=== $PASS passed, $FAIL failed ==="
exit $FAIL
