
# notes
#   Very Important Formula (not foreshadow)
#     y = a^-1(x-b) mod 26
# all of the alphabet, copy/paste
#   a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z


#beginning of code


# given numbers
#first_number_given = int(input("Enter the first number given: "))
first_number_given = 23
#second_number_given = int(input("Enter the second number given: "))
second_number_given = 23
print("If you would like to stop, enter 'stop' in the input box.")
inversed = input('Enter the inverse value of "a" (this is found on the resource sheet provided [at least i think]): ')


# all of the letters numercial value. It is inside a function to simplfy the code and to clean it up
def alphabet_values():
    a=0
    b=1
    c=2
    d=3
    e=4
    f=5
    g=6
    h=7
    i=8
    j=9
    k=10
    l=11
    m=12
    n=13
    o=14
    p=15
    q=16
    r=17
    s=18
    t=19
    u=20
    v=21
    w=22
    x=23
    y=24
    z=25
    return a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z


# what the varible letter_value is equal to
def what_is_letter_value(a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z):
    # the letter we want to find
    letter = str(input("Enter the letter you would like to find the value of: ")).lower()

    if letter == "a":
        letter_value = a
    elif letter == "b":
        letter_value = b
    elif letter == "c":
        letter_value = c
    elif letter == "d":
        letter_value = d
    elif letter == "e":
        letter_value = e
    elif letter == "f":
        letter_value = f
    elif letter == "g":
        letter_value = g
    elif letter == "h":
        letter_value = h
    elif letter == "i":
        letter_value = i
    elif letter == "j":
        letter_value = j
    elif letter == "k":
        letter_value = k
    elif letter == "l":
        letter_value = l
    elif letter == "m":
        letter_value = m
    elif letter == "n":
        letter_value = n
    elif letter == "o":
        letter_value = o
    elif letter == "p":
        letter_value = p
    elif letter == "q":
        letter_value = q
    elif letter == "r":
        letter_value = r
    elif letter == "s":
        letter_value = s
    elif letter == "t":
        letter_value = t
    elif letter == "u":
        letter_value = u
    elif letter == "v":
        letter_value = v
    elif letter == "w":
        letter_value = w
    elif letter == "x":
        letter_value = x
    elif letter == "y":
        letter_value = y
    elif letter == "z":
        letter_value = z
    return letter_value

# the actual formula
def plus_minus(inversed, value, second_number_given):
    stor = (int(inversed) * (value - (second_number_given))) % 26
    return stor

#to stop the loop
def exit(letter):
    if letter == "stop":
        print("Have a happy and nice day!")
        exit
    else:
        next_letter = True
        return next_letter
# actual execution

# the value to letter conversion
def find_stor_letter(stor_number):
    if stor_number == 0:
        stor_letter = "a"
    elif stor_number == 1:
        stor_letter = "b"
    elif stor_number == 2:
        stor_letter = "c"
    elif stor_number == 3:
        stor_letter = "d"
    elif stor_number == 4:
        stor_letter = "e"
    elif stor_number == 5:
        stor_letter = "f"
    elif stor_number == 6:
        stor_letter = "g"
    elif stor_number == 7:
        stor_letter = "h"
    elif stor_number == 8:
        stor_letter = "i"
    elif stor_number == 9:
        stor_letter = "j"
    elif stor_number == 10:
        stor_letter = "k"
    elif stor_number == 11:
        stor_letter = "l"
    elif stor_number == 12:
        stor_letter = "m"
    elif stor_number == 13:
        stor_letter = "n"
    elif stor_number == 14:
        stor_letter = "o"
    elif stor_number == 15:
        stor_letter = "p"
    elif stor_number == 16:
        stor_letter = "q"
    elif stor_number == 17:
        stor_letter = "r"
    elif stor_number == 18:
        stor_letter = "s"
    elif stor_number == 19:
        stor_letter = "t"
    elif stor_number == 20:
        stor_letter = "u"
    elif stor_number == 21:
        stor_letter = "v"
    elif stor_number == 22:
        stor_letter = "w"
    elif stor_number == 23:
        stor_letter = "x"
    elif stor_number == 24:
        stor_letter = "y"
    elif stor_number == 25:
        stor_letter = "z"
    return stor_letter
    
#               o                   o                
#___________________________________________________#
#(heh look, i make a face)


# checking if the user would like to stop the loop
exit(inversed)
next_letter = True

while next_letter == True:
    a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z = alphabet_values() #damn, thats a lot of varibles
    value = what_is_letter_value(a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z) # i lowk didn't now that many could be there
    stor_number = plus_minus(inversed,value, second_number_given)
    stor_letter = find_stor_letter(stor_number)

    #our result
    print("The decrypted letter is: ", stor_letter)