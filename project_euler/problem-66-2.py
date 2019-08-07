
def f(n):
    m = int(n**0.5)
    if n == m**2:
        y = (1,0)
    else:
        x = (m,1)
        y = (m+1,1)
        while y[0]**2- n*y[1]**2 > 1:
            z = (x[0]+y[0],x[1]+y[1])
            if z[0]**2- n*z[1]**2 > 0:
                y = z
            else: x = z
        return y[0]

print f(661)