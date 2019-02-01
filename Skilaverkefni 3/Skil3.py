staf = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
staf_cache = []
def strengur(n):
    s = []
    for a in range(n):
        s.append(a)
    print(s)
    return r(s)

def r(l, m=1):
    p = l[len(l)-m]

    return p

print(strengur(7))
