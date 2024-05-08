# LEVEL0: 원하는 문자열 찾기
def solution(myString, pat):
    answer = 0
    if pat.lower() in myString.lower():
        answer = 1
    return answer

# 출력문 예시
print(solution("AbCdEfG", "aBc"))
print(solution("aaAA", "aaaaa"))