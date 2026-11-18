import numpy as np
import pandas as pd

print("My Python project is working!")

# NumPy example
numbers = np.array([10, 20, 30, 40, 50])

print("Array:", numbers)
print("Mean:", np.mean(numbers))

# Pandas example
data = {
    "Name": ["Amit", "Rahul", "Priya"],
    "Age": [22, 25, 23]
}

df = pd.DataFrame(data)

print(df)