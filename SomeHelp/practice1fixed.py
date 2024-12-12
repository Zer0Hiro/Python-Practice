# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 15:53:23 2024

@author: motil
"""

def main():
    length=1
    delta=0
    delta_s=0
    delta_f=0
    length_s=0
    start=0
    count = 0
    num1=int(input("Insert 1st number:"))
    start=num1
    while num1!=-1 and num1>0:
        num2=int(input("Insert next number, end with -1:"))
        if num2==-1 or num2<0: 
            num1=num2
        else:
            length+=1
            delta=num2-num1
            if delta!=delta_s:
                if length>length_s:
                    start_s=start
                    delta_f=delta_s
                    length_s=length-1
                length=2
                start=num1
                delta_s=delta
            count+=1
            num1=num2
    
    if length<=length_s:
        delta=delta_f
        start=start_s
        length=length_s
             
    if num1==-1:
        if count==0:
            print("Longest mathematical series start with %d, length of %d"%(start,length))
        else:
            print("Longest mathematical series start with %d, delta of %d, length of %d"%(start,delta,length))
    else:
        print("Illegal data!")
main()
        
    