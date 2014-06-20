import random
import string

def array(a, b):
	return [x for x in range(a, b)];

def rarray(a, b):
	x = array(a, b);
	random.shuffle(x);
	return x;

def carray(index_a, index_b):
    return list(string.letters[index_a:index_b]);