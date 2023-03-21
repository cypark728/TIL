#구름이의 취미
#https://level.goorm.io/exam/49094/%ED%83%9C%EB%AF%BC%EC%9D%B4%EC%9D%98-%EC%B7%A8%EB%AF%B8/quiz/1

user_input = int(input())

result = int((user_input * (user_input + 1)//2) ** 2)

print(result % 1000000007)