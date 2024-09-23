# 구해야 하는 것 :
# cond) 문자열 s가 주어질 때,
# answ) [규칙에 따라 변환된 문자열이 1이 될때까지 변환한 횟수, 변환과정에서 제거된 모든 0의 개수] 를 return

# 알아야 하는 것 :
# bin() : 이진변환 함수

def solution(s):
    transform_count = 0
    total_zeros_removed = 0
    
    while s != "1" :
        zeros_removed = s.count("0")
        total_zeros_removed += zeros_removed
        s = s.replace("0", "")
        
        s = bin(len(s))[2:]
        
        transform_count += 1
        
    answer = [transform_count, total_zeros_removed]
        
    return answer