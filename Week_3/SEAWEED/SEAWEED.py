mod = int(1e9+7)

def mul(a,b):
    global mod    
    x = a[0][0]*b[0][0]+a[0][1]*b[1][0]
    y = a[0][0]*b[0][1]+a[0][1]*b[1][1]
    z = a[1][0]*b[0][0]+a[1][1]*b[1][0]
    t = a[1][0]*b[0][1]+a[1][1]*b[1][1]
    return [[x,y],[z,t]] 


def pow(a,n):
    if n == 1:
        return a
    elif n%2 == 0:
        t = pow(a,n/2)
        return mul(t,t)
    else:
        t = pow( a , ( n - 1 ) / 2)
        
        return mul( mul( t , t ) , a)


def solve():
    global mod
    n,k = map( int, input().split())
    res = pow( [[1,1],[1,0]], k*2)
    print ((res[0][0]*n) % mod)

solve()