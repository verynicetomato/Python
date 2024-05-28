# LEVEL0: 문자열 뒤집기
def solution(my_string):
    answer = ''
    for i in range(len(my_string) - 1 , -1, -1):
        answer += my_string[i]
    return answer

# 출력문 예시
print(solution("jaron"))
print(solution("bread"))
