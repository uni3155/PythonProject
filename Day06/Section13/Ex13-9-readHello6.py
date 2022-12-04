import sys  # 운영체제 관련된 정보를 가지고 있는 모듈

with open('hello.txt', 'rt', encoding='UTF-8') as file:
    line_list = file.readlines()
    sys.stdout.writelines(line_list)
    # standardout => console 에 쓰겠다.

    