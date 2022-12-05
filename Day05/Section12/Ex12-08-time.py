'''
time 모듈
    시간처리에 관련된 time 모듈
'''
import time

# 1970년 1월 1일 0시 0분 0초부터 현재까지 경과한 시간을 반환
# 마이크로초
print(time.time())  # epoch converter

# ctime() 함수 - 인수로 전달된 시간을 time 시간형식을 갖춰 반환
print(time.ctime(time.time()))

#인수로 전달된 날짜와 지시자를 이용하여 형식을 갖춘
#날짜 데이터를 문자열로 반환
# print(time.strftime('%Y-%m-%d %H:%M:%S'))

# 한글로 하려면 ... (무조건 영어로 쓰세요!!)
print('%년 %월 %일'.encode('unicode-escape').decode())

print(
    time.strftime(
        '%년 %월 %일'
        .encode('unicode-escape')
        .decode()
    ).encode().decode('unicode-escape')
)

# 인자 초만큼 시스템 일시중지
time.sleep(1)

sec = 1
while True:
    print(sec)
    if sec == 10:
        break
    time.sleep(1)
    sec += 1

