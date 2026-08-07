#BMI Calculator (Metric)


def calculate_bmi():
    # Ask the user for weight and height
    weight = float(input("Enter your weight in kilograms: "))
    height = float(input("Enter your height in meters (e.g., 1.75): "))

    # Formula: weight / (height * height)
    bmi = weight / (height**2)

    # Check which category the BMI falls into
    if bmi < 18.5:
        category = "Underweight"
    elif bmi < 25.0:
        category = "Normal weight"
    elif bmi < 30.0:
        category = "Overweight"
    else:
        category = "Obesity"

    # Round to 2 decimal places
    bmi = round(bmi, 2)

    return bmi, category


# Main program
bmi_value, category = calculate_bmi()

print("Your BMI is:", bmi_value)
print("Category:", category)