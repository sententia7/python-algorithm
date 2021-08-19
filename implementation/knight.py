# 8 x 8 평면도(세로 1~8, 가로 a~h)
# 나이트는 이동할때 L자 혈태로 이동(정원밖으로 나갈 수 없다)
# 2가지 경우로 이동
# - 가로 두칸 이동후 수직으로 한칸 이동
# - 세로 두칸 이동후 수평으로 한칸 이동
# print(ord("a")) #아스키코드 문자를 숫자로
# print(chr(97)) #아스키코드 숫자를 문자로
import string

# 현재값
coordinate = input()
row = ord(coordinate[0:1]) #열 (a~h)
col = coordinate[1:2] #행 (1~8)



# x : +2 or -2, y : +1 or -1
# x : +1 or -1, y : +2 or -2
#(+2,+1), (+2,-1), (-2,+1), (-2,-1)
#(+1,+2), (-1,-2), (-1,+2), (-1,-2)
cnt = 0
if((col == '1' or col == '8') and (row == 97 or row == 104)):
    cnt = 2
elif(((col == '2' or col == '7') and (row == 97 or row == 104)) or
     ((col == '1' or col == '8') and (row == 98 or row == 103))):
    cnt = 3
elif(((col >= '3' or col <= '6') and (row == 97 or row == 104)) or
    ((col == '1' or col == '8') and (row >= 99 or row <= 102)) or
    ((col == '2' or col == '7') and (row == 98 or row == 103))):
    cnt = 4
elif(((col >= '3' or col <= '6') and (row == 98 or row == 103)) or
    ((col == '2' or col == '7') and (row >= 99 or row <= 102))):
    cnt = 6
else:
    cnt = 8

print(cnt)

# print(string.ascii_lowercase)
# ab = list(map(chr, range(97, 105)))
# print(ab[0]) #아스키코드 a ~ h까지


#풀이
#현재 나이트의 위치 입력받기
# input_data = input()
# row = int(input_data[1])
# column = int(ord(input_data[0])) - int(ord('a')) + 1
#
# # 나이트가 이동할 수 있는 8가지 방향 정의
# steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1)z (1, 2), (-1, 2), (-2, 1)]
#
# # 8가지 방향에 대하여 각 위치로 이동이 가능한지 확인
# result = 0
# for step in steps:
#     # 이동하고자 하는 위치 확인
#     next_row = row + step[0]
#     next_column = column + step[1]
#
#     # 해당 위치로 이동이 가능하다면 카운트 증가
#     if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
#         result += 1
#
# print(result)