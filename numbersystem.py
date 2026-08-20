print("Welcome to the Number System Converter!")
print("This tool allows you to convert numbers between different numeral systems. Supported systems include binary, octal, decimal, and hexadecimal.")

print("\nPlease select the source numeral system:")
print("1. Decimal")  
print("2. Binary")
print("3. Octal")
print("4. Hexadecimal")

source_choice = input("Enter the number corresponding to your choice (1-4): ")
while source_choice not in ['1', '2', '3', '4']:
    print("Invalid choice. Please select a valid option (1-4).")
    source_choice = input("Enter the number corresponding to your choice (1-4): ")

if source_choice == '1':
    decimal_number = input("Enter the decimal number to convert: ")
    conversion_choice = input("Enter the target numeral system (binary, octal, hexadecimal): ").lower()

    while conversion_choice not in ['binary', 'octal', 'hexadecimal']:
        print("Invalid choice. Please select a valid target numeral system.")
        conversion_choice = input("Enter the target numeral system (binary, octal, hexadecimal): ").lower()

    if conversion_choice == 'binary':
        binary_result = bin(int(decimal_number))[2::]
        print(f"The binary representation of {decimal_number} is: {binary_result}")
    if conversion_choice == 'octal':
        octal_result = oct(int(decimal_number))[2::]    
        print(f"The octal representation of {decimal_number} is: {octal_result}")
    if conversion_choice == 'hexadecimal':
        hexadecimal_result = hex(int(decimal_number))[2::]
        print(f"The hexadecimal representation of {decimal_number} is: {hexadecimal_result}")



elif source_choice == '2':
    binary_number = input("Enter the binary number to convert: ")
    conversion_choice = input("Enter the target numeral system (decimal, octal, hexadecimal): ").lower()

    while conversion_choice not in ['decimal', 'octal', 'hexadecimal']:
        print("Invalid choice. Please select a valid target numeral system.")
        conversion_choice = input("Enter the target numeral system (decimal, octal, hexadecimal): ").lower()

    if conversion_choice == 'decimal':
        decimal_result = int(binary_number, 2)
        print(f"The decimal representation of {binary_number} is: {decimal_result}")
    elif conversion_choice == 'octal':
        octal_result = oct(int(binary_number, 2))[2::]
        print(f"The octal representation of {binary_number} is: {octal_result}")
    elif conversion_choice == 'hexadecimal':
        hexadecimal_result = hex(int(binary_number, 2))[2::]
        print(f"The hexadecimal representation of {binary_number} is: {hexadecimal_result}")

elif source_choice == '3':
    octal_number = input("Enter the octal number to convert: ")
    conversion_choice = input("Enter the target numeral system (decimal, binary, hexadecimal): ").lower()

    while conversion_choice not in ['decimal', 'binary', 'hexadecimal']:
        print("Invalid choice. Please select a valid target numeral system.")
        conversion_choice = input("Enter the target numeral system (decimal, binary, hexadecimal): ").lower()

    if conversion_choice == 'decimal':
        decimal_result = int(octal_number, 8)
        print(f"The decimal representation of {octal_number} is: {decimal_result}")
    elif conversion_choice == 'binary':
        binary_result = bin(int(octal_number, 8))[2::]
        print(f"The binary representation of {octal_number} is: {binary_result}")
    elif conversion_choice == 'hexadecimal':
        hexadecimal_result = hex(int(octal_number, 8))[2::]
        print(f"The hexadecimal representation of {octal_number} is: {hexadecimal_result}")

elif source_choice == '4':
    hexadecimal_number = input("Enter the hexadecimal number to convert: ")
    conversion_choice = input("Enter the target numeral system (decimal, binary, octal): ").lower()

    while conversion_choice not in ['decimal', 'binary', 'octal']:
        print("Invalid choice. Please select a valid target numeral system.")
        conversion_choice = input("Enter the target numeral system (decimal, binary, octal): ").lower()

    if conversion_choice == 'decimal':
        decimal_result = int(hexadecimal_number, 16)
        print(f"The decimal representation of {hexadecimal_number} is: {decimal_result}")
    elif conversion_choice == 'binary':
        binary_result = bin(int(hexadecimal_number, 16))[2::]
        print(f"The binary representation of {hexadecimal_number} is: {binary_result}")
    elif conversion_choice == 'octal':
        octal_result = oct(int(hexadecimal_number, 16))[2::]
        print(f"The octal representation of {hexadecimal_number} is: {octal_result}")