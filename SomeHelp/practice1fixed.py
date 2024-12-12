# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 15:53:23 2024

@author: motil
"""

def main(): 
    s_delta=0
    delta=0
    delta_final=0
    length=0
    s_length=1
    start = 0
    num1=int(input("Insert 1st number:"))
    start_s = num1
    while num1!=-1 and num1>0:
        num2=int(input("Insert next number, end with -1:"))
        if num2==-1 or num2<0: 
            num1=num2
        else:
            s_delta=num2-num1
            s_length+=1
            if s_delta!=delta:
                if s_length>length:
                    delta_final=delta
                    start_s = start
                    length=s_length-1
                s_length=2
                start = num1
            delta=s_delta
            num1=num2
    
    if s_length<=length:
        start = start_s
        s_length = length
        delta = delta_final
        
        
    if num1==-1:
        print("Longest mathematical series start with %d, delta of %d, length of %d"%(start,delta_final,s_length))
    else:
        print("Illegal data!")
main()
        
    