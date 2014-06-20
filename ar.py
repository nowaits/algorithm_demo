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

def genMatrix(M, N):
    matrix = [[m*N+n  for n in range(N)] for m in range(M)]
    return matrix;

def printMatrix(A, M, N):
    for i in range(M):
        for j in range(N):
            print("%10d"% A[i][j]),
        print;