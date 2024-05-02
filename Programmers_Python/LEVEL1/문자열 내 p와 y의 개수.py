# LEVEL1: 문자열 내 p와 y의 개수
def solution(s):
    s_lower = s.lower()
    if s_lower.count("p") == s_lower.count("y"):
        answer = True
    else:
        answer = False
    return answer

# 출력문 예시
print(solution("pPoooyY"))
print(solution("Pyy"))