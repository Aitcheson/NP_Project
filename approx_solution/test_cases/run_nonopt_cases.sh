#!/bin/bash
echo "Running non-optimal case:"
cat ./test-nonoptimal.txt
echo "Solution:"
python ../approximate_min_cover.py < ./test-nonoptimal.txt
