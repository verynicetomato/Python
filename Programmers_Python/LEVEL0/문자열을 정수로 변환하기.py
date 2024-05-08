# LEVEL0: 문자열을 정수로 변환하기
def solution(rny_string):
    answer = rny_string.replace("m", "rn")
    return answer

# 출력문 예시
print(solution("10"))
print(solution("8542"))