import sys
data = int(sys.stdin.readline().rstrip())

cnt = 0
c_typ = [500, 100, 50, 10]

for c in c_typ:
    r_cnt = 0
    r_cnt = data // c
    data -= r_cnt * c
    cnt += r_cnt

print(cnt)


# n = 1260
# count = 0
#
# coin_type = [500, 100, 50, 10]
#
# for coin in coin_type:
#     count += n // coin
#     n %= coin
#
# print(count)