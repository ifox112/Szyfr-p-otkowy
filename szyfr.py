def convert(s):
    new = ""
    for x in s:
        new += x
    return new


def encrypting(txt, key):
    row = []
    table = []
    r = 0
    c = 0
    k = -1
    enc = []
    for i in range(len(txt)):
        row.append("-")
    for i in range(key):
        table.append(row[:])
    for i in range(len(txt)):
        table[r][c] = txt[i]
        c += 1
        if r == 0 or r == key-1:
            k = -1 * k
        r = r + k
    #print(table)
    for i in range(key):
        for j in range(len(txt)):
            if table[i][j] != '-':
                enc += table[i][j]

    return convert(enc)
    #import sys
    #for i in range(len(txt)):
    #    sys.stdout.write(enc[i])


def decrypting(txt, key):
    row = []
    table = []
    r = 0
    c = 0
    k = -1
    a = 0
    decr = []
    for i in range(len(txt)):
        row.append("-")
    for i in range(key):
        table.append(row[:])
    for i in range(len(txt)):
        table[r][c] = '@'
        c += 1
        if r == 0 or r == key-1:
            k = -1 * k
        r = r + k
    #print(table)
    for i in range(key):
        for j in range(len(txt)):
            if table[i][j] == '@':
                table[i][j] = txt[a]
                a += 1
    r = 0
    c = 0
    k = -1
    #print(table)
    for i in range(len(txt)):
        decr.append(table[r][c])
        c += 1
        if r == 0 or r == key-1:
            k = -1 * k
        r = r + k

    return convert(decr)
    #import sys
    #for i in range(len(txt)):
    #    sys.stdout.write(decr[i])

print("SZYFR PŁOTKOWY ZE ZMIENNĄ WYSOKOŚCIĄ PŁOTKA\n")
dec = input("1.Szyfrowanie\n2.Deszyfrwanie\n")
#text = input("Wprowadz tekst do zaszyfrowania: ")
height = int(input("Wprowadz klucz szyfrowania: "))
f = input("Podaj sieżkę do pliku: ")



if dec == '1':
    file1 = open(f).read()
    file2 = open('tekst_zaszyfrowany.txt', 'w')
    lines = file1.split('\n')
    for i in range(0, len(lines)):
        buff = str(encrypting(lines[i], height)) + "\n"
        file2.write(buff)
        file2.close
elif dec == '2':
    file1 = open(f).read()
    file2 = open('tekst_odszyfrowany.txt', 'w')
    lines = file1.split('\n')
    for i in range(0, len(lines)):
        buff = str(decrypting(lines[i], height)) + "\n"
        file2.write(buff)
        file2.close


input()

#KACZOROWSKI BARTOSZ
