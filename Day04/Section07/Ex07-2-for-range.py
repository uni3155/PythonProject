'''
    for문과 range
'''
dan = int(input('출력할 구구단을 입력하세요.>>>'))

for n in range(10):     # 0~9 range(stop)
    print('{} x {} = {}'.format(dan, n, dan*n))
print('\n')
for n in range(1, 10):  # 1~9 range(start,stop)
    print('{} x {} = {}'.format(dan, n, dan*n))
print('\n')
for n in range(1, 10, 2):   # start,stop,step
    print('{} x {} = {}'.format(dan, n, dan*n))
