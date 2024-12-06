The approximation solution expects input to be formatted like the following:

3
1 2
1 3
2 4

The first line of input indicates how many edges are to follow.
You may use a file with the input by using the following command, where test.txt is the file containing input:
    python approximate_min_cover.py < test.txt

To run all tests:
    first: chmod +x ./test_cases/run_test_cases.sh
    second: ./test_cases/run_test_cases.sh

    This will run all .txt files in the approx_solution\test_cases folder

To run the non-optimal solution:
    first: chmod +x ./test_cases/run_nonopt_cases.sh
    second: ./test_cases/run_nonopt_cases.sh