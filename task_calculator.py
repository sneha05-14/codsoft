print("Welcom to Calculator!")
num1=float(input("Enter first number"))
opr=input("Select an operation{+,-,*,/}")
num2=float(input("Enter second number"))
if opr=="+":
  result=num1+num2
  print("The result of",num1,"+",num2,"is",result)
elif opr=="-":
  result=num1-num2
  print("The result of",num1,"-",num2,"is",result)
elif opr=="*":
  result=num1*num2
  print("The result of",num1,"*",num2,"is",result)
elif opr=="/":
  result=num1/num2
  print("The result of",num1,"/",num2,"is",result)
else:
  print("Oops!Incorrect opererator selected")
  print("Exit.")
