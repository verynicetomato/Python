# LEVEL0: 가위 바위 보
def solution(rsp):
    answer = ''
    for i in rsp:
        if i == "2":
            answer += "0"
        elif i == "0":
            answer += "5"
        elif i == "5":
            answer += "2"
    return answer

# 출력문 예시
print(solution("2"))
print(solution("205"))