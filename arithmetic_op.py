n1=int(input("Enter your first number =>"))
n2=int(input("Enter your second number =>"))
sig=input("Enter your operation")
match sig:
    case '+':
        ans=n1+n2
        print("Addition:",ans)
    case '-':
        ans=n1-n2
        print("Subtraction:",ans)
    case '*':
        ans=n1*n2
        print("Multipliction:",ans)
    case '/':
        ans=n1/n2
        print("Division:",ans)
    case '%':
        ans=n1%n2
        print("Modulo:",ans)
       
    

