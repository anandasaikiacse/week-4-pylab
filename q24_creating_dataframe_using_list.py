import pandas as pd

# Creating a DataFrame from a list
data = [['Alice', 25], ['Bob', 30], ['Charlie', 35]]
df = pd.DataFrame(data, columns=['Name', 'Age'])

print("DataFrame from List:")
print(df)