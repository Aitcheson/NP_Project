#!/bin/bash
for file in *.txt; do
    echo "Timing test case: $file"
    /usr/bin/time -p python ../approximate_min_cover.py < $file
done
