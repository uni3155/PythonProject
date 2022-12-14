'''
[회원가입]
    아이디를 입력하세요.(3글자 이상) >>>
    >아이디를 3글자 이상 입력해 주세요!

    아이디를 입력하세요.(3글자 이상) >>>

    패스워드를 입력하세요.(영문,숫자 포함 8자이상) >>>
    >영문,숫자 포함 8자이상 입력해 주세요!

    패스워드를 다시 한번 입력하세요 >>>
    >패스워드가 일치하지 않습니다!

    패스워드를 입력하세요.(영문,숫자 포함 8자이상) >>>
    >패스워드 다시 한번 입력하세요 >>>

    회원가입 완료!!

[로그인]
    아이디를 입력하세요 >>>
    >아이디가 일치하지 않습니다.

    아이디를 입력하세요 >>>

    패스워드를 입력하세요 >>>
    >패스워드가 일치하지 않습니다.

    패스워드를 입력하세요 >>>

    로그인 성공!!
    ooo님 환영합니다 :)
'''
def login(member):
    while member:
        login_id = input('아이디를 입력해 주세요.>>>')
        if id == login_id:
            while True: #패스워드 불일치시 패스워드 다시입력
                login_pw = input('패스워드를 입력해 주세요.>>>')
                if pwd == login_pw:
                    print("> 로그인 성공!\n" + id + "님,환영합니다:)")
                    break
                else:
                    print('> 패스워드가 일치하지 않습니다.')
            break   #종료후 아이디로 튀는 문제해결
        else:
            print('> 아이디가 일치하지 않습니다.')

while True: # 틀리면 무한반복
    id = input('아이디를 입력하세요.(3글자 이상) >>>')
    id_count = len(id)
    if id_count >= 3:
        while True:  # 패스워드 불일치시 패스워드 다시입력
            pwd = input('패스워드를 입력하세요.(영문,숫자 포함 8자이상) >>>')
            ch_count = 0
            num_count = 0
            for ch in pwd:
                if ch.isalpha():
                    ch_count += 1
                elif ch.isnumeric():
                    num_count += 1
            if ch_count > 0 and num_count > 0 and len(pwd) >= 8:
                check = input('패스워드를 다시한번 입력하세요 >>>')
                if pwd == check:
                    print('> 회원가입 완료!!')
                    login(True)
                    break
                else:
                    print('> 패스워드가 일치하지 않습니다.')
            else:
                print('> 영문,숫자 포함 8자이상 입력해 주세요!')
        break   #종료후 아이디로 튀는 문제해결
    else:
        print('> 3글자 이상 입력하세요.')

