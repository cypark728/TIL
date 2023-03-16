#입력 값을 변수에 저장하기

#input 함수로 변수에 입력 저장하기
x = input("아무거나 입력하시오")
print(x)

#입력된 두 수 합치기
a = input("첫번째 숫자 입력")
b = input("두번쨰 숫자 입력")
print(a + b)

#입력된 값을 원하는 자료형으로 바꾸기
a = int(input("첫번쨰 숫자 입력"))
b = int(input("두번째 숫자 입력"))
print(a + b)

#한번에 2개의 문자열 입력받기
a, b = input("문자열 두 개를 입력하세요 : ").split()
print(a)
print(b)

#한번에 2개의 정수 입력받기
a, b = map(int, input("숫자 두 개를 입력하세요 : ").split())
print(a + b)

#기준을 토대로 나눠서 입력 받기
a, b = map(int, input("숫자 두 개를 , 로 나눠서 입력받기").split(',')) #10,20 입력 받기
print(a + b)
