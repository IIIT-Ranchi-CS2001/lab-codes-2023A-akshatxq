#problem 1
s = input("enter the sentence :")
arr = s.split(" ")
cnt=0
for i in range(len(arr)):
    if(arr[i]==arr[i][::-1]):
        cnt+=1
print("the number of palindrome present :",cnt)
print("*********************************************************")

#problem 2
brr = []
sum=0
n= int(input("enter the size of list :"))
for i in range(0, n):
    element = int(input())
    sum+=element
    brr.append(element) 
mean = sum/n 
print("mean is : ",mean)
brr.sort()
n = len(brr)
if n % 2 == 0:
    median = (brr[n // 2 - 1] + brr[n // 2]) / 2
    print("median is:", median)
else:
    median = brr[n // 2]
    print("median is:", median)
mode = 3*median -2*mean
print("mode is : ",mode)
print("*********************************************************")

#problem 3
course_codes = ["CS1001", "CS1002", "CS1003"]
course_names = ["python", "dsa", "algorithms"]
combined_courses = []
for i in range(len(course_codes)):
    combined_courses.append(f"{course_codes[i]}:{course_names[i]}")
print(combined_courses)
print("*********************************************************")

#problem 4
singers = {'eena', 'meena', 'deeca', 'salu'}
dancers = {'chintu', 'raju', 'motu', 'chotu'}
singers_set = {singer for singer in singers}
dancers_set = {dancer for dancer in dancers}
all_artists = singers_set.union(dancers_set)
allrounders = singers_set.intersection(dancers_set)
dancers_not_singers = dancers_set.difference(singers_set)
singers_not_dancers = singers_set.difference(dancers_set)
dancers_not_singers_combined = dancers_not_singers.union(singers_not_dancers)
print("all artists in the class:", all_artists)
print("all rounders in the class:", allrounders)
print("dancers but not singers:", dancers_not_singers)
print("singers but not dancers:", singers_not_dancers)
print("combined dancers but not singers and singers but not dancers:", dancers_not_singers_combined)
print("*********************************************************")



