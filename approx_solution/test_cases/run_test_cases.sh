#!/bin/bash
for file in *.txt; do
    echo "Running test case: $file"
    python main.py < $file
done

