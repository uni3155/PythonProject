'''
추상메소드(Abstract Method)
    선언만하고 구현되지 않은 미완성 메소드

추상클래스(Abstract Class)
    추상메소드를 하나이상 가지고 있는 클래스

오버라아딩
    슈퍼클래스 메소드 재정의
'''
from abc import *

class Family(metaclass=ABCMeta):
    @abstractmethod
    def introduce(self):
        pass

class Person(Family):
    def introduce(self):
        print('저는 사람입니다.')

a = Person()
a.introduce()

