
import math
s1="Maha Bharat"
print(s1.swapcase()) #“mAHA bHARAT”
print(s1.split(" ")[1]) #“Bharat”
print(s1.split(" ")[1]*3) #“BharatBharatBharat”
print("Mera "+s1.split(" ")[1]) #“Mera Bharat”
print("Mera "+s1.split(" ")[1]+" Mahan") #“Mera Bharat Mahan”
print("-------------------------")

s="Ba Ba Black Sheep"
print(len(s)) #The length of the string s
print(s.find("e")) #The first occurrence of the letter ‘e’
print(s.count("a")) #The total number of occurrences of ‘a’
print("Ta"+" Ta "+s.split(" ")[2]+" "+s.split(" ")[3]) #Generate “Ta Ta Black Sheep”
print("-------------------------")

y=str(input("enter the string :"))
z=y[::-1]
if(y == z):
    print("palindrome")
else:
    print("not a palindrome")
print("-------------------------")


name=str(input("enter your name :"))
roll_no = int(input("enter your roll number :"))
marks = int(input("enter your marks :"))
if(marks >= 90):
    gp = 10
    remarks = "OUTSTANDING"
elif(marks>=80 and marks<90):
    gp = 9
    remarks = "VERY GOOD"
elif(marks>=70 and marks<80):
    gp=8
    remarks="GOOD"
elif(marks>=60 and marks<70):
    gp=7
    remarks = "AVERAGE"
elif(marks>=50 and marks<60):
    gp=6
    remarks = "PASS"
else:
    gp = 0
    remarks = "FAIL"
print("name is :",name)
print("roll number is :",roll_no)
print("marks is :",marks)
print("grade point is :",gp)
print("remarks is :",remarks)
print("-------------------------")


a = int(input("enter a :"))
b = int(input("enter b :"))
c = int(input("enter c :"))
d = b*b - 4*a*c
if(d==0):
    print("one real repeated root :",-b/(2*a))
elif(d>0):
    print("distinct real roots are :",(-b+math.sqrt(d))/(2*a),"and ",(-b-math.sqrt(d))/(2*a))
else:
    print("complex root with real parts is ",-b / (2 * a) ,"and the imaginary part is ",math.sqrt(-d) / (2 * a))
print("-------------------------")