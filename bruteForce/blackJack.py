# n : 카드의개수, m : 플레이어가 고른 카드의 합
n, m = map(int, input().split())

# 카드가 쓰여있는 숫자
card_number = list(map(int, input().split()))

result = []
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            if card_number[i] + card_number[j] + card_number[k] > m:
                continue
            else:
                result.append(card_number[i]+card_number[j]+card_number[k])
print(max(result))

# result = 0
#
# for i in range(n):
#     for j in range(i+1, n):
#         for k in range(j+1, n):
#             if card_number[i] + card_number[j] + card_number[k] > m:
#                 continue
#             else:
#                 result = max(result, card_number[i]+card_number[j]+card_number[k])
# print(result)



