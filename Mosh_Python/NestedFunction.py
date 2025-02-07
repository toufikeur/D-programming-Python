# def disp():
#     def show():
#         print(f'Show the function')
#     print(f'Display sub functions')
#     show()
# disp()

def disp():
    def show():
       return 'This is show function'
    x= show() +  ' ' + 'and Display function'
    return x
a= disp()  
print(a)



