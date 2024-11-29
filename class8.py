import numpy as np
import matplotlib.pyplot as plt

# Given data for daily COVID-19 cases across 5 countries over 7 days
covid_data = np.array([
    [1500, 2000, 1800, 1200, 900],   # Day 1
    [1600, 2100, 1900, 1300, 950],   # Day 2
    [1700, 2200, 2000, 1400, 1000],  # Day 3
    [1650, 2150, 1950, 1350, 980],   # Day 4
    [1750, 2250, 2050, 1450, 1020],  # Day 5
    [1800, 2300, 2100, 1500, 1050],  # Day 6
    [1900, 2400, 2200, 1600, 1100]   # Day 7
])

# 1. Calculate the total number of cases for each country over the 7 days
total_cases_per_country = np.sum(covid_data, axis=0)

# Print the total cases for each country
print("Total cases for each country over 7 days:")
for i, total_cases in enumerate(total_cases_per_country, start=1):
    print(f"Country_{i}: {total_cases}")

# 2. Determine the country with the highest total cases
country_with_highest_cases = np.argmax(total_cases_per_country) + 1  # +1 to make it 1-based index
highest_cases = total_cases_per_country[country_with_highest_cases - 1]

# Print the country with the highest number of cases
print(f"\nCountry with the highest total cases: Country_{country_with_highest_cases} with {highest_cases} cases")

# 3. Calculate the average number of cases reported per day across all countries
average_cases_per_day = np.mean(covid_data)

# Print the average number of cases per day
print(f"\nAverage number of cases reported per day across all countries: {average_cases_per_day:.2f}")

# 4. Identify the day with the highest total number of cases across all countries
total_cases_per_day = np.sum(covid_data, axis=1)  # Sum cases for each day across all countries

# Find the day with the maximum total cases
day_with_highest_cases = np.argmax(total_cases_per_day) + 1  # +1 to make it 1-based index
highest_total_cases = total_cases_per_day[day_with_highest_cases - 1]

# Print the day with the highest total cases
print(f"Day with the highest total cases: Day {day_with_highest_cases} with {highest_total_cases} cases")

# 5. Calculate the percentage increase or decrease in cases for each country from Day 1 to Day 7
percentage_change_per_country = ((covid_data[6] - covid_data[0]) / covid_data[0]) * 100

# Print the percentage change for each country
print("\nPercentage increase or decrease in cases from Day 1 to Day 7 for each country:")
for i, pct_change in enumerate(percentage_change_per_country, start=1):
    print(f"Country_{i}: {pct_change:.2f}%")

# 6. Find the country with the highest percentage increase
country_with_highest_pct_increase = np.argmax(percentage_change_per_country) + 1
highest_pct_increase = percentage_change_per_country[country_with_highest_pct_increase - 1]

# Print the country with the highest percentage increase
print(f"\nCountry with the highest percentage increase: Country_{country_with_highest_pct_increase} with {highest_pct_increase:.2f}% increase")

# 7. Data Transformation: Normalize the data (scale all values between 0 and 1)
# We normalize each country's data (along the columns) using Min-Max scaling
normalized_data = (covid_data - covid_data.min(axis=0)) / (covid_data.max(axis=0) - covid_data.min(axis=0))

# Print the normalized dataset
print("\nNormalized data (values between 0 and 1):")
print(normalized_data)

# 8. Visualize the data: Line chart showing daily cases for each country
plt.figure(figsize=(10, 6))

# Plotting each country's data
for i in range(covid_data.shape[1]):
    plt.plot(covid_data[:, i], label=f"Country_{i+1}")

# Highlight the day with the highest total cases using an annotation
plt.annotate(f"Day {day_with_highest_cases}", 
             xy=(day_with_highest_cases-1, highest_total_cases), 
             xytext=(day_with_highest_cases-2, highest_total_cases + 500),
             arrowprops=dict(facecolor='red', arrowstyle='->'),
             fontsize=12, color='red')

# Add titles and labels
plt.title("Daily COVID-19 Cases for Each Country")
plt.xlabel("Day")
plt.ylabel("Number of Cases")
plt.legend()

# Show the plot
plt.grid(True)
plt.show()
