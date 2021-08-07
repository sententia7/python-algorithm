n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort(reverse=True)
f_val = data[0]
s_val = data[1]

result = 0;
o_cnt = k

for i in range(m):
    if(o_cnt == 0):
        result += s_val
        o_cnt = k
    else:
        result += f_val
        o_cnt -= 1
print(result)
