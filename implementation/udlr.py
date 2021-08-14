#예시
#N을 3으로 입력했을떄(첫번째 라인)
#1,3이 열의 끝(U,R 무시)
#3,1이 행의 끝(D,L 무시)
#3,3이 형열의 끝 (D,R 무시)

#Up Down Left Right
space = int(input()) # N x N 값
move = input().split() # 상,하,좌,우 값
x, y = 1, 1 # 시작 위치

for i in move:
    if(i == 'U' and x != 1): #1,1 or 1, N
        x -= 1
    elif(i == 'D' and x != space): #N,1 or N,N
        x += 1
    elif(i == 'R' and y != space): #1,N or N,N
        y += 1
    elif(i == 'L' and y != 1): #1,1 or N,1
        y -= 1

print(x, y)



# 풀이
# n = int(input())
# x , y = 1, 1
# plans = input().split()
# # L, R, U, 다에 따른 이동 방향
#
# dx = [0, 0, -1, 1]
# dy = [-1, 1, 0, 0]
# move_types = ['L', 'R', 'U', 'D']
# # 이동 계획을 하나씩 확인
# for plan in plans:
# # 이동 후 좌표 구하기
#     for i in range(len(move_types)):
#         if plan == move_types[i]:
#             nx = x + dx[i]
#             ny = y + dy[i]
#     # 공간을 벗어나는 경우 무시
#     if nx < 1 or ny < 1 or nx > n or ny > n:
#         continue
#     # 이동 수행
#     x, y = nx, ny
# print(x,y)