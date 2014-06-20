count = 0;
def show(A, pos, len):
    for i in range(pos, len):
        A[i], A[pos] = A[pos], A[i];
        if (pos == len - 1):
            print(A);
            global count
            count += 1;
        else:
            show(A, pos + 1, len);
        A[i], A[pos] = A[pos], A[i];
    return count;
