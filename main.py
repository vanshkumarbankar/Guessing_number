import random as r
import num2words as num
import roman as rm

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False            
    return True


computer=r.randint(0,101)
trials=0

hints=[(f"This length of word of that number is :{len(num.num2words(computer).replace("-",''))}"),
       ("This number is written in roman is".upper(),rm.toRoman(computer)),
       ("if the half of the number is substracted from cube of that no is: ",computer**3-computer/2), 
       ("yeh number prime hai: ",is_prime(computer)),
       
      ]

print()
print("The Game is Started".title())
print("the computer selected a number u guess it".title())
while True:
  trials+=1
  if trials in [x*5 for x in range(1,100) ]:
    user_input=input("You want Hint??(y/n): ")
    if user_input =="y":
      print("The Hints for the number: ",r.choice(hints))
  
  try:
    user=int(input("Guess The Number Between 1 to 100: "))
  except:
    print("Invalid syntax")
  if user < 0 and user>100:
    print("enter number in between 0 and 100 only!".upper())
    continue

  if user==computer:
    print("good You win the game".upper())
    print(f"in trials {trials}".upper())
    break
  
  elif (computer-user)<=5 and (computer-user)>=0:
    print("good,you come near the number")
  
  elif (user - computer) <=5 and (user-computer)>=0:
    print("good,you come near the number")
  
  else:
    print("try again!".upper())
    continue
