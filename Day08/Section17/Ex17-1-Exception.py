'''
예외
    프로그램 존재하는 오류 비슷하지만
    개발자가 직접처리 할 수 있는 문제를 예외라고 한다.
    
'''
# 고전적인 예외처리
a = int(input('제수를 입력하세요>>>'))  # 10
b = int(input('피제수를 입력하세요>>>')) # 0
# ZeroDivisionError: division by zero
if b == 0:
    print('> 0으로 나누는 것은 불가능합니다.')
else:
    print('{} / {} = {}'.format(a, b, a / b))

