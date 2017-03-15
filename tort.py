from math import ceil

pikkus = input("Sisestada pikkus tykkides: ")
laius = input("Sisestada laius tykkides: ")
k6rgus = input("Sisestada k6rgus tykkides: ")
tk_pakk = input("Mitu tykki on yhes pakis: ")

def pakke():
    tk_arv = int(pikkus)*int(laius)*int(k6rgus)
    pakk_arv = tk_arv/int(tk_pakk)
    print ("Sul on vaja "+str(ceil(pakk_arv))+" pakki")


pakke()

    