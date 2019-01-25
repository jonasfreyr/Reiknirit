#1. (2%) Hvað er sauðakóði (pseuodocode) og til hvers er hann notaður? - Svona eiginlega beinagrind yfir hvað maður ætlar að forrita

#2. (3%) Skrifaðu forrit í sauðakóða sem umreytir tugakerfistölu í tvíundarkerfistölu. Hér er ekki
# verið að biðja um keyranlegt forrit.
'''
1. tekur inn heiltölu frá notanda
2. Bý til lista með 2 í upp að veldinu 7
3. ef n er stærra eða sama og summa plús tala í listanum sem index er komið á
3.3 bæti við b +1 binary strenginn
3.6 bæti tölunni í listanum sem indexið er komið á við summuna
4. bæti við b + 0 binary strenginn
5 ef index er komið á seinasta stakið í listanum skila b
6. skila b + fallið aftur með index +1

(2%) Skoðaðu rununa 1, 4, 9, 16, 25, 36, .... Eins og þú sérð er þetta í raun n
2 þar sem n er stak
í menginu náttúrulegar tölur N = {1, 2, 3, 4,...}. Skrifaðu endurkvæma fallið summa(m) sem
reiknar ∑ 𝑛
𝑚 2
𝑛=1
og skilar summunni. Dæmi: Ef m er 5 þá ætti fallið summa(5) að reikna og
skila 12 + 22 + 32+ 4
2 +52 = 55.
'''
def summa(t, i=0, s=0):
    s = (i ** 2)
    if i == t:
        return s



    return s + summa(t, i + 1, s)

print("Summa")
tala = int(input(">> "))

print(summa(tala))

'''
4. (4%) Skoðaðu vel rununa 1, 3, 6, 10, 15, 21, .... Finndu út mynstur rununnar og skrifaðu
endurkvæma fallið runa(m) sem skrifar m fyrstu stök rununnar á skjáinn. Dæmi: runa(5)
mundi skrifa 1 3 6 10 15 á skjá.
'''

def runa(t, i=1, p=0):
    s = i + p
    print(s)

    if i == t:
        return None

    return runa(t, i + 1, s)

print("Runa")
tala = int(input(">> "))

runa(tala)

'''
5. (2%) Skrifaðu endurkvæma fallið þversumma(n) sem tekur færibreytuna n. Fallið skilar til
baka þversummu n. Dæmi: þversumma tölunnar 12 er 3 eða 1+2=3. Þversumma tölunnar
1206 er 9 eða 1+2+0+9=12.
'''

def þversumma(t):
    tala = int(t[0])

    if len(t) == 1:
        return tala

    return tala + þversumma(t[1:])

print("Þversumma")
tala = (input(">> "))

print(þversumma(tala))


'''
6. (2%) Skrifaðu endurkvæma fallið samnefnari(n,m) sem tekur heltölufæribreyturnar n og
m. Fallið skal skila hæsta samnefnara talnanna n og m.
'''
def samnefnari(n, m, s=0):
    if n > m:
        tala = n - s

    else:
        tala = m - s

    if tala == 0:
        return "Ekki hægt"

    if m % tala == 0 and n % tala == 0:
        return tala

    return samnefnari(n, m, s+1)

print("Samnefnari tala1")
tala1 = int(input(">> "))

print("Samnefnari tala2")
tala2 = int(input(">> "))

print(samnefnari(tala1, tala2))
