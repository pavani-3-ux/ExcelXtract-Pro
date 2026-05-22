
import pandas as pd

# Read Excel file
data = pd.read_excel("employees.xlsx")

# Filter Electronics category
electronics = data[data["CATEGORY"] == "Electronics"]

# Print filtered data
print(electronics)

# Save filtered data
electronics.to_excel("electronics_products.xlsx", index=False)

print("Electronics data extracted successfully")