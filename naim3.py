try:
  B=int(input("PLease enteR A NUMBER   "))
  print("the number you entered is,",B)
except ValueError as v:
  print("ERROR ERROR, BOMB BLOWING UP ")
finally:
    print("i will be executed for ever")