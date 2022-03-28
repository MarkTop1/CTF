import gmpy2
import libnum

def continuedFra(x, y):
    cf = []
    while y:
        cf.append(x // y)
        x, y = y, x % y
    return cf
def gradualFra(cf):
    numerator = 0
    denominator = 1
    for x in cf[::-1]:
        # 这里的渐进分数分子分母要分开
        numerator, denominator = denominator, x * denominator + numerator
    return numerator, denominator
def solve_pq(a, b, c):
    par = gmpy2.isqrt(b * b - 4 * a * c)
    return (-b + par) // (2 * a), (-b - par) // (2 * a)
def getGradualFra(cf):
    gf = []
    for i in range(1, len(cf) + 1):
        gf.append(gradualFra(cf[:i]))
    return gf


def wienerAttack(e, n):
    cf = continuedFra(e, n)
    gf = getGradualFra(cf)
    for d, k in gf:
        if k == 0: continue
        if (e * d - 1) % k != 0:
            continue
        phi = (e * d - 1) // k
        p, q = solve_pq(1, n - phi + 1, n)
        if p * q == n:
            return d


e= 0x14b367bf01efd4dc667b8e62975479c612c96e78f7f1f55242b2973c882ddcb33a65c52174d8ae1273764ce429054ea3f2fdc38ff205443c92ef4198739f05aa11fc10d3fc6ff30c8f5f05a04f43e3d8fc9bfffe916b2e0360560a162729e91b7775bda70177e0f875626e0a81bd4eacea9948b02232a82659f8d9aa9b4c754f
n= 0x75be564267f8bf6c2038dd0cadfeecbc3158acfc27e679dd0bdb0db0e90bd5198a0a7edc0626f357a2d75f3c37ede045b7f7ca6bda79e5bf6fc0aea0aa7beda587388599d2b77b538fc3e666784493ffaf731e2ae232e8e9e9f9f2a4df25c19b7680f5bf6c485bd87923f01c17d8ec35438772c28e361774e6e7681d67ecbe19
c= 10127659956533419108589656976567211166527205183773088147543122705230809548550336271584049969380709512046523116316965506372940655242616078713681678662841367955124154879878984026023241163358487655249424233120021240245459984899558747887087199609289148343740081670749999484769650710161617077523656215330005636913

d=wienerAttack(e, n)
m=pow(c, d, n)
print(libnum.n2s(m).decode())