data segment
    num1 db ?
    num2 db ?
    res db ?
    msg1 db 10,13,"enter the first number: $"
    msg2 db 10,13,"enter the second number: $"
    msg3 db 10,13,"result of addition is: $"
data ends   

assume cs:code,ds:data

code segment
    start: mov ax,data
           mov ds,ax           ;initialize data segment 
           
           lea dx,msg1         ;load address of msg1 into dx
           mov ah,9h           ;interrupt to display contents of dx
           int 21h    
           
           mov ah,1h           ;read a character from console
           int 21h
           sub al,30h          ;convert number into bcd from ascii form
           mov num1,al         ;store number as num1
           
           lea dx,msg2         ;load address of msg2 into dx
           mov ah,9h           ;interrupt to display contents of dx
           int 21h    
           
           mov ah,1h           ;read a character from console
           int 21h
           sub al,30h          ;convert number into bcd from ascii form
           mov num2,al         ;store number as num2
           
           add al,num1         ;add num1 to num2
           mov res,al          ;store sum in res
           mov ah,0            ;clear garabage value (ah to be used later)
           aaa                 ;converts hex to bcd and stores values in ah and al 
           add ah,30h          ;first digit converted into bcd
           add al,30h          ;second digit converted from ascii to bcd
           
           mov bx,ax           ;save value of ax into bx
           lea dx,msg3         ;print ms3
           mov ah,9h
           int 21h
           
           mov ah,2h           ;print first digit
           mov dl,bh                                
           int 21h
           
           mov ah,2            ;print second digit
           mov dl,bl
           int 21h
    
           mov ah,4ch
           int 21h
    
code ends
end start




Lab;1
.model small
.stack 100h
.data
msg1 db 'Input: $'
msg2 db 0Dh, 0Ah, 'Output: $'
msg3 db 0Dh, 0Ah, 'this in not character $'
.code
main:
mov ax, @data
mov ds, ax
mov ah, 09h
lea dx, msg1
int 21h
mov ah, 01h
int 21h
mov cl, al
cmp cl,'A'
jl no_text
cmp cl,'Z'
jle Out_put
cmp cl,'a'
jl no_text
cmp cl,'z'
jle Out_put
Out_put:
mov ah, 09h
lea dx, msg2
int 21h
mov ah, 02h
mov dl, cl
int 21h
jmp end_program
no_text:
mov ah,09h
lea dx,msg3
int 21h
jmp end_program
end_Program:
mov ah, 4Ch
int 21h






Lab:2
.MODEL SMALL 
.STACK 100h 
.DATA 
myname db "Toufike-Ur-Rahman Ridoy$" 
.CODE                 
MAIN PROC 
 MOV AX, @DATA 
 MOV DS,AX 
 LEA DX, myname  
 MOV AH, 09h 
 INT 21H 
 MAIN ENDP 
END MAIN












Lab-3
.model small
.stack 100h
.data
msg1 db 'Enter Number_1: $'
msg2 db 0Dh, 0Ah, 'Enter Number_2: $'
msg3 db 0Dh, 0Ah, 'Sum is: $'
result db ?
msg4 db 0Dh, 0Ah, 'this is not valid input try again $'
.code
main:
mov ax, @data
mov ds, ax
mov ah, 09h
lea dx, msg1
int 21h
mov ah, 01h
int 21h
cmp al, '0'
jl check
cmp al, '9'
jg check
sub al, '0'
mov bl, al
mov ah, 09h
lea dx, msg2
int 21h
mov ah, 01h
int 21h
sub al, '0'
add bl, al
mov ah, 09h
lea dx, msg3
int 21h
add bl, '0'
mov ah, 02h
mov dl, bl
int 21h
jmp exit
check:
mov ah, 09h
lea dx, msg4
int 21h
jmp exit
exit:
mov ah, 4Ch
int 21h


Lab:4

.model small
.stack 100h
.data
msg1 db 'Enter Number_1: $'        
msg2 db 0Dh, 0Ah, 'Enter Number-2: $' 
msg3 db 0Dh, 0Ah, 'Subtraction Result is: $'     
msg4 db 0Dh, 0Ah, 'This is not valid input. Try again. $' 
result db ?                           
.code
main:
    mov ax, @data      
    mov ds, ax

    mov ah, 09h
    lea dx, msg1
    int 21h

    mov ah, 01h
    int 21h
    cmp al, '0'
    jl invalid_input
    cmp al, '9'
    jg invalid_input
    sub al, '0'         
    mov bl, al          

    mov ah, 09h
    lea dx, msg2
    int 21h

    mov ah, 01h
    int 21h
    cmp al, '0'
    jl invalid_input
    cmp al, '9'
    jg invalid_input
    sub al, '0'        
    sub bl, al         

    mov ah, 09h
    lea dx, msg3
    int 21h

    cmp bl, 0
    jge positive_result 
    mov ah, 02h
    mov dl, '-'        
    int 21h
    neg bl             

positive_result:
    add bl, '0'         
    mov ah, 02h
    mov dl, bl
    int 21h
    jmp exit           

invalid_input:
    mov ah, 09h
    lea dx, msg4
    int 21h

exit:
    mov ah, 4Ch         
    int 21h
end main

Lab:5

.MODEL SMALL
.STACK 100H
.DATA
A DB "Enter Multiplicand : $"
B DB "Enter Multiplier : $"
C DB "Multiplication Result : $"
.CODE
MAIN PROC
MOV AX,@DATA
MOV DS,AX
LEA DX,A
MOV AH,9
INT 21H
MOV AH,1
INT 21H
SUB AL,48
MOV BL,AL
MOV AH,2
MOV DL,0DH
INT 21H
MOV DL,0AH
INT 21H
LEA DX,B
MOV AH,9
INT 21H
MOV AH,1
INT 21H
SUB AL,48
MOV BH,AL
MOV AH,2
MOV DL,0DH
INT 21H
MOV DL,0AH
INT 21H
MOV AL,BL
MOV AH,0
mul BH
aam
mov bh,ah
add bh,48
mov bl,al
add bl,48
LEA DX,C
MOV AH,9
INT 21H
MOV AH,2
MOV DL,Bh
INT 21H
MOV AH,2
MOV DL,BL
INT 21H
MOV AH,4CH
INT 21H
MAIN ENDP
END MAIN


Lab:6

.MODEL SMALL
.STACK 100H
.DATA
A DB "Enter Devident : $"
B DB "Enter Divisor : $"
ERROR DB "Operation can not be done $"
Q DB "Result : $"
R DB "Reminder : $"
.CODE
MAIN PROC
MOV AX,@DATA
MOV DS,AX
LEA DX,A
MOV AH,9
INT 21H
MOV AH,1
INT 21H
SUB AL,48
MOV BL,AL
MOV AH,2
MOV DL,0DH
INT 21H
MOV DL,0AH
INT 21H
LEA DX,B
MOV AH,9
INT 21H
MOV AH,1
INT 21H
SUB AL,48
MOV BH,AL
MOV AH,2
MOV DL,0DH
INT 21H
MOV DL,0AH
INT 21H
CMP BH,0
JE ERR
MOV AL,BL
MOV AH,0
DIV BH
ADD AL,48
MOV BL,AL
ADD AH,48
MOV BH,AH
LEA DX,Q
MOV AH,9
INT 21H
MOV AH,2
MOV DL,BL
INT 21H
MOV AH,2
MOV DL,0DH
INT 21H
MOV DL,0AH
INT 21H
LEA DX,R
MOV AH,9
INT 21H
MOV AH,2
MOV DL,BH
INT 21H
MOV AH,4CH
INT 21H
ERR:
LEA DX,ERROR
MOV AH,9
INT 21H
MOV AH,4CH
INT 21H
MAIN ENDP
END MAIN

Lab:7
.model small
.stack 100h
.data
msg1 db 'Enter an Uppercase Letter: $'
msg2 db 0Dh, 0Ah, 'The lowercase letter Of this is: $'
errorMsg db 0Dh, 0Ah, 'Invalid input. Please enter an uppercase letter. $'
.code
main:
mov ax, @data
mov ds, ax
mov ah, 09h
lea dx, msg1
int 21h
mov ah, 01h
int 21h
cmp al, 'A'
jl invalid
cmp al, 'Z'
jg invalid
mov bl,al
add bl,32
mov ah, 09h
lea dx, msg2
int 21h
mov ah, 02h
mov dl, bl
int 21h
jmp exit
invalid:
mov ah, 09h
lea dx, errorMsg
int 21h
exit:
mov ah, 4Ch
int 21h
end main


Lab:8

.model small
.stack 100h
.data
msg1 db 'Enter a lowercase letter: $'
msg2 db 0Dh, 0Ah, 'The Uppercase Letter of this is: $'
errorMsg db 0Dh, 0Ah, 'Invalid input. Please enter an lowercase letter. $'
.code
main:
mov ax, @data
mov ds, ax
mov ah, 09h
lea dx, msg1
int 21h
mov ah, 01h
int 21h
cmp al, 'a'
jl invalid
cmp al, 'z'
jg invalid
mov bl,al
sub bl,32
mov ah, 09h
lea dx, msg2
int 21h
mov ah, 02h
mov dl, bl
int 21h
jmp exit
invalid:
mov ah, 09h
lea dx, errorMsg
int 21h
exit:
mov ah, 4Ch
int 21h
end main


Lab;9
.model small
.stack 100h
.data
msg1 db 'Enter number_1: $'
msg2 db 0Dh, 0Ah, 'Enter number_2: $'
msg3 db 0Dh, 0Ah, 'The smallest number is: $'
.code
main:
mov ax, @data
mov ds, ax
mov ah, 09h
lea dx, msg1
int 21h
mov ah, 01h
int 21h
sub al, '0'
mov bl, al
mov ah, 09h
lea dx, msg2
int 21h
mov ah, 01h
int 21h
sub al, '0'
mov cl, al
cmp bl, cl
jle show_bl
mov bl, cl
show_bl:
mov ah, 09h
lea dx, msg3
int 21h
add bl, '0'
mov dl, bl
mov ah, 02h
int 21h
mov ah, 4Ch
int 21h
end main




Lab:10

.model small
.stack 100h
.data
msg1 db 'Enter number_1: $'
msg2 db 0Dh, 0Ah, 'Enter number_2: $'
msg3 db 0Dh, 0Ah, 'The largest number is: $'
.code
main:
mov ax, @data
mov ds, ax
mov ah, 09h
lea dx, msg1
int 21h
mov ah, 01h
int 21h
sub al, '0'
mov bl, al
mov ah, 09h
lea dx, msg2
int 21h
mov ah, 01h
int 21h
sub al, '0'
mov cl, al
cmp bl, cl
jge show_bl
mov bl, cl
show_bl:
mov ah, 09h
lea dx, msg3
int 21h
add bl, '0'
mov dl, bl
mov ah, 02h
int 21h
mov ah, 4Ch
int 21h
end main





























from numpy import*

a=array([[1,2,3,4],[5,6,7,8],[11,12,13,14]])

# for r in a:
#     for x in r:
#         print(x)
#     print()

n=len(a)
# for i in range(n):
#     for j in range(len(a[i])):
#         print(a[i][j])
#     print()
i=0
while (i<n):
    j=0
    while j<len(a[i]):
        print(a[i][j])
        j+=1
    print()
    i+=1
print("End of the code")
