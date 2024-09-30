# 구하고자 하는 것 : 규칙에 따른 배열 return
# 생각 요소 : 삼각형 형식이 아니라  ↓ > → > ↑ + ← 라고 생각하기.
# 1. 주어진 n에 따른 직각삼각형 생성
# 2. 다음 칸이 0부터 n 범위 내에 위치하고 값이 0일 경우 y, x값 변경
# 3. 범위를 벗어나거나 값이 0이 아닐 경우 방향 변경

def solution(n):
    # 1. 주어진 n에 따른 직각삼각형 생성
    triangle = [[0] * i for i in range(1, n+1)]
    
    # 초기 위치 및 방향 설정
    x, y = 0, 0
    num = 1
    
    # 방향 정의 (아래, 오른쪽, 왼쪽 위)
    directions = [(1, 0), (0, 1), (-1, -1)]
    direction = 0
    
    while num <= (n * (n + 1)) // 2:
        triangle[y][x] = num
        num += 1
        
        # 2. 다음 칸이 0부터 n 범위 내에 위치하고 값이 0일 경우 y, x값 변경
        ny, nx = y + directions[direction][0], x + directions[direction][1]
        
        # 3. 범위를 벗어나거나 값이 0이 아닐 경우 방향 변경
        if not (0 <= ny < n and 0 <= nx <= ny) or triangle[ny][nx] != 0:
            direction = (direction + 1) % 3
            ny, nx = y + directions[direction][0], x + directions[direction][1]
        
        y, x = ny, nx
    
    # 결과를 1차원 배열로 변환
    answer = [num for row in triangle for num in row]
    
    return answer