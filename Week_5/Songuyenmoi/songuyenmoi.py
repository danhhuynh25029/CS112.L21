n = input().strip()
length = len(n)
n = int(n)
arr = []
for i in range(length):
    t = n%10
    arr.append(t)
    n = n//10
arr = arr[::-1]
i = 9
j = 0
def reduce(arr):
    i = 9
    j = length -1
    while i > 0:
        if arr[j] > i and (sum(arr) - arr[j] + i) % 3 == 0:
            arr[j] = i
            print(*arr,sep="")
            break
        if i == 1:
            if j > 1:
                print(j)
                j -= 1
            i = 9
            continue
        i -= 1

while i > 0:
    if arr[j] < i and (sum(arr) - arr[j] + i) % 3 == 0:
        arr[j] = i
        print(*arr,sep="")
        break
    if i == 1:
        if j == length - 1:
            reduce(arr)
            break
        if j < length-1:
            j += 1
        i = 9
        continue
    i -= 1