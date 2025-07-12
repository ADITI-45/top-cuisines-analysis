

import pandas as pd

import pandas as pd

# Read the Excel file into a pandas DataFrame
df = pd.read_excel("/content/restaurant.csv.xlsx")

# Display the first few rows of the DataFrame and its columns
display(df.head())
display(df.info())

# Split the 'Cuisines' column by comma and stack the results
all_cuisines = df['Cuisines'].str.split(',').explode()

# Remove leading and trailing spaces from each cuisine
all_cuisines = all_cuisines.str.strip()

# Count the occurrences of each cuisine and get the top 3
top_3_cuisines = all_cuisines.value_counts().head(3)

# Display the result
print("Top 3 Most Common Cuisines:")
display(top_3_cuisines)