'''
    [회원가입]
        아이디를 입력하세요.(3글자 이상) >>>
        >3글자 이상 입력해 주세요!

        아이디를 입력하세요.(3글자 이상) >>>

        패스워드를 입력하세요.(영문,숫자 포함 8자이상) >>>
        >영문,숫자 포함 8자이상 입력해 주세요!

        패스워드 확인 한번 더 입력하세요 >>>
        >일치하지 않습니다! 다시 입력해 주세요!

        패스워드를 입력하세요.(영문,숫자 포함 8자이상) >>>

        패스워드 확인 한번 더 입력하세요 >>>

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
while True:#틀리면 계속 실행
    id = input('아이디를 입력하세요.(3글자 이상) >>>')
    id_count = len(id)
    if id_count >= 3:
        pwd = input('패스워드를 입력하세요.(영문,숫자 포함 8자이상) >>>')
        ch_count = 0
        num_count = 0
        for ch in pwd:
            if ch.isalpha():
                ch_count += 1
            elif ch.isnumeric():
                num_count += 1
        if ch_count > 0 and num_count > 0 and len(pwd) >= 8:
            check = input('패스워드 다시한번 입력하세요 >>>')
            if pwd == check:
                print('회원가입 완료!!')
                login(True)
                break
            else:
                print('일치하지 않습니다! 다시 입력해 주세요!')
        else:
            print('패스워드는 영문,숫자 포함 8자이상 입력해 주세요!')
    else:
        print('아이디를 3글자 이상 입력하세요.')
    def login(member):
        while member:
            login_id = input('아이디를 입력하세요.>>>')
            if login_id == id:
                login_pw = input('패스워드를 입력하세요.>>>')
                if login_pw == pwd:
                    print("로그인 성공!\n"+id+"님,반갑습니다:)")
                    break
                else:
                    print('패스워드가 일치하지 않습니다.')
            else:
                print('아이디가 일치하지 않습니다.')

