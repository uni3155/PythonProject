with open('hello.txt', 'rt', encoding='UTF-8') as file:
    line_list = file.readlines()
    for no, line in enumerate(line_list):
        print('{} {}'.format(no+1, line), end='')
        '''
            1 안녕하세요.
            2 반갑습니다.
            3 Hello
            4 Nice to meet you
        '''
