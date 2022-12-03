'''
    메소드(method):
        특정 객체가 가지고 있는 함수를 의미한다.
        객체.메소드() 사용가능
'''
# String 객체 format 메소드
print("10자리 폭 왼쪽정렬 '{:<10d}'".format(123))
print("10자리 폭 오른쪽정렬 '{:>10d}'".format(123))
print("10자리 폭 가운데정렬 '{:^10d}'".format(123))
print()
print("10자리 폭 왼쪽정렬 채움문자 {:*<10d}".format(123))
print("10자리 폭 오른쪽정렬 채움문자 {:*>10d}".format(123))
print("10자리 폭 가운데정렬 채움문자 {:*^10d}".format(123))

# count() 메소드
s = '내가 그린 기린 그림은 목이 긴 기린 그림이고,네가 그린 기린 그림은 목 짧은 기린 그림이다.'
result = s.count('기린')
print(result)

s = 'best of best'
result = s.count('best', 5)
print(result)
result = s.count('best', -7)
print(result)

# find() 메소드 위치한 첫번째 인덱스 번호 반환
s = 'apple'
result = s.find('p')
print(result)

s = 'apple'
result = s.find('z')
if result == -1:    # 없는값 find -1
    print('존재하지 않는 문자 입니다.')

s = 'best of best'
result = s.find('best', 5)
print(result)
result = s.find('best', -7)
print(result)

s = 'apple'
result = s.index('p')
print(result)
result = s.index('z')
print(result)
# 존재하지 않는 문자입니다.
# index() & find() 메소드와 같지만
# 문자열이 존재하지 않을 경우 에러발생!


