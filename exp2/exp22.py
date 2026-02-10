# program to find factorial number
"""
Created on Tue Feb 10 07:18:29 2026

@author: sahil gujar
"""

n=int(input("enter number:"))

fact=1

for i in range(1,n+1):
    
    fact=fact*i

print("factorial:",fact)
