# a=(2,3,4,5,6)
# b,c,d,e,f =a
# print(b)
# print(c)
# print(d)
# print(a)

#apply this concept :

customer = ("Ridoy","ridoy@gmail.com","01774416101")

name,email,phone_number = customer
print(name)
print(email)
print(phone_number)
#another way

customer = {
    "name": "Ridoy",
    "email": "ridoy@gmail.com",
    "phone_number": "01774416101"
}

print(customer["email"])

print(customer.get("birthdate","1 Dec"))
