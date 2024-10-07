def calculator():
    print("Welcome to the Calculator")
    
    while True:
        print("Please enter number")
        x = float(input("First number: "))
        
        print("Please enter number")
        y = float(input("Second number: "))
        
        print("Select operation:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Exit")
        
        choice = input("Enter choice (1/2/3/4/5): ")
        
        if choice == '5':
            print("Thank you for using the calculator. Goodbye!")
            break
        
        if choice in ('1', '2', '3', '4'):
            if choice == '1':
                result = x + y
                operation = '+'
            elif choice == '2':
                result = x - y
                operation = '-'
            elif choice == '3':
                result = x * y
                operation = '*'
            elif choice == '4':
                if y != 0:
                    result = x / y
                    operation = '/'
                else:
                    print("Error: Division by zero!")
                    continue
            
            print(f"Output: {x} {operation} {y} = {result}")
        else:
            print("Invalid input. Please try again.")
        
        print("\n")  # Add a blank line for readability

if __name__ == "__main__":
    calculator()
