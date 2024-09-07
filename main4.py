try:
    num1,num2=eval(input("enter 2 numbers seperated by a comma"))
    result=num1/num2
    print(result)
except ZeroDivisionError:
    print("number can not be divided by 0")
 
except SyntaxError:  
     print("ADD A COMMA OR ELSE0")
     
except:
    print("wrong input") 
    
else:
    print("there is no execption")
    
    
finally:
    print("i will be executed besuse of you")