#입력
# 55-50+40

#출력
# -35

#참고사항
# +를 먼저하고 -하면 최소값이 나온다

data = input().split("-")

result = 0

for i in data[0].split("+"):
    result += int(i)
for i in data[1:]:
    for j in i.split("+"):
        result -= int(j)
print(result)

# 런타임 에러
# -기준으로 split 후 각 값들을 eval로 계산 시켜버리고 첫번째 [0]만 더하고 나머지는 빼버린다
#05-01+40 할때 eval를 할때는 앞에 0이 있으면 안된다
# data = input().split("-")
#
# result = 0
#
# for i in data[0].split("+"):
#     result += int(i)
#     for j in data[1:]:
#         result -= int(eval(j))
#
# print(result)