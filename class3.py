#problem 1:-
n=int(input("enter a number : "))
print("Number     Square")
i = 1;
while(i <= n):
    print(i,"        ",i*i)
    i+=1

#problem 2:-
import math
num = int(input("enter a number : "))
sum=0;
while(num != 0):
    sum = sum + int(num%10);
    num = int(num/10);
print("the sum of digits is  : ",sum)

#problem 3:-
g = int(input("enter the number for fibonacci series :"))
cnt = 0;
n1=0;
n2=1;
while(cnt < g):
    print(n1);
    nth = n1 + n2;
    n1 = n2;
    n2 = nth;
    cnt+=1;

#problem 4:-
number = int(input("enter the number for multiplication table : "))
for x in range(10):
    print(number,"x",x+1,"=",number*(x+1))
    
#problem 5:-
str = str(input("enter the string : "))
if(str.isalnum()):
    print("True")
else:
    print("False")
    
#problem 6:-
text = (input("enter the string :"))
c = (input("enter the character :"))
j=0;
for char in text:
    if(char == c):
        j+=1;
print("the count is : ",j)
