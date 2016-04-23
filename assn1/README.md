To run this assignment, an input file must first be generated. To
generate a test input file, run the following command once all files
have been downloaded:

    $python generate_test.py <#>

where <#> is replaced by the number of points you want in your input
file. A test input file with the name input<#>.txt will be generated.

Once an input file is available, type the following command into the
command line to run the nearest neighbor algorithm on the contents of
the input file:

    $python nearest_neighbor.py <filename>.txt

where <filename> is replaced by the name of the test input file, which
is likely to be "input<#>" unless a custom input file is created and
used instead.

Running nearest_neighbor.py will find the distance between the closest
pair of points in the input file and output that distance as a decimal
value in a file named:

    <filename>_distance.txt

corresponding to the name of the input text file.

The program also outputs the runtimes of the brute force and divide
and conquer methods of implementing this assignment. The brute force
runtime is displayed first and is followed by the divide and conquer
runtime. Both times are in seconds.
