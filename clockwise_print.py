import ar

def calc(A, M, N, B):
    m = 0;
    n = 0;
    while 2 * m < M and 2 * n < N:
            for i in range(n, N - n):
                B.append(A[m][i]);
            for i in range(m + 1, M - m - 1):
                B.append(A[i][N - n - 1]);
            if (2 * m + 1 < M):
                for i in range(N - n - 1, n - 1, -1):
                    B.append(A[M - m - 1][i]);
            if(2 * n + 1 < N):
                for i in range(M - m - 2, m, -1):
                    B.append(A[i][n]);
            m += 1;
            n += 1;
    
def show(A, M, N):
    B = [];
    calc(A, M, N, B);
    print B;
