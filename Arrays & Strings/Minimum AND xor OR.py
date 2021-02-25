T = int(input())

for _ in range(T):
    input()
    arr = sorted(map(int, input().split()))
    print(min([arr[i] ^ arr[i + 1] for i in range(len(arr) - 1)]))

