import random
def array(a, b):
	return [x for x in range(a, b)];

def rarray(a, b):
	x = array(a, b);
	random.shuffle(x);
	return x;