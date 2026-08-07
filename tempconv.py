#This is a program that Converts C to F
print("Hello, Welcome to C to F converter")

choice = input("Enter what unit is it: ")


if choice == "Celsius" or choice == "celsius":
    print("Okay this will be converted to fahrenheit")
    number = float(input("Enter the value: "))
    convFahn = (9/5 * number) + 32
    print("The value of the temperature in fahrenheit is" , convFahn)
    
    
elif choice == "Fahrenheit" or choice == "fahrenheit":
    print("Okay this will be converted to celsius")
    number = float(input("Enter the value: "))
    convcels = (number-32) * 5/9
    print("The value of the temperature in celsius is" , convcels)
    
else:
    print("#This is a program that Converts C to F")
print("Hello, Welcome to C to F converter")

choice = input("Enter what unit is it: ")


if choice == "Celsius" or choice == "celsius":
    print("Okay this will be converted to fahrenheit")
    number = float(input("Enter the value: "))
    convFahn = (9/5 * number) + 32
    print("The value of the temperature in fahrenheit is" , convFahn)
    print("Thank you for using this program")
          
    
    
elif choice == "Fahrenheit" or choice == "fahrenheit":
    print("Okay this will be converted to celsius")
    number = float(input("Enter the value: "))
    convcels = (number-32) * 5/9
    print("The value of the temperature in celsius is" , convcels)
    print("Thank you for using this program")
    
else:
    print("Error")
