This is a small example program which demonstrates some python code I wrote. It
is a command-line application that will calculate the ranking table for a soccer
league given some match results.

The main program is solutions.py

Command line help is available with no arguments and no standard input, or an
argument of -h or --help

The input is game results, one per line (see sample-input.txt). The output is a
ranking of teams and their points, one per line (see expected-output.txt). We
expect that the input will be well-formed.

In this league, teams accumulate points by winning (3 points) or drawing (1
point).  If two teams have the same number of points, they are ranked equally
and are output in alphabetical order.

Tests are in test.py and can be run by executing test.py.
The tests assume solution.py is in the same directory
or in the module path.
