import pandas as pd

# Creating DataFrame using lists and dictionary
names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30, 35]
cities = ['New York', 'Los Angeles', 'Chicago']

data = {'Name': names, 'Age': ages, 'City': cities}
df = pd.DataFrame(data)

print("DataFrame from Lists Using Dictionary:")
print(df)