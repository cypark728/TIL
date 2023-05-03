a = input()
b = a.replace('+', '-')
temp = list(map(int, b.split('-')))
result_list = []
result_list.append(temp[0])
index = 1
for i in a:
    if i == '-':
        result_list.append(temp[index])
        index += 1
    elif i == '+':
        result_list[len(result_list) - 1] += temp[index]
        index += 1
result = result_list[0]
for j in range(1, len(result_list)):
    result -= result_list[j]
print(result)
