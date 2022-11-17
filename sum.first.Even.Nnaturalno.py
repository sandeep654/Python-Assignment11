#Write a python script to calculate sum of first N Even natural numbers
N=int(input("Enter N Natural number:"))
i=0
for e in range(2,(N+1)*2,2):
    i=e+i
print("Sum of Square first n natural number",i)