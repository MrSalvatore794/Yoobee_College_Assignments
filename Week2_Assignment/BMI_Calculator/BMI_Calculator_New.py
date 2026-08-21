# BMI Calculator New 13/08/2026

class BMI_Calculator:
    def set_data(self, weight, height):
        self.weight = weight
        self.height = height

    def calculate_bmi(self):
        bmi = self.weight / (self.height ** 2)
        return round(bmi, 2)

    def get_category(self):
        bmi = self.calculate_bmi()
        if bmi < 18.5:
            return "Underweight"
        elif bmi < 25.0:
            return "Normal weight"
        elif bmi < 30.0:
            return "Overweight"
        else:
            return "Obesity"


def main():
    weight = float(input("Enter your weight in kilograms: "))
    height = float(input("Enter your height in meters (e.g., 1.75): "))

    bmi_calculator = BMI_Calculator()
    bmi_calculator.set_data(weight, height)
    bmi_value = bmi_calculator.calculate_bmi()
    category = bmi_calculator.get_category()

    print(f"Your BMI is: {bmi_value}")
    print(f"Category: {category}")


if __name__ == "__main__":
    main()