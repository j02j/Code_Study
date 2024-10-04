#구하고자 하는 것 : 방 개설자가 보는 로그를 배열로 return
# 유저 아이디와 최종 닉네임 매핑 > 매핑된거로 메시지 생성

def solution(record):
    user_dict = {}
    actions = []
    
    for r in record:
        parts = r.split()
        action = parts[0]
        uid = parts[1]
        
        if action in ["Enter", "Change"]:
            nickname = parts[2]
            user_dict[uid] = nickname
    
    for r in record:
        parts = r.split()
        action = parts[0]
        uid = parts[1]
        
        if action == "Enter":
            actions.append(f"{user_dict[uid]}님이 들어왔습니다.")
        elif action == "Leave":
            actions.append(f"{user_dict[uid]}님이 나갔습니다.")
    
    return actions