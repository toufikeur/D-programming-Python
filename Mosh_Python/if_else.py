weight = float(input("Enter your weight: "))
unit =input("(L)bs or (K)g: ")


while 1 :
    
    if unit.upper()=="L" :
            converted = weight * 0.45
            print(f"You are {converted} Kilo")
            break

    else :
            converted = weight / 0.45
            print(f"You are {converted}Pounds")
            break
    