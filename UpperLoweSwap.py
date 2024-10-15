str1 = "ridoy"
tit="Hello Mr ridoy khan how are you?"
tit1="Hello Mr Toufike Ur Rahman Ridoy"
dig="124252"
dig1="123ab543"
sp=" "
print(str1)
str2 =str1.upper()
print(str2)
str3 =str2.lower()
print(str3)
print(tit)
str4 =tit.title()
print(str4)

print()

print(str1.isupper())
print(tit.isupper())
print(str1.islower())
print(tit.islower())
print("About title")
print(tit.istitle())
print(tit1.istitle())
print("About digit")
print(dig.isdigit())
print(dig1.isdigit())
print("About ALPHA")
print(dig1.isalpha())
print(dig.isalpha())
print(str1.isalpha())
print("Alnum\n")
print(dig.isalnum())

print()
print("is Space")
print(str1.isspace())
print(tit.isspace())
print(sp.isspace())

print("\n About left or Right strip \n")
lsp="    Ridoy"
print(lsp)
print(lsp.lstrip())

rsp="Ridoy        "
print(rsp)
print(rsp.lstrip())