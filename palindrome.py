num=int(input("Enter a number"))
original_number=num

reversed_number=0

while num>0:
    digit=num%10
    reversed_number=(reversed_number*10)+digit
    num//=10
if original_number==reversed_number:
    print("The number is a palindrome")
else:
    print("The number is not a palindrome")
    
