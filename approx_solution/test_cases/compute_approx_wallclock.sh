#!/bin/bash
for file in *.txt; do
    echo "Timing test case: $file"
    /usr/bin/time -p python main.py < $file
done
