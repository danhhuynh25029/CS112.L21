def solve(a,n):
    a.sort(reverse=True)
    for i in range(n):
        if a[i]< i+1:
            return i
    else:
        return n

n = int(input())
a = list(map(int,input().split()))
print(solve(a,n))
