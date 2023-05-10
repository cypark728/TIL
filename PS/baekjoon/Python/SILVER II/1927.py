import sys
input = sys.stdin.readline

N = int(input())

arr = [0]

for i in range(N):
    a = int(input())
    if a == 0:
        # delete
        if len(arr) == 1:
            print(0)
        elif len(arr) == 2 or len(arr) == 3:
            print(arr[1])
            del arr[1]
        else:
            print(arr[1])
            arr[1], arr[len(arr) - 1] = arr[len(arr) - 1], arr[1]
            del arr[len(arr) - 1]
            idx = 1
            while True:
                if len(arr) == idx * 2 + 1:
                    if arr[idx] < arr[idx * 2]:
                        break
                    else:
                        arr[idx], arr[idx * 2] = arr[idx * 2], arr[idx]
                        idx = idx * 2
                else:
                    if (arr[idx] < arr[idx*2]) and (arr[idx] < arr[idx*2+1]):
                        break
                    elif arr[idx * 2] < arr[idx * 2 + 1]:
                        arr[idx], arr[idx * 2] = arr[idx * 2], arr[idx]
                        idx = idx * 2
                    else:
                        arr[idx], arr[idx * 2 + 1] = arr[idx * 2 + 1], arr[idx]
                        idx = idx * 2 + 1

                if idx * 2 >= len(arr):
                    break

    else:
        # add
        idx = len(arr)
        arr.append(a)
        while True:
            if arr[idx//2] > arr[idx]:
                arr[idx//2], arr[idx] = arr[idx], arr[idx//2]
                idx = idx//2
            else:
                break
            if idx == 1:
                break
