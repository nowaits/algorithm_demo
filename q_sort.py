_DEBUG=False

def partion(A, p, q):
	if (p >= q):
		return p;
	x = A[q];
	k = p;
	for i in range(p, q):
		if (A[i] <= x) :
			A[i], A[k] = A[k],A[i];
			k +=1;
	A[k], A[q] = A[q], A[k];
	return k;

def quick_sort(A, p, q):
	if (p >= q):
		return
	x = partion(A, p, q);
	if _DEBUG == True: 
		import pdb 
		pdb.set_trace();
	quick_sort(A, p, x - 1);
	quick_sort(A, x + 1, q);

def sort(A):
	quick_sort(A, 0, len(A) - 1);
