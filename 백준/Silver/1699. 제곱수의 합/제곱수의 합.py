import sys

n = int(input())

# dp[i]는 i를 제곱수의 합으로 표현할 때 필요한 최소 항의 개수를 저장
dp = [0] * (n + 1)

for i in range(1, n + 1):
    dp[i] = i  # i를 1^2으로만 표현했을 때의 개수로 초기화

    j = 1
    while j * j <= i:
        dp[i] = min(dp[i], dp[i - j * j] + 1)
        j += 1

print(dp[n])