def rotate_array(A, offset, count):
    i = offset;
    t = A[i];
    c = 0;
    while c < count:
        t, A[(i+offset)%count] = A[(i+offset)%count], t;
        i = (i+offset)%count;
        c+=1;