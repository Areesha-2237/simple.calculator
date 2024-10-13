import streamlit as st

# Simple Calculator using Streamlit

# Function for Addition
def add(x, y):
    return x + y

# Function for Subtraction
def subtract(x, y):
    return x - y

# Function for Multiplication
def multiply(x, y):
    return x * y

# Function for Division
def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

# Main Streamlit app function
def calculator():
    st.title("Simple Calculator App")

    # Dropdown for selecting the operation
    operation = st.selectbox("Choose an operation:", ["Add", "Subtract", "Multiply", "Divide"])
    
    # Input fields for numbers
    num1 = st.number_input("Enter the first number:", format="%f")
    num2 = st.number_input("Enter the second number:", format="%f")

    # Button to calculate
    if st.button("Calculate"):
        if operation == "Add":
            result = add(num1, num2)
        elif operation == "Subtract":
            result = subtract(num1, num2)
        elif operation == "Multiply":
            result = multiply(num1, num2)
        elif operation == "Divide":
            result = divide(num1, num2)
        
        # Display the result
        st.success(f"The result is: {result}")

# Run the Streamlit app
if __name__ == "__main__":
    calculator()
