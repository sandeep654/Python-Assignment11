"""Write a python script to print binary equivalent of a given decimal number. (do not
use bin() method)"""
n=int(input("Enter decimal number:"))
bs=''
while n!=0:
    bs=bs+str(n%2)
    n=n//2
print("Decimal no. equal to binary no. is")
for i in range(len(bs)-1,-1,-1):
    print(bs[i],end=' ')