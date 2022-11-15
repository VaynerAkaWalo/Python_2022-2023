import math

def add_frac(frac1, frac2):
    l = frac1[0] * frac2[1] + frac2[0] * frac1[1]
    m = frac1[1] * frac2[1]
    nwd = math.gcd(l, m)
    return [l/nwd, m/nwd]
    

def sub_frac(frac1, frac2):
    l = frac1[0] * frac2[1] - frac2[0] * frac1[1]
    m = frac1[1] * frac2[1]
    nwd = math.gcd(l, m)
    return [l/nwd, m/nwd]

def mul_frac(frac1, frac2):
    l = frac1[0] * frac2[0]
    m = frac1[1] * frac2[1]
    nwd = math.gcd(l, m)
    return [l/nwd, m/nwd]

def div_frac(frac1, frac2):
    l = frac1[0] * frac2[1]
    m = frac1[1] * frac2[0]
    nwd = math.gcd(l, m)
    return [l/nwd, m/nwd]

def is_positive(frac):
    return (frac[0] >= 0 and frac[1] >= 0) or (frac[0] < 0 and frac[1] < 0)

def is_zero(frac):
    return frac[0] == 0

def cmp_frac(frac1, frac2):
    f1 = frac2float(frac1)
    f2 = frac2float(frac2)
    if(f1 == f2):
        return 0
    return f1 > f2

def frac2float(frac):
    if(frac[0] != 0) :
        return float(frac[0]/frac[1])
    return None

