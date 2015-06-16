
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

def grafer(c):
    for i in range(0, len(c)):
        print str(i) + " " + str((c[i]))

def distribucionAproximada(texto, largo):
    salida = []
    t = len(texto)/largo
    for i in range(0, largo):
        salida.append(0)
        for e in range(0, t):
            salida[i] = salida[i] + ord(texto[i+e*largo])
        salida[i] = salida[i] / t
    prom=0

    for i in range(largo/2, largo):
        prom = prom + salida[i]
    prom=prom/(largo/2)
    for i in range(0, largo/2):
        salida[i] = (salida[i]+prom)/2
        pass
    for i in range(0, len(salida)):
        salida[i] = salida[i] - 32
        salida[i] = int(salida[i]/10)
    return salida

def promedioParcial(texto, factor):
    prom = 0
    for i in texto:
        prom = prom + int(ord(i)-32)/10
    prom = prom/factor
    return prom

def generarHash(distribucion, pParcial, p):
    salida = str(pParcial) + str(p)
    for i in distribucion:
        salida = salida + str(i)
    return int(salida)

def __shortcut(c1):
    return generarHash(distribucionAproximada(c1,5), promedioParcial(c1,100), promedioParcial(c1,len(c1)))

def main():
    c = range(0,9)
    c[0] = "crc-06"
    c[1] = "gas01"
    c[2] = "CCLSimpleClient"
    c[3] = "omniORB--1298793584"
    c[4] = "TelCalPublisherEventNC-Consumer"
    c[5] = "__process_event - Took too long to handle an 'PhaseCalReducedEvent' event: 2.257478 seconds."
    c[6] = "__process_event - Took too long to handle an 'AtmosphereReducedEvent' event: 2.257478 seconds."
    c[7] = "Main - No Primary Flux Calibrator up in the sky! Wait until a primary Flux Calibrator is up"
    c[8] = "setExecError - Error in the script execution: ACSErr.ErrorTrace(file='/alma/ACS-12.1/ACSSW/bin/SBExecProcess.py', lineNum=138, routine='<module>', host='gas01', process='5159', thread='MainThread', timeStamp=136472328149382460L, sourceObject='', errorType=10100L, errorCode=5L, severity=Error, shortDescription='General ScriptExecutor runtime error', data=[], previousError=[ACSErr.ErrorTrace(file='/alma/ACS-12.1/ACSSW/bin/SBExecProcess.py', lineNum=132, routine='<module>', host='gas01', process='5159', thread='MainThread', timeStamp=136472328149346010L, sourceObject='', errorType=7L, errorCode=0L, severity=Error, shortDescription='A Python exception', data=[ACSErr.NameValue(name='Real Description', value='Request to exit from the interpreter.'), ACSErr.NameValue(name='Traceback', value='Traceback (most recent call last):\n  File \"/alma/ACS-12.1/ACSSW/bin/SBExecProcess.py\", line 108, in <module>\n    result = executor.runSource(srcCode)\n  File \"/alma/ACS-12.1/ACSSW/lib/python/site-packages/ScriptExec/Executor.py\", line 92, in runSource\n    exec source in self._globals, self._locals\n  File \"<string>\", line 140, in <module>\nSystemExit\n')], previousError=[])])"
    for i in c:
        print str(__shortcut(i)/100) + " => " + i
        print "------------------------------------------------------------------------"



if __name__ == "__main__":
    main()
