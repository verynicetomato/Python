# LEVEL0: 문자열 정렬하기
def solution(my_string):
    answer = "".join(sorted(my_string.lower()))
    return answer

# 출력문 예시
print(solution("Bcad"))
print(solution("heLLo"))
print(solution("Python"))