# TLE for 2 test cases

T = int(input())

for _ in range(T):
    N, K = list(map(int, input().split()))
    binary = input()
    binary = binary + binary
    i = 1
    max_i = [0]
    while i < N:
        j = 0
        if binary[i : i + N] > binary[max_i[0] : max_i[0] + N]:
            max_i = [i]
        elif binary[i : i + N] == binary[max_i[0] : max_i[0] + N]:
            max_i.append(i)
        i += 1

    if K % len(max_i) == 0:
        print(N * (K // len(max_i) - 1) + max_i[-1])
    else:
        print(N * (K // len(max_i)) + max_i[K % len(max_i) - 1])
