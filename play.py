import pandas as pd



# Import the data as a Pandas DataFrame. Name the DataFrame bike_df. Then, complete the following:
#
# Delete the unnecessary columns:
# Unnamed: 7
# Unnamed: 8
# Unnamed: 9
bike_df = pd.read_csv('Bikes.csv')
print(bike_df.keys())
bike_df = bike_df.drop(columns=['Unnamed: 7', 'Unnamed: 8', 'Unnamed: 9'])
print(bike_df.keys())

# 2. Rename the Unnamed: 6 column to percent_change
bike_df = bike_df.rename(columns={'Unnamed: 6': 'percent_change'})
print(bike_df.keys())

# 3. How many missing values are in the dataset? Which columns are they in?
print(bike_df.isna().sum())


# Fill all missing values in the 2021 Counts column with 0.
# Optional/Bonus: There is a challenging but common issue in the name for the 2019 counts column. 
# Can you find it? If so, Rename the 2019 counts (31 counters) column to "counts_2019" (a more Pythonic column name)


