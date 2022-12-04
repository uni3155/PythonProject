file = open('hello.txt', 'rt', encoding='UTF-8')

while True:
    str = file.read(5)
    # print(str)
    '''
        안녕하세요
        .
        반갑습
        니다.
        H
        ello
        
        Nice 
        to me
        et yo
        u
    '''
    if not str:  #읽을 값이 없으면 True
        break
    print(str, end='')
    '''
        안녕하세요.
        반갑습니다.
        Hello
        Nice to meet you
    '''

file.close()
