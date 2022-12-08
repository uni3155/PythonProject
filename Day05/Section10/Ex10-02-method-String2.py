# join() 메소드
s = '-'.join('python')
print(s)

s = ''.join(['a', 'b', 'c', 'd', 'd', 'e'])
print(s)

# split() 메소드
s = 'Life is too short'
result = s.split()
print(result)

s = '010-1234-5678'
result = s.split('-')
print(result)

name = '김태호|39|프로그래머'
result = s.split('|')
print(result)
print('이름 : {}'.format(result[0]))

# replace()
s = 'Life is too short'
result = s.replace('short', 'long')
print(result)

# strip(), lstrip(), rstrip() 공백제거
s = '       apple'
print(s)
result = s.lstrip()  # 왼쪽 공백제거
print(result)

s = 'apple       '
print(s)
result = s.rstrip()  # 오른쪽 공백제거
print(result)

s = '      apple      '
print(s)
result = s.strip()  # 양쪽 공백제거
print(result)

# 전체 공백제거
s = ' a p p l e '
print(s)  # 그대로

start_end = s.strip()
print(start_end)  # 앞뒤제거

all = s.replace(' ', '')
print(all)  # 모두제거

# 교집합 intersection()
s1 = {'apple', 'banana', 'cherry'}
s2 = {'apple', 'banana', 'orange'}
print(s1 & s2)

result = s1.intersection(s2)
print(result)

# 합집합
s1 = {'banana', 'apple', 'cherry'}
s2 = {'banana', 'apple', 'orange'}
print(s1 | s2)

plus = s1.union(s2)
print(plus)

# 차집합
s1 = {'banana', 'apple', 'cherry'}
s2 = {'banana', 'apple', 'orange'}
print(s1 - s2)

minus = s1.difference(s2)
print(minus)

