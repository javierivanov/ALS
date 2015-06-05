
import xml.etree.ElementTree as etree
import sys, os


def average(d):
    a = 0
    for i in d:
        a=a+i
    return a/len(d)


def filter(c):
    c = ord(c)
    ##Vocales
    if c == 65 or c == 65+32:
        return 4
    if c == 69 or c == 69+32:
        return 4
    if c == 73 or c == 73+32:
        return 4
    if c == 79 or c == 79+32:
        return 4
    if c == 85 or c == 85+32:
        return 4

    ## Consonantes 65 - 90
    if (c > 65 and c < 71) or (c > 65+32 and c < 71+32):
        return 0
    if (c >= 71 and c < 77) or (c >= 71+32 and c < 77+32):
        return 1
    if (c >= 77 and c < 84) or (c >= 77+32 and c < 84+33):
        return 2
    if (c >= 84 and c <= 90) or (c >= 84+32 and c <= 90+32):
        return 3

    ##Simbolos puntuacion

    if c in [44,46,58,59,92,124,126]:
        return 5

    ##Numeros 0-4, 5-9
    if c >= 48 and c <= 52:
        return 6
    if c > 52 and c <= 57:
        return 7

    ##Simbolos matematcos

    if c in [42,43,45,47,60,61]:
        return 8

    ##Simbolos pares y otros
    return 9

def partial(d,s):
    out = []
    t = len(d)/s
    for i in range(0, s):
        out.append(0)
        for e in range(0,t):
            out[i] = out[i]+d[i+e*s]
        out[i] = out[i]/t
    return out

def main():
    test = "HolaMundo Como estan todos y todos welcome"
    d = []
    dd = []
    for i in test:
        d.append(ord(i))
        dd.append(filter(i))

    print len(test)/25
    print average(d)
    print len(dd)/10

    print partial(dd, 10)

if __name__ == "__main__":
    main()
