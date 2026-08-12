# Shipping Cost Calculator
# Added by: Aditya Barnwal

# Input package weight and shipping rate
weight = float(input("Enter package weight in kg: "))
rate = float(input("Enter shipping rate per kg: "))

# Calculate total shipping cost
shipping_cost = weight * rate

# Display the result
print(f"Total Shipping Cost: ${shipping_cost}")