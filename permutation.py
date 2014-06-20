count = 0;
def show(A, pos, size):
    for i in range(pos, size):
        A[i], A[pos] = A[pos], A[i];
        if (pos == size - 1):
            print(A);
            global count
            count += 1;
        else:
            show(A, pos + 1, size);
        A[i], A[pos] = A[pos], A[i];
    return count;
