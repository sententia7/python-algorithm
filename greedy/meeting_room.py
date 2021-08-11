import sys
input = sys.stdin.readline
meetCnt = int(input())

var = []
cnt = 0

for i in range(int(meetCnt)):
    time = list(map(int, input().split()))
    var.append(time)

# 종료시간을 오름차순으로 정렬
var.sort(key=lambda x:(x[1], x[0]))

start = 0
count = 0

for time in var:
	if (time[0] >= start):
		count += 1
		start = time[1]
print(count)




#The King God General Jordy 풀이

### 내 풀이 : 시간초과

# n = int(input())
# arr = [[0,0]] * n
# for i in range(n):
#     arr[i] = list(map(int, input().split()))
# # print(arr)
# arr.sort(key=lambda x: (x[0], x[1]))
# print(arr)
#
# resultArr = []
# for a in arr:
#     tempA = a
#     tempArr = []
#     tempArr.append(tempA)
#
#     for b in arr:
#         # 최초 tempA = [0,6]
#         if (tempA[1] <= b[0]): # 종료시간이 그다음 회의 시작시간보다 작거나 같으면.. 가능
#             tempArr.append(b)
#             tempA = b
#
#     resultArr.append(len(tempArr)) # 길이를 담기 위함
#     # print(tempArr)
#     # print('-----------')
#
# print(max(resultArr))



# import sys
# input = sys.stdin.readline
# n = int(input())
# arr = [[0,0]] * n
# for i in range(n):
#     arr[i] = list(map(int, input().split()))
#
#
#
# arr.sort(key=lambda x: (x[1], x[0]))
#
# start = 0
# count = 0
#
# for time in arr:
# 	if (time[0] >= start):
# 		count += 1
# 		start = time[1]
# print(count)