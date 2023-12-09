# Calculator
from art import logo
# Add
def add(n1, n2):
  return n1 + n2
# Subtract
def subtract(n1, n2):
  return n1 - n2
# Division 
def divide(n1, n2):
  return n1/n2
def multiply(n1, n2):
  return n1 * n2

# Mathematical operations to perform
# Here key is the operators and value is the above functions
# New Learning
operations = {
  "+" : add,
  "-" : subtract,
  "*" : multiply,
  "/" : divide,
  
}

def calculator():
  print(logo)
  contd = True
  # Getting the first input number
  num1 = float(input("What's the first number?: "))
  while contd:
  # Print the items in operations
    for operator in operations:
      print(operator)
  # Select the operation
    operation_symbol = input("Pick an   operation from the line above: ")
  # Getting the second input number
    num2 = float(input("What's the next number?: "))
  # New learning
    calculation_function = operations[operation_symbol]
    answer = calculation_function(num1, num2)

    print(f"{num1} {operation_symbol} {num2} = {answer}")
    #contd=input(f"Type 'y' to continue calculating with {answer}, or type 'n' to exit.: ")

    if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to exit.: ")=='y':
      num1= answer  
    else:
      contd = False
      calculator()

calculator()   
    