def count_inversion(M, N):
    num_inversions = 0
    for i in range(N):
        for j in range(N):
            for p in range(i, N):
                for q in range(j, N):
                    if M[i][j] > M[p][q]:
                        num_inversions += 1

    return num_inversions


T = int(input())

for _ in range(T):
    N = int(input())
    M = [list(map(int, input().split())) for _ in range(N)]
    print(count_inversion(M, N))
