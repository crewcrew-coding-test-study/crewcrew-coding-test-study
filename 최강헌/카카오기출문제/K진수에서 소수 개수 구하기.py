import math


def check(num):
    if num == 2:
        return True
    if num == 1 or num % 2 == 0:
        return False
    # 3,5,7
    for i in range(3, int(math.sqrt(num)) + 1, 2):
        if num % i == 0:
            return False
    return True


def convert(num, base):
    q, r = divmod(num, base)
    if q:
        return convert(q, base) + str(r)
    else:
        return str(r)


def solution(n, k):
    # 10 진수 일떄는 굳이 할필요가 없다
    numstr = str(n) if k == 10 else convert(n, k)
    # 0이 연속될수있음
    nums = numstr.split('0')

    answer = 0

    for value in nums:
        if len(value) and check(int(value)):
            answer += 1
    return answer