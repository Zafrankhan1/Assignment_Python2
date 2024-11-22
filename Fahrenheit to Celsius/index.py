# Prompt the user to enter a temperature in Fahrenheit
fahrenheit = float(input("Enter temperature in Fahrenheit: "))

# Convert Fahrenheit to Celsius using the formula
celsius = (fahrenheit - 32) * 5.0 / 9.0

# Output the temperature in both Fahrenheit and Celsius
print(f"Temperature: {fahrenheit}F = {celsius}C")
