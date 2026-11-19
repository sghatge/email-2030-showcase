#!/bin/sh
for d in 0[145]-*/; do (cd "$d" && python -m pytest -q) || exit 1; done
