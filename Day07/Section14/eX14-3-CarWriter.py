'''
인코딩(Encoding):
    문자 => 바이너리로 (0과 1)변환
    컴퓨터가 읽을 수 있는 바이너리로 변환
    암호학 - 암호화
    
디코딩(Decoding):
    바이너리 => 문자로 변환
    암호학 - 복호화
'''
import csv
# 첫번째 방법
with open('차량관리.csv', 'w', encoding='UTF-8') as file:
    csv_maker = csv.writer(file, delimiter=',')
    csv_maker.writerow([1, '08러 1234', '2020-10-20,14:00'])
    csv_maker.writerow([2, '25러 1234', '2020-10-20,14:10'])
    csv_maker.writerow([3, '28러 1234', '2020-10-20,14:20'])
print('차량관리.csv 파일이 생성되었습니다.')
# 두번째 방법
with open('차량관리.csv', 'w', newline='', encoding='UTF-8') as file:
    csv_maker = csv.writer(file, delimiter=',')# default '"'
    csv_maker.writerow([1, '08러 1234', '2020-10-20,14:00'])
    csv_maker.writerow([2, '25러 1234', '2020-10-20,14:10'])
    csv_maker.writerow([3, '28러 1234', '2020-10-20,14:20'])
print('차량관리.csv 파일이 생성되었습니다.')
# 마지막 방법========================================================
with open('차량관리.csv', 'w', newline='', encoding='UTF-8') as file:
    csv_maker = csv.writer(file, delimiter=',', quotechar='"')
    csv_maker.writerow([1, '08러 1234', '2020-10-20,14:00'])
    csv_maker.writerow([2, '25러 1234', '2020-10-20,14:10'])
    csv_maker.writerow([3, '28러 1234', '2020-10-20,14:20'])
print('차량관리.csv 파일이 생성되었습니다.')
