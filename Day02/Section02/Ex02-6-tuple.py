''''
    tuple:

'''
thistuple = ("피카츄", "라이츄", "파이리")
print(thistuple)
# 튜플 길이 변경
print(thistuple[1:3])
print(thistuple[1:3])
print(thistuple[1:3])

# 튜플값 변경방법
thistuple = ("피카츄", "라이츄", "파이리")
thiscast = list(thistuple)
thiscast[1] = "잠만보"
thistuple = tuple(thiscast)
print(thistuple)

#튜플 압축풀기
thistuple = ("피카츄", "라이츄", "꼬부기")
(p1, p2, p3, p4) = thistuple
print(type(1))
print(2)
print(3)
print(4)

# 두개 튜플 조인
thistuple1 = ("피카츄", "라이츄", "파이리", "꼬부기")
thistuple2 = ("버터플", "야도란", "피존투", "또가스")
thistuple3 = thistuple1 + thistuple2
print(thistuple3)
