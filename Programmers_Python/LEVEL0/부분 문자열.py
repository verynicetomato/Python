# LEVEL0: 부분 문자열
def solution(str1, str2):
    answer = 0
    if str1 in str2:
        answer = 1
    return answer

# 출력문 예시
print(solution("abc", "aabcc"))
print(solution("tbt", "tbbttb"))
