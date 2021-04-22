a, k, b, m, n = list(map(int, input().split()))
socaymoichukylon = m * (k - 1) * a + k * (m - 1) * b
sochukydachat = n // socaymoichukylon
socayconlai = n % socaymoichukylon

i = 0
if not socayconlai:
    i = -1
else:
    i = int(socayconlai // (a + b - a / k - b / m))
    while (a + b) * i - a * (i // k) - b * (i // m) >= socayconlai:
        i -= 1

    while (a + b) * i - a * (i // k) - b * (i // m) < socayconlai:
        i += 1

ans = m * k * sochukydachat + int(i)
print(ans)