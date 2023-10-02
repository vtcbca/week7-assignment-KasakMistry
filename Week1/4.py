#4.Write a python script to enter any number, if it is integer number, then check its armstrong or not. Print appropriate message if it is not palindrom.

def armstong(n):
    n=int(n)
    rem=0
    sum=0
    a=n
    while(n!=0):
        rem=n%10
        sum=sum+(rem**3)
        n//=10
    if(a==sum):
        print(f"The number {a} is an armstrong number!")
    else:
        print(f"The number {a} is  not an armstrong number!")


num=input("Enter a number!!:")
if(num.isdigit()):
    armstong(num)
else:
    print(f"The given input {num} is not valid number!!")
