import ar
import q_sort

x = ar.rarray(0, 100);
print "++++++++++ the unsort array ++++++++++\n";
print(x);
print "\n--------- the sort array ---------\n";
q_sort.sort(x);
print(x);
print "\n++++++++++ end ++++++++++";