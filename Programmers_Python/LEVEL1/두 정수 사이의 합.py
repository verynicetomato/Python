# LEVEL1: 두 정수 사이의 합
def solution(a, b):
    answer = 0
    if a > b:
        a, b = b, a
    for i in range(a, b + 1):
        answer += i
    return answer

# 출력문 예시
print(solution(3, 5))
print(solution(3, 3))
print(solution(5, 3))