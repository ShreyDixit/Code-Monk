T = int(input())

for _ in range(T):
    N, K = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    for i in range(N):
        print(arr[(N - K + i) % N], end=" ")
    print("")
