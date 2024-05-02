# LEVEL1 : 짝수와 홀수
def solution(num):
    if num % 2 == 0:
        answer = "Even"
    else:
        answer = "Odd"
    return answer

# 출력문 예시
print(solution(3))
print(solution(4))