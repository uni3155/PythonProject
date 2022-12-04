'''
패키지
    모듈 상위 개념
    모듈의 집합을 의미한다

패키지 설치
    console > pip instal package 명
패키지 삭제
    console > pip uninstal package 명
'''
import numpy as np  # 행렬기반 패키지

print(np.sum([1, 2, 3, 4, 5]))

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

# 각 요소 더하기
c = a + b
c = np.add(a, b)
print(c)

# 각 요소 빼기
c = a - b
c = np.substract(a, b)
print(c)

# 각 요소 곱하기
c = a * b
c = np.multiply(a, b)
print(c)

# 각 요소 나누기
c = a / b
c = np.divide(a, b)
print(c)
