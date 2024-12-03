
# practical lab python code:-

import pandas as pd
import numpy as np

# getting the dataset
file_path = '/Users/akshat_singh/Downloads/AQI_data.csv' 
data = pd.read_csv(file_path)

# part 1-> displaying  information
# a. displaying the first 5 rows
print("first 5 rows of the dataset")
print(data.head())

# b. displaying the last 6 rows
print("\nlast 6 rows of the dataset")
print(data.tail(6))

# c. showing the summary statistics for all numeric columns
print("\nsummary statistics for numeric columns")
print(data.describe())

# d. computing mean AQI, PM2.5, and PM10 values for each city using numpy
print("\nmean AQI, PM2.5, and PM10 values for each city")
if 'City' in data.columns and all(col in data.columns for col in ['AQI', 'PM2.5', 'PM10']):
    city_means = data.groupby('City')[['AQI', 'PM2.5', 'PM10']].mean()
    print(city_means)
else:
    print("required columns for mean calculation are missing.")

# part 2-> grouping data by city and calculate average AQI and maximum PM10
# a. average AQI
# b. maximum PM10 level
grouped_data = data.groupby('City').agg(
    Average_AQI=('AQI', 'mean'),
    Max_PM10=('PM10', 'max')
)

# displaying grouped data
print("\ngrouped data by city with average AQI and maximum PM10 levels:")
print(grouped_data)

# saving grouped data in a csv file
output_file_path = '/Users/akshat_singh/Downloads/AQI_data_answer.csv'
grouped_data.to_csv(output_file_path)
print(f"\ngrouped data has been saved to {output_file_path}")
