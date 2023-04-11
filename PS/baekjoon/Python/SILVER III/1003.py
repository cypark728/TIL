zero = [1, 0, 1]
one = [0, 1, 1]

def fibonacci(a):
    length = len(zero)
    if(a >= length):
        for j in range(length, a + 1):
            zero.append(zero[j - 2] + zero[j - 1])
            one.append(one[j - 2] + one[j - 1])
    print("{} {}".format(zero[a], one[a]))



n = int(input())
for i in range(n):
    temp = int(input())
    fibonacci(temp)