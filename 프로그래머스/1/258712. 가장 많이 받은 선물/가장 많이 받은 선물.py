# 구하고자 하는 것 : 가장 많은 선물을 받는 친구가 받을 선물의 수
# 구현으로 그냥 풀기 (표 형식으로 정리해버리기)

def solution(friends, gifts):
    n = len(friends)
    gift_matrix = [[0] * n for _ in range(n)]
    gift_index = {friend: [0, 0] for friend in friends}

    friend_to_index = {friend: i for i, friend in enumerate(friends)}

    for gift in gifts:
        giver, receiver = gift.split()
        i, j = friend_to_index[giver], friend_to_index[receiver]
        gift_matrix[i][j] += 1
        gift_index[giver][0] += 1
        gift_index[receiver][1] += 1 
    
    for friend in friends:
        given, received = gift_index[friend]
        gift_index[friend] = given - received
    
    next_month_gifts = [0] * n
    for i in range(n):
        for j in range(i+1, n):
            if gift_matrix[i][j] > gift_matrix[j][i]:
                next_month_gifts[i] += 1
            elif gift_matrix[i][j] < gift_matrix[j][i]:
                next_month_gifts[j] += 1
            else:
                if gift_index[friends[i]] > gift_index[friends[j]]:
                    next_month_gifts[i] += 1
                elif gift_index[friends[i]] < gift_index[friends[j]]:
                    next_month_gifts[j] += 1
    
    answer = max(next_month_gifts)
    
    return answer