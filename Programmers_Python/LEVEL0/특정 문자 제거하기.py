# LEVEL0: 특정 문자 제거하기
def solution(my_string, letter):
    answer = my_string.replace(letter, "")
    return answer

# 출력문 예시
print(solution("abcdef", "f"))
print(solution("BCBdbe", "B"))