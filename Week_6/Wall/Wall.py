n = int(input())
hangrao = list(map(int,input().split()))
m = int(input())
gothua = list(map(int,input().split()))
l = min(hangrao)
r = max(hangrao) + max(gothua)
if len(gothua) >= len(hangrao):
    r = min(hangrao) + max(gothua)
else:
    c = hangrao.copy()
    c.sort()
    index = len(hangrao)-len(gothua)
    r = c[len(hangrao)-index]
def check(mid):
    i = 0
    j = 0
    vth = []
    vtg = []
    sl = 0
    t = 0
    tmp = 0
    tmph = []
    tmphv = []
    for k in range(len(hangrao)):
        if hangrao[k] < mid:
            t += 1
            tmph.append(k)
            tmphv.append(hangrao[k])
    st_h = sum(tmphv)
    st_g = sum(gothua)
    s_h = 0
    s_g = 0
    while i < len(gothua):
        if j >= len(tmph):
            break
        if len(gothua) - (i) < len(tmph) - (j):
            return 0,vth,vtg,sl
        if (st_h - s_h) + (st_g-s_g) < (len(tmph) - j)*mid:
            return 0,vth,vtg,sl
        if hangrao[tmph[j]] + gothua[i] >= mid:
            tmp += 1
            sl += 1
            s_h += tmphv[j]
            s_g += gothua[i]
            vtg.append(i)
            vth.append(tmph[j])
            j += 1
            i += 1
        else:
            s_g += gothua[i]
            i += 1
    if tmp == t:
        return 1,vth,vtg,sl 
    else:
        return 0,vth,vtg,sl
docao = r
reh = []
reg = []
vth = []
vtg = []
s = 0
while l < r-1:
    test,vth,vtg,sl = check(docao)
    if test == 1:
        l = docao
        reh = vth.copy()
        reg = vtg.copy()
        s = sl
    else:
        r = docao-1
    docao = (l+r) // 2
if r > l:
    t,vth,vtg,sl = check(r)
    if t == 1:
        reh = vth
        reg = vtg
        s = sl
        l = r
if  max(hangrao) > docao:
    t,vth,vtg,sl = check(max(hangrao))
    if t == 1:
        reh = vth
        reg = vtg
        s = sl
        l = max(hangrao)
print(l,s)
for i in range(s):
    print(reh[i]+1,reg[i]+1)