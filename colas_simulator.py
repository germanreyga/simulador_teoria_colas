import math
from fractions import Fraction as frac

# M/M/S


def mms(la, mi, s):
    la = frac(str(la))
    mi = frac(str(mi))

    rho = frac(la, (s*mi))

    # Calculating p0
    a = 0
    for n in range(0, s):
        a += frac(frac(la, mi) ** n, math.factorial(n))
    b = frac(frac(la, mi) ** s, math.factorial(s))
    c = frac(1, (1-rho))
    p0 = frac(1, a+(b*c))

    # Calculating lq
    d = p0 * (frac(la, mi) ** s) * rho
    e = math.factorial(s) * ((1-rho) ** 2)
    lq = frac(d, e)

    # Calculating l, wq, w
    l = lq + frac(la, mi)
    wq = frac(lq, la)
    w = wq + frac(1, mi)

    return l, lq, w, wq

# M/M/1


def mm1(la, mi):
    return mms(la, mi, 1)

# M/M/s/K


def mmsk(la, mi, s, k):
    la = frac(str(la))
    mi = frac(str(mi))

    rho = frac(la, (s*mi))

    # Calculating p0
    a = 0
    for n in range(0, s+1):
        a += frac(frac(la, mi) ** n, math.factorial(n))
    b = frac(frac(la, mi) ** s, math.factorial(s))
    c = 0
    for n in range(s+1, k+1):
        c += rho ** (n-s)
    p0 = frac(1, a+(b*c))

    # Calculating lq
    d = p0 * (frac(la, mi) ** s) * rho
    e = math.factorial(s) * ((1-rho) ** 2)
    f = 1 - (rho ** (k-s)) - ((k-s) * (rho ** (k-s)) * (1-rho))
    lq = frac(d, e) * f

    # Calculating lae, wq, w, l
    g = frac(la, mi) ** k
    h = math.factorial(s) * (s ** (k-s))
    pk = frac(g, h) * p0
    print(pk)
    lae = la * (1-pk)
    wq = frac(lq, lae)
    w = wq + frac(1, mi)
    l = lae * w

    return lae, l, lq, w, wq

# M/G/1


def mg1(la, mi, sig):
    la = frac(str(la))
    mi = frac(str(mi))
    sig = frac(str(sig))

    rho = frac(la, mi)
    p0 = 1 - rho

    # Calculating lq
    a = (la**2) * (sig**2) * (rho**2)
    b = 2 * p0
    lq = frac(a, b)

    # Calculating l, wq, w
    l = rho + lq
    wq = frac(lq, la)
    w = wq + frac(1, mi)

    return l, lq, w, wq

# M/Ek/1


def mek1(la, mi, k):
    la = frac(str(la))
    mi = frac(str(mi))
    k = frac(str(k))

    lq = frac((la**2)*(1+k), 2*k*mi*(mi-la))
    wq = frac(lq, la)
    w = wq + frac(1, mi)
    l = la * w

    return l, lq, w, wq
