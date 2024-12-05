#!/bin/bash
for file in *.txt; do
    echo "Running test case: $file"
    cat $file
    echo "Solution:"
    python ../approximate_min_cover.py < $file
    echo "---"
done

