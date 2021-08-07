n, m = map(int, input().split())

min_a = []

for i in range(n):
    col = list(map(int, input().split()))

    min_val = min(col)

    min_a.append(min_val)
    min_a.sort(reverse=True)

print(min_a[0])

