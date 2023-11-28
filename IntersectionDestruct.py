class Prvek:
    def __init__(self, x, dalsi):
        self.x = x
        self.dalsi = dalsi

def VytiskniLSS(p):
    print("LSS:", end=" ")
    while p is not None:
        print(p.x, end=" ")
        p = p.dalsi
    print(".")

def NactiLSS():
    """cte cisla z radku, dokud nenacte prazdny radek"""
    prvni = None
    posledni = None
    r = input()
    while r != "":
        radek = r.split()
        if len(radek) == 0:
            break
        for s in radek:
            p = Prvek(int(s), None)
            if prvni is None:
                prvni = p
            else:
                posledni.dalsi = p
            posledni = p
        r = input()
    return prvni

def IntersectionDestruct(a, b):
    result = Prvek(None, None)
    current = result

    while a is not None and b is not None:
        if a.x < b.x:
            a = a.dalsi
        elif a.x > b.x:
            b = b.dalsi
        else:
            current.dalsi = a
            a = a.dalsi
            b = b.dalsi
            current = current.dalsi
        current.dalsi = None
    return result.dalsi

VytiskniLSS(IntersectionDestruct(NactiLSS(), NactiLSS()))