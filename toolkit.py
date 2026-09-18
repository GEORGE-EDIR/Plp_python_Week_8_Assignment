# Personal Mini-Toolkit
# A simple program containing three useful tools.


# Tool 1: Simple Calculator
# Performs basic arithmetic with two numbers.
def calculator():
    print("\n--- Simple Calculator ---")

    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Please enter valid numbers.")
        return

    operation = input("Enter an operation (+, -, *, /): ")

    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        if num2 == 0:
            print("Sorry, you cannot divide by zero.")
            return
        result = num1 / num2
    else:
        print(f"'{operation}' is not a valid operation.")
        return

    print(f"Result: {num1} {operation} {num2} = {result}")


# Tool 2: To-Do List
# Allows the user to add, view, and remove tasks.
def todo_list():
    tasks = []

    while True:
        print("\n--- To-Do List ---")
        print("1. Add task")
        print("2. View tasks")
        print("3. Remove task")
        print("4. Back to main menu")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            task = input("Enter a task: ").strip()

            if task:
                tasks.append(task)
                print(f"Task '{task}' added successfully.")
            else:
                print("Please enter a task.")

        elif choice == "2":
            if len(tasks) == 0:
                print("Your to-do list is empty.")
            else:
                print("\nYour tasks:")

                number = 1

                for task in tasks:
                    print(f"{number}. {task}")
                    number = number + 1

        elif choice == "3":
            task = input("Enter the task to remove: ").strip()

            if task in tasks:
                tasks.remove(task)
                print(f"Task '{task}' removed successfully.")
            else:
                print(f"'{task}' is not on your list.")

        elif choice == "4":
            print("Returning to the main menu...")
            break

        else:
            print(f"'{choice}' is not a valid option.")


# Tool 3: Number Checker
# Checks whether a number is positive, negative, zero, even, or odd.
def number_checker():
    print("\n--- Number Checker ---")

    try:
        number = int(input("Enter a whole number: "))
    except ValueError:
        print("Please enter a valid whole number.")
        return

    if number > 0:
        print(f"{number} is positive.")
    elif number < 0:
        print(f"{number} is negative.")
    else:
        print(f"{number} is zero.")

    if number % 2 == 0:
        print(f"{number} is even.")
    else:
        print(f"{number} is odd.")


# Main menu
# Keeps displaying the menu until the user chooses Quit.
def main():
    print("\n====================================")
    print("   Welcome to the Personal Toolkit!")
    print("====================================")

    while True:
        print("\n===== PERSONAL MINI-TOOLKIT =====")
        print("1. Simple Calculator")
        print("2. To-Do List")
        print("3. Number Checker")
        print("4. Quit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            calculator()

        elif choice == "2":
            todo_list()

        elif choice == "3":
            number_checker()

        elif choice == "4":
            print("\nThanks for using the Personal Mini-Toolkit!")
            print("Goodbye!")
            break

        else:
            print(f"Sorry, '{choice}' is not on the menu.")
            print("Please choose an option from 1 to 4.")


# Run the program
if __name__ == "__main__":
    main()