n = int(input())
arr = input()
arr = list(map(int,arr.split()))
result = 0
max_s  = 0
begin,end = 0,0
location = []
sum_arr = []
test = False
for i in arr:
    if i  > 0:
        test = True
if test == False:
    if sum(arr) < 0:
        min_s = max(arr)
        location.append(arr.index(min_s))
        location.append(arr.index(min_s))
        print(location[0]+1,location[1]+1,min_s)
else:
    for i in range(0,len(arr)):
        if max_s + arr[i] < 0:
            result = 0
            max_s = 0
            begin = i+1
            continue
        max_s += arr[i]
        if max_s > result:
            result = max_s
            end = i
            location.append(begin)
            location.append(end)
            sum_arr.append(result)
    i = 0
    j = 0 
    result = max(sum_arr)
    while i < len(sum_arr):
        if sum_arr[i] == result:
            if location[j] < begin and location[j+1] < end:
                begin = location[j]
                end = location[j+1]
        j += 2  
        i += 1
    print(begin+1,end+1,result)