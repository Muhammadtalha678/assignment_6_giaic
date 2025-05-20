class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(c):
        return (c * 9/5) + 32
    
tc = TemperatureConverter()

print(tc.celsius_to_fahrenheit(40))
print(TemperatureConverter.celsius_to_fahrenheit(35))