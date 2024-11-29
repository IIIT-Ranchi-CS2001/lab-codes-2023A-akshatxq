print("********************************")
# PROBLEM 1:-

point1 = (1, 2, 3)
point2 = (4, 5, 6)
distance = ((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2 + (point2[2] - point1[2])**2)**(1/2)

print("THE DISTANCE IS :",distance)
print("********************************")

# PROBLEM 2,3,4 DELETED

# PROBLEM 5:-
points = [tuple(map(float, input(f"ENTER THE COORDINATE: ").split(' '))) for i in range(2)]
(x1, y1), (x2, y2) = points
if x1 == x2:
    print("THE LINE IS VERTICAL")
else:
    slope = (y1 - y2) / (x1 - x2)
    b = y1 - slope * x1
    print(f"EQUATION IS : y = {slope:.1f}x + {b:.1f}")
print("********************************")

# PROBLEM 6:-
s = str(input("ENTER THE STRING :"))
count = {}
for char in s:
    if char in count:
        count[char] += 1
    else:
        count[char] = 1
print(count)
print("********************************")

# PROBLEM 7:-
customer_names = [f'Customer {i}' for i in range(1, 6)]
customer_ids = [f'ID-{i}' for i in range(1, 6)]
shopping_points = [i * 10 for i in range(1, 6)]
# WITHOUT ZIP()
customer_tuples_without_zip = [(customer_names[i], customer_ids[i], shopping_points[i]) for i in range(len(customer_names))]
# WITH ZIP()
customer_tuples_with_zip = list(zip(customer_names, customer_ids, shopping_points))

print("CUSTOMER NAMES:", customer_names)
print("CUSTOMER IDs:", customer_ids)
print("SHOPPING POINTS:", shopping_points)
print("TUPLES WITHOUT ZIP:", customer_tuples_without_zip)
print("TUPLES WITH ZIP:", customer_tuples_with_zip)
print("********************************")

#PROBLEM 8:-

# WITH SORTED()
sorted_data = sorted(customer_names)
print("SORTED WITH sorted():", customer_names)
# WITHOUT SORTED()
customer_names.sort()
print("SORTED WITHOUT sorted():", customer_names)
print("********************************")

