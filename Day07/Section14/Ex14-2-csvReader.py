'''
CSV(comma-seperated values)
필드를 쉼표(,)로 구분한 텍스트 데이터 파일이다.
'''
student_list = []
with open('학생명단.csv', 'rt', encoding='UTF-8') as file:
    file.readline() # 첫줄 제거
    while True:
        line = file.readline()
        if not line:
            break
        '''
        [
        ['10101', '김승별', '서울시 영등포구', '010-1111-1111\n']
        ['10102', '박나라', '서울시 여의도구', '010-2222-2222\n']
        ['10103', '최대욱', '서울시 강남구', '010-3333-3333\n']
        ['10104', '민기홍', '인천시 계양구', '010-4444-4444\n']
        ['10105', '이명숙', '경기도 과천시', '010-5555-5555\n']
        ]
        '''
        student = line.split(',')   # ','기준구분 => 리스트로 반환
        student_list.append(student)    #리스트 안에 리스트 추가
print(student_list)
