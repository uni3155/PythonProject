'''
    5. 비트 연산자
        어떤 변수의 값을 0과 1의 조합인 2진수,
        즉 비트로 변환한 뒤에 비트단위로 연산 수행

    1. &(AND) : 입력이 모두 1이면 1, 아니면 0
    2. |(OR) : 입력중 하나라도 1이면  1, 아니면 0
    3. ^(XOR) : 입력이 서로 다르면 1, 아니면 0
    4. ~(NOT) : 입력이 0이면 1, 입력이 1이면 0
    5. <<(왼쪽 SHIFT) : 비트 단위로 왼쪽으로 N비트 이동하며 2의 N 거듭제곱 만큼 곱셈
    6. >>(오른쪽 SHIFT) : 비트 단위로 오른쪽으로 N비트 이동하며 2의 N 거듭제곱 만큼 나눗셈
'''
a = 3   # 0011
b = 5   # 0101
print('a & b : {}'.format(a & b))   # 0001
print('a | b : {}'.format(a | b))   # 0111
print('a ^ b : {}'.format(a ^ b))   # 0110
print('~ a : {}'.format(~ a))   # (-/1)100
