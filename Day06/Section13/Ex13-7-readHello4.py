with open('hello.txt', 'rt', encoding='UTF-8') as file:
    line_list = file.readlines()
    print(line_list)
    #['안녕하세요.\n', '반갑습니다.\n', 'Hello\n', 'Nice to meet you\n']
    for line in line_list:
        print(line, end='')

