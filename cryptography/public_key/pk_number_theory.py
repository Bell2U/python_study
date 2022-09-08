from math import gcd

# given n, returns z(n)* and phi(n)
def z_star(n: int): 
    mult_grp = [x for x in range(n) if gcd(n, x) == 1]
    theta_n = len(mult_grp)
    return mult_grp, theta_n

# The Euclidean algorithm
# return (d, s, t) so sx + ty = d = gcd(x,y)    i.e. 
# d >= 0
def bezout(x: int, y: int):
    if x == 0:
        return (y, 0, 1) if y >= 0 else (-y, 0, -1)
    d, s, t = bezout(y%x, x)
    return (d, t - (y//x)*s, s)

# find the invertse of x without knowing theta(n), where x belongs to z(n)*
def modinv(x: int, n: int):
    d, s, t = bezout(x, n)
    if d != 1:
        raise ValueError(f'{x} is not coprime to {n}.')  # x not belongs to z(n)*
    return s