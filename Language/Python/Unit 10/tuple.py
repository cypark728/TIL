#튜플
#저장된 요소를 변경, 추가, 삭제를 할 수 없는 읽기 전용 리스트이다.

#튜플 만들기
a = (1,2,3,4,5)
print(a)

b = 1,2,3,4,5
print(b)

#튜플도 리스트와 같이 여러 자료형을 섞어 사용 가능하다. 
c = (158.0, "INE", 30, True)
print(c)

#요소가 한 개 들어있는 튜플
d = (38,) #콤마 없이 그냥 괄호에 요소를 넣으면 아무것도 아닌 값이 된다.
print(d)

#range함수로 튜플 만들기
e = tuple(range(10))
print(e)

#tutpe to list, list to tuple
f = [1, 2, 3]
print(tuple(f))

g = {1, 2, 3}
print(list(g))
