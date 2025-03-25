import pandas as pd

# Creating a DataFrame from a dictionary of ndarrays/lists
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}

df = pd.DataFrame(data)

print("DataFrame from Dictionary of ndarrays/lists:")
print(df)