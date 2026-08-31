def decimal_to_other_systems():
    decimal_number = input("Enter the decimal number to convert: ")
    conversion_choice = input("Choose the target number system (binary, octal, hexadecimal): ").lower()
    while conversion_choice not in ['binary', 'octal', 'hexadecimal']:
        print("Invalid choice. Please choose from binary, octal, or hexadecimal.")
        conversion_choice = input("Choose the target number system (binary, octal, hexadecimal): ").lower()

    if conversion_choice == 'binary':
        
        binary_result = bin(int(decimal_number))[2::]
        print("The binary representation of" ,decimal_number , "is: " ,binary_result)
    if conversion_choice == 'octal':
        octal_result = oct(int(decimal_number))[2::]    
        print("The octal representation of" ,decimal_number , "is: " ,octal_result)   
    if conversion_choice == 'hexadecimal':
        hexadecimal_result = hex(int(decimal_number))[2::]
        print("The hexadecimal representation of" ,decimal_number , "is: " ,hexadecimal_result) 

def binary_to_other_systems():
    binary_number = input("Enter the binary number to convert: ")
    conversion_choice = input("Choose the target number system (decimal, octal, hexadecimal): ").lower()
    while conversion_choice not in ['decimal', 'octal', 'hexadecimal']:
        print("Invalid choice. Please choose from decimal, octal, or hexadecimal.")
        conversion_choice = input("Choose the target number system (decimal, octal, hexadecimal): ").lower()

    if conversion_choice == 'decimal':
        decimal_result = int(binary_number, 2)
        print("The decimal representation of" ,binary_number , "is: " ,decimal_result)
    elif conversion_choice == 'octal':
        octal_result = oct(int(binary_number, 2))[2::]
        print("The octal representation of" ,binary_number , "is: " ,octal_result)
    elif conversion_choice == 'hexadecimal':
        hexadecimal_result = hex(int(binary_number, 2))[2::]
        print("The hexadecimal representation of" ,binary_number , "is: " ,hexadecimal_result)

def octal_to_other_systems():
    octal_number = input("Enter the octal number to convert: ")
    conversion_choice = input("Choose the target number system (decimal, binary, hexadecimal): ").lower()
    while conversion_choice not in ['decimal', 'binary', 'hexadecimal']:
        print("Invalid choice. Please choose from decimal, binary, or hexadecimal.")
        conversion_choice = input("Choose the target number system (decimal, binary, hexadecimal): ").lower()

    if conversion_choice == 'decimal':
        decimal_result = int(octal_number, 8)
        print("The decimal representation of" ,octal_number , "is: " ,decimal_result)
    elif conversion_choice == 'binary':
        binary_result = bin(int(octal_number, 8))[2::]
        print("The binary representation of" ,octal_number , "is: " ,binary_result)
    elif conversion_choice == 'hexadecimal':
        hexadecimal_result = hex(int(octal_number, 8))[2::]
        print("The hexadecimal representation of" ,octal_number , "is: " ,hexadecimal_result)

def hexadecimal_to_other_systems():
    hexadecimal_number = input("Enter the hexadecimal number to convert: ")
    conversion_choice = input("Choose the target number system (decimal, binary, octal): ").lower()
    while conversion_choice not in ['decimal', 'binary', 'octal']:
        print("Invalid choice. Please choose from decimal, binary, or octal.")
        conversion_choice = input("Choose the target number system (decimal, binary, octal): ").lower()

    if conversion_choice == 'decimal':
        decimal_result = int(hexadecimal_number, 16)
        print("The decimal representation of" ,hexadecimal_number , "is: " ,decimal_result)
    elif conversion_choice == 'binary':
        binary_result = bin(int(hexadecimal_number, 16))[2::]
        print("The binary representation of" ,hexadecimal_number , "is: " ,binary_result)
    elif conversion_choice == 'octal':
        octal_result = oct(int(hexadecimal_number, 16))[2::]
        print("The octal representation of" ,hexadecimal_number , "is: " ,octal_result)







print("Hello welcome to the number system converter!")
source_choice = input("Choose the source number system (1: Decimal, 2: Binary, 3: Octal, 4: Hexadecimal): ")
while source_choice not in ['1', '2', '3', '4']:
    print("Invalid choice. Please choose from 1, 2, 3, or 4.")
    source_choice = input("Choose the source number system (1: Decimal, 2: Binary, 3: Octal, 4: Hexadecimal): ")

if source_choice == '1':
    decimal_to_other_systems()
elif source_choice == '2':
    binary_to_other_systems()
elif source_choice == '3':
    octal_to_other_systems()
elif source_choice == '4':
    hexadecimal_to_other_systems()
else:
    print("Invalid choice. Please choose from 1, 2, 3, or 4.")
    
