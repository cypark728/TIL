#리스트

#리스트 만들기
a = [24, 26, 27, 28, 29, 30]
print(a)

#리스트에 여러 자료형 저장하기
a = [30, "INE", 158.0, True]
print(a)

#빈 리스트 만들기
b = []
print(b)
c = list()
print(c)

#range를 이용하여 리스트 채우기
a = list(range(10)) #0에서 시작해서 10개의 숫자 넣기(기본은 1씩 증가)
print(a)

b = list(range(5, 12)) #5부터 시작해서 12 - 1까지 넣기
print(b)

c = list(range(-4, 10, 2)) #-4부터 10전까지 2씩 증가하면서 리스트 만들기
print(c)