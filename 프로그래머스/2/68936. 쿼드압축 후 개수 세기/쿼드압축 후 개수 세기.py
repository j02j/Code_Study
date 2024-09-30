#구해야 하는 것 : arr을 규칙에 따라 압축할 때, 배열에 최종적으로 남는 0의 개수와 1의 개수
# 재귀함수 호출로 해결

def quad(arr, x, y, l):
    for i in range(x, x + l):
        for j in range(y, y + l):
            if arr[i][j] != arr[x][y]:
                l = l // 2
                quad(arr, x, y, l)
                quad(arr, x, y + l, l)
                quad(arr, x + l, y, l)
                quad(arr, x + l, y + l, l)
                return

    answer[arr[x][y]] += 1

def solution(arr):
    global answer
    answer = [0, 0]

    quad(arr, 0, 0, len(arr))

    return answer