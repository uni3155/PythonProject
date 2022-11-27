'''
    while
        특정 조건을 만족하는 동안 반복해서 수행하는 코드
    while 조건식:
        반복 실행코드
'''
# n = 10
# while n >= 1:
#     print(n)
#     n -= 1

def autoDoor(isPerson):
    time = 10
    while isPerson:
        print("문이 열려요")
        if time < 1:
            break
        time -= 1
    print("문이 닫혀요")
autoDoor(True)

