def solution(m, n, puddles):

    # 문제 에서 요구하는 물 웅덩이 2, 2는 0, 0 부터 시작하는 배열을 의미하지 않음.
    # 인덱스 에러를 방지하기 위해서 Sync 맞추기 위해서 맵 초기화
    map = [[0] * (m+1) for _ in range(n+1)]

    # print(map)

    # 초기값(집) 지정
    map[1][1] = 1
    # print(map)

    # 아래 방향으로 이동
    for i in range(1, n + 1):
        # 오른쪽으로 이동
        for j in range(1, m + 1) :

            # 집의 위치 무시
            if i == 1 and j == 1:
                continue

            # 이동 중, 웅덩이를 만나는 경우
            if [j, i] in puddles:
                map[i][j] = 0
            else:
                map[i][j] = map[i-1][j] + map[i][j-1]

            print('i : {}, j : {}, map[i][j] = {}'.format(i, j, map[i][j]))

    for xy in map:
        print(xy)

    return map[n][m] % 1000000007

print(solution(4, 3, [[2, 2]]))

"""
- 문제풀이 및 접근 방법
    - M : 행, N : 열, puddle : 물 웅덩이
    - puddle의 파라미터 값이 일반적으로 생각하고 있는 0,0 부터 시작하는 배열의 주소를 의미하지 않음.

"""

"""
0 0 0 0 0 
0 S 0 0 0
0 0 * 0 0
0 0 0 0 E
"""

"""
m = 4, n = 3 
(0,0) (0,1) (0,2) (0,3)
(1,0) (1,1) (1,2) (1,3)
(2,0) (2,1) (2,2) (2,3)

(1,1) (1,2) (1,3) (1,4)
(2,1) (2,2) (2,3) (2,4)
(3,1) (3,2) (3,3) (3,4)

(1,1) (1,2) (1,3) (1,4)
(2,1) (2,2) (2,3) (2,4)
(3,1) (3,2) (3,3) (3,4)

(0,0) (0,1) (0,2) (0,3) (0,4)
(1,0) (1,1) (1,2) (1,3) (1,4)
(2,0) (2,1) (2,2) (2,3) (2,4)
(3,0) (3,1) (3,2) (3,3) (3,4)
"""