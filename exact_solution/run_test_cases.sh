#!/usr/bin/env bash

for file in test_cases/*.txt; do
    echo "Running with input file: $file"
    python3 exact_min_cover.py < "$file"
done