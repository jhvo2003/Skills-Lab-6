name = input("What is your name?")
temperature = input("What is the temperature outside right now?:")
c_f = int(input("Input 0 if this temperature is Celsius and input 2 if this temperature is in Fahrenheit: " ))
if (c_f == 0):
    Fahrenheit = (c_f * (9/5)) + 32
    print("This temperature in Fahrenheit is ", Fahrenheit)