# LEVEL0: 짝수 홀수 개수
def solution(num_list):
    answer = [0, 0]
    for i in num_list:
        if i % 2 == 0:
            answer[0] += 1
        else: 
            answer[1] += 1
    return answer

# 출력문 예시
print(solution([1, 2, 3, 4, 5]))
print(solution([1, 3, 5, 7]))
