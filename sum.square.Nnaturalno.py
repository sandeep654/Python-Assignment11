#Write a python script to calculate sum of squares of first N natural numbers
N=int(input("Enter N Natural number:"))
i=0
for e in range(1,N+1,1):
    i=(e**2)+i
print("Sum of Square first n natural number",i)