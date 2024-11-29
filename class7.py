#PROBLEM 1:-
import matplotlib.pyplot as plt

# Data for Madhya Pradesh and Rajasthan elections
states = ['Madhya Pradesh', 'Rajasthan']
parties_mp = ['BJP', 'INC', 'BSP', 'Others']
seats_mp = [163, 66, 0, 1]

parties_rj = ['INC', 'BJP', 'BSP', 'Others']
seats_rj = [69, 115, 2, 13]

# Colors for the pie chart slices
colors = ['#FF9999', '#66B3FF', '#99FF99', '#FFCC99']

# Create subplots: Pie chart 1 (Madhya Pradesh) and Pie chart 2 (Rajasthan)
fig, axs = plt.subplots(1, 2, figsize=(14, 7))

# Madhya Pradesh Pie Chart
axs[0].pie(seats_mp, labels=parties_mp, autopct='%1.1f%%', startangle=90, colors=colors, pctdistance=0.85)
axs[0].set_title('Madhya Pradesh Election Result')

# Detach the largest wedge (BJP) slightly
wedges, texts, autotexts = axs[0].pie(seats_mp, labels=parties_mp, autopct='%1.1f%%', startangle=90, colors=colors, pctdistance=0.85)
for i, wedge in enumerate(wedges):
    if parties_mp[i] == 'BJP':
        wedge.set_theta_offset(0)  # Offset the BJP slice
        wedge.set_edgecolor('black')
        wedge.set_linewidth(2)

# Rajasthan Pie Chart
axs[1].pie(seats_rj, labels=parties_rj, autopct='%1.1f%%', startangle=90, colors=colors, pctdistance=0.85)
axs[1].set_title('Rajasthan Election Result')

# Detach the largest wedge (BJP) slightly
wedges, texts, autotexts = axs[1].pie(seats_rj, labels=parties_rj, autopct='%1.1f%%', startangle=90, colors=colors, pctdistance=0.85)
for i, wedge in enumerate(wedges):
    if parties_rj[i] == 'BJP':
        wedge.set_theta_offset(0)  # Offset the BJP slice
        wedge.set_edgecolor('black')
        wedge.set_linewidth(2)

# Add Legends
fig.legend(parties_mp, loc="center left", bbox_to_anchor=(1, 0.5), title="Parties")

# Bar Chart: Seats comparison across both states
fig2, ax2 = plt.subplots(figsize=(10, 6))

# Combining both states' data into a single dataset for comparison
states_combined = ['BJP (MP)', 'INC (MP)', 'BSP (MP)', 'Others (MP)',
                   'INC (RJ)', 'BJP (RJ)', 'BSP (RJ)', 'Others (RJ)']
seats_combined = [163, 66, 0, 1, 69, 115, 2, 13]

# Creating the bar chart
ax2.bar(states_combined, seats_combined, color=colors)
ax2.set_xlabel('Party')
ax2.set_ylabel('Seats Won')
ax2.set_title('Seats Comparison: Madhya Pradesh and Rajasthan')

# Rotate x-axis labels for better readability
plt.xticks(rotation=45, ha="right")

# Add Legend
ax2.legend(['Madhya Pradesh', 'Rajasthan'], loc='upper left')

# Show plots
plt.tight_layout()
plt.show()


#PROBLEM 2:-
import random
import math
import matplotlib.pyplot as plt

# Function to check if a number is prime
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

# Function to check if a number is composite
def is_composite(num):
    return num > 1 and not is_prime(num)

# Function to generate random numbers and classify them into primes and composites
def generate_and_classify_numbers(K, N):
    # Generate K random numbers within the limit N
    random_numbers = [random.randint(1, N) for _ in range(K)]
    
    primes = [num for num in random_numbers if is_prime(num)]
    composites = [num for num in random_numbers if is_composite(num)]
    
    return primes, composites

# User input for K and N
K = int(input("Enter the number of random numbers to generate (minimum 10): "))
N = int(input("Enter the upper limit for the random numbers: "))

# Ensure K is at least 10
if K < 10:
    print("K must be at least 10. Setting K to 10.")
    K = 10

# Generate the list and classify the numbers
primes, composites = generate_and_classify_numbers(K, N)

# Calculate the squares of primes and square roots of composites
prime_squares = [p ** 2 for p in primes]
composite_sqrts = [math.sqrt(c) for c in composites]

# Plot the results
fig, axs = plt.subplots(1, 2, figsize=(14, 6))

# Prime numbers vs their squares
if primes:
    axs[0].scatter(primes, prime_squares, color='blue')
    axs[0].set_title('Prime Numbers vs Squares')
    axs[0].set_xlabel('Prime Numbers')
    axs[0].set_ylabel('Squares of Prime Numbers')

# Composite numbers vs their square roots
if composites:
    axs[1].scatter(composites, composite_sqrts, color='green')
    axs[1].set_title('Composite Numbers vs Square Roots')
    axs[1].set_xlabel('Composite Numbers')
    axs[1].set_ylabel('Square Roots of Composite Numbers')

# Show the plots
plt.tight_layout()
plt.show()
