#구하고자 하는 것 : 주어진 매개변수 n과 top에 따라 채워지는 타일의 경우의 수를 10007로 나눈 나머지
# 문제를 2번 순서대로 풀어야함
# 1. n과 top에 따라 주어지는 퍼즐
# 2. 이 퍼즐에 맞는 경우의 수
# 즉, DP임을 알 수 있다.

# 현재 위치에 삼각형을 놓는 경우의 수 = 이전 위치의 모든 경우의 수
# 현재 위치에 마름모를 놓는 경우의 수 = 이전 위치에서 위쪽에 공간이 있는 경우의 수

def solution(n, tops):
    MOD = 10007
    dp1 = [0] * n
    dp2 = [0] * n
    dp1[0] = 1
    dp2[0] = 2 + tops[0]
    
    for i in range(1, n):
        dp1[i] = (dp1[i - 1] + dp2[i - 1]) % MOD
        dp2[i] = ((dp1[i - 1] * (1 + tops[i])) + \
                (dp2[i - 1] * (2 + tops[i]))) % MOD
        
    return (dp1[-1] + dp2[-1]) % MOD 