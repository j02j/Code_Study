# 구해야 하는 것 : 숫자들 규칙대로 밀었을 때, 바뀐 것 중에 가장 작은 숫자들을 순서대로 배열한 것을 return

# 풀이
# 아래>위, 좌>우, 위>아래, 우>좌로 한칸씩 당겨서 tmp에 땡겼던 애들 기억해서 집어넣기(그냥구현)

def solution(rows, columns, queries):

    answer = []
    array = [[0 for col in range(columns)] for row in range(rows)]
    t = 1
    for row in range(rows):
        for col in range(columns):
            array[row][col] = t
            t += 1

    for x1,y1,x2,y2 in queries:
        tmp = array[x1-1][y1-1]
        mini = tmp

        for k in range(x1-1,x2-1):
            test = array[k+1][y1-1]
            array[k][y1-1] = test
            mini = min(mini, test)

        for k in range(y1-1,y2-1):
            test = array[x2-1][k+1]
            array[x2-1][k] = test
            mini = min(mini, test)

        for k in range(x2-1,x1-1,-1):
            test = array[k-1][y2-1]
            array[k][y2-1] = test
            mini = min(mini, test)

        for k in range(y2-1,y1-1,-1):
            test = array[x1-1][k-1]
            array[x1-1][k] = test
            mini = min(mini, test)

        array[x1-1][y1] = tmp
        answer.append(mini)

    return answer