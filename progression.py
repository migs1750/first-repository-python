def arithmetic_seq(start, difference, n_term):
    sequence = []

    for n in range(n_term):
        term = start + n * difference
        sequence.append(term)
    return sequence

def arithmetic_sum(start, difference, n_term):
     for n in range(n_term):
        term = (n_term / 2) * (2 * start + (n_term - 1) * difference)   
     return term
def geometric_seq(start, ratio, n_term):
    sequence = []

    for n in range(n_term):
        term = start * (ratio ** n)
        sequence.append(term)
    return sequence

def geometric_sum(start, ratio, n_term):
    if ratio == 1:
        return n_term * start
    else:
        return start * (1 - ratio ** n_term) / (1 - ratio)

print("Progression Calculator")

choice = input(
    "Enter the type of progression you want (arithmetic/geometric): "
).strip().lower()

while choice not in ["arithmetic" , "arithmetic series" , "geometric" , "geometric series"]:
    choice = input(
    "Invalid. Enter the type of progression you want (arithmetic/geometric): "
).strip().lower()
    

if choice == "arithmetic":
    first_term = int(input("Enter the first term: "))
    common_difference = int(input("Enter the common difference: "))
    nth_term = int(input("Enter the number of terms: "))

    result = arithmetic_seq(first_term, common_difference, nth_term)

    print("Arithmetic sequence:", result)
   
if choice == "arithmetic series":
    first_term = int(input("Enter the first term: "))
    common_difference = int(input("Enter the common difference: "))
    nth_term = int(input("Enter the number of terms: "))

    result = arithmetic_sum(first_term, common_difference, nth_term)
    print("The arithmetic series for that is" , result)

if choice == "geometric":
    first_term = int(input("Enter the first term: "))
    common_ratio = int(input("Enter the common ratio: "))
    nth_term = int(input("Enter the number of terms: "))

    result = geometric_seq(first_term, common_ratio, nth_term)

    print("Geometric sequence:", result)

if choice == "geometric series":
    first_term = int(input("Enter the first term: "))
    common_ratio = int(input("Enter the common ratio: "))
    nth_term = int(input("Enter the number of terms: "))

    result = geometric_sum(first_term, common_ratio, nth_term)
    print("The geometric series for that is" , result)
