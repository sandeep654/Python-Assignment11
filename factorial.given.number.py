#Write a python script to calculate factorial of a given number
N=int(input("Enter N Natural number:"))
i=1
for e in range(N,0,-1):
    i=e*i
print("Sum of cube first n natural number",i)