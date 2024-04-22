print("<---------hello this is new programme-------->")
print("this programme tells you which number is the greatest among three values 'a', 'b', and 'c'.")
print("Please enter values for 'a', 'b', and 'c'.")
try:
    a = int(input("Value of 'a': "))
    b = int(input("Value of 'b': "))
    c = int(input("Value of 'c': "))
    
    if (a > b) and (a > c):
        print("a is greater than 'b' and 'c'.")
    elif (b > a) and (b > c):
        print("b is greater than 'a' and 'c'.")
    elif (c > a) and (c > b):
        print("c is greater than 'a' and 'b'.")
    else:
        print("Two or more values are equal.")
except ValueError:
    print("Invalid input. Please enter valid numbers for 'a', 'b', and 'c'.")
