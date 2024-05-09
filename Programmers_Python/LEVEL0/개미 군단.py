# LEVEL0: 개미 군단
def solution(hp):
    answer = (hp // 5) + ((hp % 5) // 3) + ((hp % 5) % 3)
    return answer

# 출력문 예시
print(solution(23))
print(solution(24))
print(solution(999))