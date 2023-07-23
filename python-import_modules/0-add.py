if __name__ == "__main__":
    a = 1
    b = 2

    # Import the add function from add_0.py
    from add_0 import add

    # Calculate the result using the add function
    result = add(a, b)

    # Display the result using string formatting
    print(f"{a} + {b} = {result}")

