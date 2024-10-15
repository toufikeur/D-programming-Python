str1="Toufike Ur Rahman Ridoy"
str2="TUR Ridoy"
str3="Hey Ridoy"
str4=str2.replace("Ridoy",str1)
print(str4)
str5=str1.split(' ')
print(str5)
str6=("hello","Mr ","Ridoy")
str7='-'.join(str6)
print(str7)

print(str3.startswith("TUR"))
print(str3.startswith("Hey"))
print(str3.endswith("Ridoy"))
