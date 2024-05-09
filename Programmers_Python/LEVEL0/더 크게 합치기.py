# LEVEL0: 더 크게 합치기
def solution(a, b):
    answer = max(str(a) + str(b), str(b) + str(a))
    return int(answer)

# 출력문 예시
print(solution(9, 91))
print(solution(89, 8))