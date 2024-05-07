# LEVEL0: 문자열 정수의 합
def solution(num_str):
    answer = 0
    for i in num_str:
        answer += int(i)
    return answer

# 출력문 예시
print(solution("123456789"))
print(solution("1000000"))