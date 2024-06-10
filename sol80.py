def Polindrom(s):
    if len(s) <= 1:
        return True
    elif s[0] != s[-1]:
        return False
    else:
        return Polindrom(s[1:-1])

print(Polindrom('ab ba'))