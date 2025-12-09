history = []
def calculate(a,b,op):
  if op == "+":
    result = a+b
  elif op == "-":
    result = a-b
  elif op == "*":
    result = a*b
  elif op == "/":
    if b==0:
      return "Error: Division by zero"
    result = a/b
  else:
    return "invalid operator"
  history.append(result)
  return result
def get_history():
  return history
print("calculator(+ - * /)")
a=float(input("enter first number: "))
b=float(input("enter second number: "))
op=input("enter operator(+,-,*,/): ")
output = calculate(a,b,op)
print("result:",output)
print("\nhistory:",get_history())
