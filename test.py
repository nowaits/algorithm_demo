# import system module
import copy
# import custom module
import ar
import q_sort
import heap_sort
import permutation

x0 = ar.rarray(0, 100);
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