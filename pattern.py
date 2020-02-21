#pattern1
'''
o
oo
ooo
 *
* *
****
'''

for i in range(0,3):
    for j in range(0,i+1):
        print('o',end="")
    print("")
for i in range(0,2):
    for j in range(0,3):
        if i-j == -1 or i-j == 1:
            print("*",end="")
            #print("")
        else:
            print(" ",end="")
    print("")
for i in range(0,4):
    print("*",end="")


#pattern2
'''
*****
****
***
**
*
'''

for i in range(5,0,-1):
    for j in range(0,i):
        print("*",end="")
    print("")

#pattern3
'''
*****
 ****
  ***
   **
    *
'''

temp=5
for i in range(0,6):
    for j in range(0,5-temp):
        print(" ",end="")
    for j in range(0,temp):
        print("*",end="")
    temp=temp-1
    print("")

#pattern4
'''
   *
  ***
 *****
*******
 *****
  ***
   *
'''
inc=1
temp=3
for i in range(0,4):
    for j in range(0,temp):
        print(" ",end="")
    for j in range(0,inc):
        print("*",end="")
    temp=temp-1
    inc=inc+2
    print(" ")
temp1=1
inc1=5
for i in range(0,3):n,
    for j in range(0,temp1):
        print(" ",end="")
    for j in range(0,inc1):
        print("*",end="")
    temp1=temp1+1
    inc1=inc1-2
    print("")
