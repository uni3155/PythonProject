'''
    print() 함수 사용법
        sep : 출력할 value의 구분문자
        end : value 출력 후 출력할 문자 (기본값 '\n')
        file : 출력 방향 지정
'''
print("재미있는", "파이썬")
print("Python", "Java", "C", sep=",")

print("안녕", end='\n')
print("하세요")
#▲▲▲▲▲▲default▲▲▲▲▲▲
print("안녕", end='')
print("하세요")

# 메모리에 임시저장
fos = open('sample.py', mode='wt')
print('print("Hello World")', file=fos)
fos.close()



