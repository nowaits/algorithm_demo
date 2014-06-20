# import system module
import copy
# import custom module
import ar
import q_sort
import heap_sort
import permutation
import clockwise_print

x0 = ar.rarray(0, 30);
print "++++++++++ the unsort array ++++++++++\n";
x = copy.deepcopy(x0);
print(x);

print "\n--------- quick sort array ---------\n";
q_sort.sort(x);
print(x);

print "\n--------- heap sort array ---------\n";
x = copy.deepcopy(x0);
heap_sort.sort(x);
print(x);

print "\n--------- the permutation of array ---------\n";
x = ar.array(0, 4);
x = permutation.show(x, 0, len(x));
print("total have %d arrays."% x);


M = 7;
N = 3;
print "\n--------- clock_wrise show matrix[%d][%d]---------\n"%(M, N);
A = ar.genMatrix(M, N);
ar.printMatrix(A, M, N);
clockwise_print.show(A, M, N);