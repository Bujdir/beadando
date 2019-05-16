def frm(x, b):
    assert(x >= 0)
    assert(1 < b < 37)
    r = ''
    import string
    while x > 0:
        r = string.printable[x % b] + r
        x //= b
    return r
def to(s, b):
    assert(1 < b < 37)
    return int(s, b)
def convert(s, a, b):
    return frm(to(s, a), b)

print(convert('11',10,2))