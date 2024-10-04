# 구하고자 하는 것 : 실패율이 높은 스테이지부터 내림차순으로 담긴 배열
# 실패율 = 해당하는 스테이지를 클리어하지 못한 플레이어(N : 1 - 클리어 한 플레이어 수)/스테이지에 도착한 플레이어(1)
# 멈춰있다 : 클리어하지 못했다.
# 각 스테이지에 머물러 있는 플레이어 수를 계산
#          의 실패율 계산
# 실패율을 기준으로 내림차순 (단, 실패율이 같으면 스테이지 번호 오름차순)
# 배열 반환

def solution(N, stages):
    stage_counts = [0] * (N + 2)
    for stage in stages:
        stage_counts[stage] += 1
    
    failure_rates = []
    total_players = len(stages)
    for i in range(1, N + 1):
        if total_players == 0:
            failure_rates.append((i, 0))
        else:
            failure_rate = stage_counts[i] / total_players
            failure_rates.append((i, failure_rate))
        total_players -= stage_counts[i]
    
    failure_rates.sort(key=lambda x: (-x[1], x[0]))
    
    answer = [stage for stage, _ in failure_rates]
    
    return answer