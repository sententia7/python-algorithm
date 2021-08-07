n, k = map(int, input().split())
cnt = 0

while n != 1:
    if(n % k == 0):
        n //= k
    else:
        n -= 1
    cnt += 1

print(cnt)



# N, K를 공백으로 구분하여 입력받기
n, k = map(int, input().split())
result = 0

while True:
    # 시이 우보다 작을 때(더 이상 나눌 수 없을 때) 반복문 탈출
    if n < k:
        break

    # (N == K로 나누어떨어지는 수)가 될 때까지 1씩 빼기
    target = (n // k) * k
    result += (n - target)
    n = target

    # 유로 나누기
    result += 1
    n //= k

# 마지막으로 남은 수에 대하여 1씩 빼기
result += (n - 1)
print(result)