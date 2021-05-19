a = int(input())
b = int(input())
c = int(input())
d = int(input())
def gcd(a,b):
    if b == 0 :
        return a
    else:
        return gcd(b,a%b)
def find(a,b,c,d):
    return (b*c - a*d)/(d-c)
tmp = int(find(a,b,c,d))
if tmp >= 0:
    for i in range(1,(tmp)+1):
        a +=1
        b += 1
        ucln = gcd(a,b)
        a = a//ucln
        b = b//ucln
        if a == c and b == d:
            print(i)
            break
        tmp -= 1
    if tmp == 0:
        print(0)
else:
    print(0)
