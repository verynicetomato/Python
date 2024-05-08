# LEVEL0: 문자열 앞의 n글자
def solution(my_string, n):
    answer = my_string[:n]
    return answer

# 출력문 예시
print(solution("ProgrammerS123", 11))
print(solution("He110W0r1d", 5))