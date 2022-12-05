def get_average(marks):
    total = 0
    for subject in marks:
        #1.subject: 국어
        #2.subject: 영어
        #3.subject: 수학
        total += marks[subject]
        #1. total+=mark['국어']
        #total 값 90
        #2. total+=mark['영어']
        #total 값 170
        #3. total+=mark['수학']
        #total 값 255
    l_average = total/len(marks)
        #l_average = 255/3
    return l_average
marks = {'국어': 90, '영어': 80, '수학':85}
average = get_average(marks)
print('평균은 {}점 입니다.'.format(average))
