#Write a python script to calculate sum of first N natural numbers
N=int(input("Enter N natural number:"))
i=0
for e in range(1,N+1,1):
    i=e+i
print("Sum of first N natural number",i)