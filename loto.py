from random import randint 
check = randint(0,9) #genereerib suvalise nri

def loto(): 
    number = input("Sisestada yks t2isarv 0-9: ")
    if number.isdigit():
        print(check)
        number = int(number)
        if number < check:
            print("Sisestatud number on v2iksem, kui kontrollarv")
            loto()
        elif number > check:
            print("Sisestatud number on suurem, kui kontrollarv")
            loto()
        else:
            print("Palju 6nne, minge auhinnale j2rgi")
    else :
        print("Numbrit taheti sa igevene tainapea")


loto() #paneb definitsiooni kinni

        
    
    
    