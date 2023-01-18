#!/usr/bin/python3
import random
import sys
import math
import numpy as np
def battle(m,n,t):
    print(n)
    P=""
    B=0
    b=random.randint(1,2)
    b1=random.randint(1,2)
    w=b+b1*10-10
    p=random.randint(1,2)
    if b==10:
        r=10
    else:
        r=w%10
    l=int((w+10-1)/10)


    while B<4:
        t[l][r]="B"
        if p%2==0:
            r+=1
        else:
            l+=1
        B=B+1



    C=0
    c=random.randint(6,6)
    c1=random.randint(6,6)
    w=c+c1*10-10
    p=random.randint(1,2)
    if c==10:
        r=10
    else:
        r=w%10
    l=int((w+10-1)/10)

    while C<5:
        t[l][r]="C"
        
        if p%2==0:
            r+=1
        else:
            l+=1
        C+=1

    D=0
    d=random.randint(7,9)
    d1=random.randint(7,9)
    w=d+d1*10-10
    p=random.randint(1,2)
    if d==10:
        r=10
    else:
        r=w%10
    l=int((w+10-1)/10)

    while D<2:
        t[l][r]="D"
        
        if p%2==0:
            r+=1
        else:
            l+=1
        D+=1

    K=0
    k=random.randint(6,8)
    k1=random.randint(1,2)
    w=k+k1*10-10
    p=random.randint(1,2)
    if k==10:
        r=10
    else:
        r=w%10
    l=int((w+10-1)/10)

    while K<3:
        t[l][r]="K"
        
        if p%2==0:
            r+=1
        else:
            l+=1
        K+=1

    S=0
    s=random.randint(1,3)
    s1=random.randint(6,7)
    w=s+s1*10-10
    p=random.randint(1,2)
    if s==10:
        r=10
    else:
        r=w%10
    l=int((w+10-1)/10)

    while S<3:
        t[l][r]="S"
        
        if p%2==0:
            r+=1
        else:
            l+=1
        S+=1


    for row in m:
        print(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], sep="|")
    ship(m)
    
def ship(m):
    turn=0
    while turn<200:
        T=0
        P=0
        if turn%2==0:
            y=input("Enter letter from A to J")        
            x=int(input("Enter number from 1 to 10"))
            a=ord(y.upper())-64+x*10-10
            if y=="J":
                r=10
            else:
                r=a%10
            q=m[int((a+10-1)/10)][r]
            while str(q)=="X" or str(q) not in m:
                y=input("Enter letter from A to J ")
                x=int(input("Enter number from 1 to 10 "))
                q=m[int((a+10-1)/10)][r]
            l=int((a+10-1)/10)        
            print(l)
            print(a)

            if t[int((a+10-1)/10)][r].isalpha():
                m[int((a+10-1)/10)][r]="X"
                t[int((a+10-1)/10)][r]="X"        
                T+=1
            else:
                m[int((a+10-1)/10)][r]="O"
                t[int((a+10-1)/10)][r]="O"        
                
        else:

            y=random.randint(0,9)        
            x=random.randint(0,9)
            if x==10:
                r=10
            else:
                r=a%10
            a=r+x*10-10
            l=int((a+10-1)/10)     
            
            if n[l][r].isalpha:
                n[l][r]="O"
            else:
                n[l][r]="X"
                P+=1
            print(n)
            for row in m:
                print(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], sep="|")
        turn+=1


        if T==17:
            print("You Win!")
            return("nothing")
        if P==17:
            print("Computer Wins!")
            return("nothing")
if __name__ == "__main__":

    n = np.array(open("ship1.dat").read().split())
    n = n.reshape(10,10)
    m=[["  ","A","B","C","D","E","F","G","H","I","J"],["1 ","_","_","_","_","_","_","_","_","_","_"],["2 ","_","_","_","_","_","_","_","_","_","_"],["3 ","_","_","_","_","_","_","_","_","_","_"],["4 ","_","_","_","_","_","_","_","_","_","_"],["5 ","_","_","_","_","_","_","_","_","_","_"],["6 ","_","_","_","_","_","_","_","_","_","_"],["7 ","_","_","_","_","_","_","_","_","_","_"],["8 ","_","_","_","_","_","_","_","_","_","_"],["9 ","_","_","_","_","_","_","_","_","_","_"],[10,"_","_","_","_","_","_","_","_","_","_"]]
    t=[["  ","A","B","C","D","E","F","G","H","I","J"],["1 ","_","_","_","_","_","_","_","_","_","_"],["2 ","_","_","_","_","_","_","_","_","_","_"],["3 ","_","_","_","_","_","_","_","_","_","_"],["4 ","_","_","_","_","_","_","_","_","_","_"],["5 ","_","_","_","_","_","_","_","_","_","_"],["6 ","_","_","_","_","_","_","_","_","_","_"],["7 ","_","_","_","_","_","_","_","_","_","_"],["8 ","_","_","_","_","_","_","_","_","_","_"],["9 ","_","_","_","_","_","_","_","_","_","_"],[10,"_","_","_","_","_","_","_","_","_","_"]]
    battle(m,n,t)