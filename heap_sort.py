_DEBUG = False

def make_heap(A, cur, size):
    for i in range(size - 2 - cur, -1, -1):
        while True:
            if (A[i / 2 + cur] > A[i + cur] or i + 1 + cur < size and A[i / 2 + cur] > A[i + 1 + cur]):
                min_index = i if  i + 1 + cur < size and A[i + cur] < A[i + 1 + cur] else i + 1;
                A[i / 2 + cur], A[min_index + cur] = A[min_index + cur], A[i / 2 + cur];
            i /= 2;
            if (i == 0):
                break;
        if _DEBUG == True:
            import pdb
            pdb.set_trace();

def sort(A):
    for i in range(0, len(A)):
        make_heap(A, i, len(A));
