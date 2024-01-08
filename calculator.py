no=int(input("Enter the ist number on which you want to perform the operation\n"))
no1=int(input("Enter the 2nd number on which you want to peform the operation\n"))
a=input("select the operator(+/-/*/%)\n")
if a == '+' :
 print(f" {no}+{no1}= {no+no1}")
elif a == '-' :
  print(f"{no}-{no1}= {no-no1}")
elif a == '*' :
  print(f"{no}*{no1}= {no*no1}")
elif a == '%' :
   print(f"The remainder of the no's {no}%{no1} are  {no%no1}")

