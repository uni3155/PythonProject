'''
파일 입출력(I/O - input/output)
    입 력(input) : 기존파일 읽어들이는 것
    출 력(output) : 파일생성, 내용추가를 말한다.
'''
file = open('myFile.txt', 'wt')
print('myFile.txt 파일이 생성 되었습니다.')
file.close()
# with문 - 자동으로 close()를 해준다.
with open('myFile.txt', 'wt') as file:
    print('myFile.txt 파일이 생성 되었습니다.')
