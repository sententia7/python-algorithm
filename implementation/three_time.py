h = int(input())

cnt = 0;

for i in range(h+1):
    for j in range(60):
        for z in range(60):
            if '3' in f'{i}{j}{z}':
                cnt += 1
print(cnt)
# for i in range(60):

#[x for x in lst if '6' in f'{x}']

# lst = [25, 64, 67, 81, 90]
# print([x for x in lst if '6' in f'{x}'])
#
# for i in lst:
#     if '6' in f'{i}':
#         print("1")
