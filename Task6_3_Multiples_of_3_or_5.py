def solution(number):
    sum_result = 0
    for num in range(number):
        if num % 3 == 0 or num % 5 == 0:
            sum_result += num
    return sum_result