j = input().rstrip().lstrip()
arr = list(j)
arr = list(map(int,arr))
arr.sort(reverse=True)
s = sum(arr)
c = []
tmp = s % 3
if s % 3 == 0:
    print(*arr,sep="")
else:
    if tmp == 1:
        arr1 = []
        arr2 = []
        for i in arr:
            if i % 3 == 1:
                arr1.append(i)
            if i % 3 == 2:
                arr2.append(i)
        if len(arr1) != 0:
            if (s - min(arr1)) % 3 ==0:
                arr.pop(arr.index((min(arr1))))
        else:
            for i in arr2:
                arr.pop(arr.index(i))
    if tmp == 2:
        arr1 = []
        arr2 = []
        for i in arr:
            if i % 3 == 1:
                arr1.append(i)
            if i % 3 == 2:
                arr2.append(i)
        if len(arr2) != 0:
            if (s - min(arr2))%3 == 0:
                arr.pop(arr.index((min(arr2))))
        else:
            for i in arr1:
                arr.pop(arr.index(i))
    print(*arr,sep="")
