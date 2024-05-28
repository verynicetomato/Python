# LEVEL0: 문자열 정렬하기1
def solution(my_string):
    answer = []
    for i in my_string:
        if i.isdigit():
            answer.append(int(i))
    return sorted(answer)

# 출력문 예시
print(solution("hi12392"))
print(solution("p2o4i8gj2"))
print(solution("abcde0"))