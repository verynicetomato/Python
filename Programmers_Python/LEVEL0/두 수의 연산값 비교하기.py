# LEVEL0: 두 수의 연산값 비교하기
def solution(a, b):
    answer = 0
    if int(str(a) + str(b)) >= 2 * a * b:
        answer = int(str(a) + str(b))
    else:
        answer = 2 * a * b
    return answer

# 출력문 예시
print(solution(2, 91))
print(solution(91, 2))