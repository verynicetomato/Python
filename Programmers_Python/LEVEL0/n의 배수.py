# LEVEL0: n의 배수
def solution(num, n):
    answer = 0
    if num % n == 0:
            answer = 1
    return answer

# 출력문 예시
print(solution(98, 2))
print(solution(34, 3))