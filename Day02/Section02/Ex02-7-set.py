'''
    set
    중복값 없음
    순서가 없다
    변경할 수 없다
    인덱싱 되지 않는 컬렉션
'''
thisset = {"피카츄", "라이츄", "파이리"}
# 실행할 때마다 순서가 변경
print(thisset)

# 항목 가져오기
for x in thisset:
    print(x)
    
# 값이 있는지 확인
thisset = {"피카츄", "라이츄", "파이리"}
print("피카츄" in thisset)
print("꼬부기" in thisset)

# 항목 추가하기
thisset.add("꼬부기")
print(thisset)

# 다른 Set 항목추가
thisset1 = {"피카츄", "라이츄", "파이리"}
thisset2 = {"꼬부기", "잠만보", "뮤츠"}
thisset1.update(thisset2)
print(thisset1)

# 항목제거
thisset = {"피카츄", "라이츄", "파이리"}
thisset.remove("피카츄")
print(thisset)
# 똑같은 내용 여러번 제거=>Error 난다.
# thisset.remove("피카츄")
# print(thisset)

# 항목제거(무작위)
thisset.pop()

# 비우기
thisset.clear()