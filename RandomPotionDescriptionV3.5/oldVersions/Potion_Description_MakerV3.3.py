
import random
import locale
print ("Hello there!")
print ("This program helps generate random potion decriptions!", '\n')

def randomPot ():
      potTitle = (open('potTitle.txt').readlines())
      potEffect = (open('potEffect.txt').readlines())
      container = (open('container.txt').readlines())
      appearance1 = (open('appearance1.txt').readlines())
      appearance2 = (open('appearance2.txt').readlines())
      texture = (open('texture.txt').readlines())
      label = (open('label.txt').readlines())
      strength = (open('strength.txt').readlines())
      sideEffect = (open('sideEffect.txt').readlines())
      tasteSmell = (open('tasteSmell.txt').readlines())
      
      potNum = eval(input("Please enter how many potions you wish to generate: "))
      print ()
      for x in range(potNum):
                  strength2 = random.choice(strength)
                  GP = 100
                  SP = GP * 10
                  CP = GP * 100
                  
                  print ("Type: \t\t",random.choice(potTitle))
                  print ("Effect: \t","of ",random.choice(potEffect))
                  print ("Strength: \t", strength2)
                  if "Regular with no side effect." in (strength2):
                        print ("Side Effects: \t No side effects.")
                        GP = GP + 400
                  elif "Seemingly permanent." in (strength2):
                        print ("Side Effects: \t No side effects.")
                  elif "Major with a strong side effect." in (strength2):
                        print ("Side Effects: \t", random.choice(sideEffect), '\t\t', random.choice(sideEffect))
                  elif "Minor with a strong side effect." in (strength2):
                        print ("Side Effects: \t", random.choice(sideEffect), '\t\t', random.choice(sideEffect))
                  elif "Regular with a strong side effect." in (strength2):
                        print ("Side Effects: \t", random.choice(sideEffect), '\t\t', random.choice(sideEffect)) 
                  elif "Regular with a slight side effect." in (strength2):
                        print ("Side Effect: \t", random.choice(sideEffect))
                  elif "Minor with a slight side effect." in (strength2):
                        print ("Side Effect: \t", random.choice(sideEffect))
                  elif "Major with a small side effect." in (strength2):
                        print ("Side Effect: \t", random.choice(sideEffect))  
                  elif "A poison. Almost no positive effect or side effect." in (strength2):
                        print ("Side Effect: \t", random.choice(sideEffect))
                  else:
                        print ("Side Effects: \t", random.choice(sideEffect),
                              '\t\t', random.choice(sideEffect), 
                              '\t\t', random.choice(sideEffect))
                  print ("Container: \t", random.choice(container))
                  print ("Appearance: \t", random.choice(appearance1),
                         '\t\t', "with", random.choice(appearance2),
                         '\t\t', "When sloshed, it feels", random.choice(texture))
                  print ("Label: \t\t", random.choice(label))
                  print ("Taste: \t\t", random.choice(tasteSmell))
                  print ("Smell: \t\t", random.choice(tasteSmell))
                  print ("Cost: ", '\t\t',"GP: ",GP, '\n',
                         '\t\t',"SP: ",SP, '\n',
                         '\t\t',"CP: ",CP, '\n')
                        
                  print ('---------------------------------------------------------------------------------------', '\n')
      if potNum == 1:
            print ( "Here is your random potion! Enjoy!")
      else:
            ("Here are your", potNum, "random potions! Enjoy!")
      print()
      input("- Hit ENTER to exit the program! -")
randomPot()















