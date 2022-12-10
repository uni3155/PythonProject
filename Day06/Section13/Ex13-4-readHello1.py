'''
    encoding문제 : 깨짐현상 - 생각보다 많이 생겨요.
    Error를 공부할때 많이 내보는게 좋습니다 -그래야 나중에 일할때 안나겠죠.

    r(read mode) : 읽기 전용모드 / 파일 없으면 에러남

    절대경로 예)    C:\pstudy\PythonProject
    상대경로 예)    ../test/hello.txt
                    ..  상위폴더
                    .   현재폴더
'''
file = open('..//test//hello.txt', 'rt', encoding='UTF-8')
str = file.read()
print(str, end='')
file.close()

with open('hello.txt', 'rt', encoding='UTF-8') as file:
    str = file.read()
    print(str, end='')
    