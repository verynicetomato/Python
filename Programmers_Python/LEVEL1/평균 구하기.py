# LEVEL1 : 평균 구하기
def solution(arr):
    answer = 0
    for i in arr:
        answer += i
    answer /= len(arr)
    return answer

# 출력문 예시
print(solution([1, 2, 3, 4]))
print(solution([5, 5]))