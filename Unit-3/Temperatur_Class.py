class Temperature:

    def convertFahrenheit(self, celsius):
        fahrenheit = (celsius * 9/5) + 32
        return fahrenheit

    def convertCelsius(self, fahrenheit):
        celsius = (fahrenheit - 32) * 5/9
        return celsius

temp = Temperature()

c = 25
f = 77

print("Celsius to Fahrenheit:", temp.convertFahrenheit(c))
print("Fahrenheit to Celsius:", temp.convertCelsius(f))
