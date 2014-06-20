_DEBUG=False

def make_heap(A, cur, len):
    for i in range(len - 2, cur, -1):
        while i > cur:
            if (A[i/2] >= A[i] or A[i/2] >= A[i + 1]):
                min_index = i if A[i] < A[i + 1] else i + 1;
                A[i/2], A[min_index] = A[min_index], A[i/2];
            i /= 2;
        if _DEBUG == True:
            import pdb
            pdb.set_trace();

def sort(A):
    for i in range(0, len(A)):
        make_heap(A, i, len(A));