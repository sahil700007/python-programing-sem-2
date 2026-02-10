# program to find out leap year
"""
created on tue feb 10 12:15:32 2026

@author:sahil gujar
"""
year = int(input("enter year:"))

if(year%400==0) or (year%4==0 and year%100!=0):
    
     print("leap year")
     
else:

     print("not a leap year")     
