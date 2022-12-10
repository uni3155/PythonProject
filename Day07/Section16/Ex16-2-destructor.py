'''
    소멸자
        인스턴스가 소멸될때 자동으로 호출된다.
'''
class Service:
    def __init__(self, service=None):  # default 값 넣을 수 있다.
        self.service = service
        print('{} Service가 시작 되었습니다.'.format(self.service))

    def __del__(self):
        print('{} Service가 종료 되었습니다.'.format(self.service))

s = Service('길 안내')
del s

s2 = Service()

print("프로그램 종료!")
