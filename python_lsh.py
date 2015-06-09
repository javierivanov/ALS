
import xml.etree.ElementTree as etree
import sys, os


def average(d):
    a = 0
    for i in d:
        a=a+i
    return a/len(d)


def filter(text):
    
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

    if c in [32,44,46,58,59,92,124,126]:
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
    test2 = "hola mundo como estan"
    test =  "Hola Mundo Como estan"
    dd = []
    dd2 = []
    ddprom = 0
    dd2prom = 0
    for i in test:
        ddprom=ddprom+filter(i)
    ddprom=ddprom/(25)

    for i in test2:
        dd2prom = dd2prom + filter(i)

    dd2prom=dd2prom/(25)

    for i in test:
        dd.append(filter(i))
    for i in test2:
        dd2.append(filter(i))
    size=6
    for i in range(0, len(dd)):
        print str(i)+" "+str(dd[i])

    #print str(ddprom) + str(partial(dd, size))
    #print str(dd2prom) + str(partial(dd2, size))
    print test
    print test2
    ddnum = 0
    ddres = partial(dd,size)
    ddres.reverse()
    for i in range(0, size):
        ddnum = ddnum + ddres[i]*(10**i)
    ddnum = ddnum + (ddprom)*(10**size)
    print ddnum
    dd2num = 0
    dd2res = partial(dd2,size)
    dd2res.reverse()
    for i in range(0,size):
        dd2num = dd2num + dd2res[i]*(10**i)
    dd2num = dd2num + (dd2prom)*(10**size)
    print dd2num

    print "diff:" + str(abs(ddnum-dd2num))

if __name__ == "__main__":
    main()
