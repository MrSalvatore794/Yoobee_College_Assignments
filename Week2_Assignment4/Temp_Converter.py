# Temperature Converter from F to C and C to F
class TemperatureConverter:
    def __init__(self, temperature):
        self.temperature = temperature

    def to_celsius(self):
        """Convert Fahrenheit to Celsius."""
        return (self.temperature - 32) * 5.0 / 9.0

    def to_fahrenheit(self):
        """Convert Celsius to Fahrenheit."""
        return (self.temperature * 9.0 / 5.0) + 32

    def convert(self, user_input):
        """Determine the conversion direction based on user input."""
        if user_input == 'f':
            return self.to_celsius()
        elif user_input == 'c':
            return self.to_fahrenheit()
        else:
            raise ValueError("Invalid input. Please enter 'F' for Fahrenheit or 'C' for Celsius.")


def main():
    """Main function to run the temperature converter."""
    user_input = input("Enter 'F' to convert from Fahrenheit to Celsius or 'C' to convert from Celsius to Fahrenheit: ").strip().lower()
    
    try:
        temperature = float(input("Enter the temperature value: "))
        converter = TemperatureConverter(temperature)
        result = converter.convert(user_input)
        
        if user_input == 'f':
            print(f"{temperature}°F is {result:.2f}°C")
        else:
            print(f"{temperature}°C is {result:.2f}°F")
            
    except ValueError as e:
        print(e)


# Execute the main function
if __name__ == "__main__":
    main()