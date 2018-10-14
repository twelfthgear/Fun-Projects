
import random
import math
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
      
      print ("twelfthGear's Potion Description Generator V 3.4.1 GOLDFIX", '\n')
      potNum = eval(input("Please enter how many potions you wish to generate: "))
      print()

      for x in range(potNum):
                  strength2 = random.choice(strength)
                  title = random.choice(potTitle)
                  effect = random.choice(potEffect)
                  # Potions cost 125 GP as a base cost.
                  GP = 125
                  
                  # This is a small random modifier just for fun.
                  GP2 = random.randint(25, 50)

                  print ("Type: \t\t", title)
                  
                  if "of  Fairy Godmother’s Lament. You get a single wish spell. It lasts until a wish is spoken." in effect:
                       print("Effect: \t","of ",effect, '\n')
                       GP = GP + 375 * 5
                  else:
                       print ("Effect: \t","of ",effect, '\n')

                  print ("Strength: \t", strength2)
                  # ----------------------------------------------------------
                  # Strength of Potion and Side Effects with a gold modifier for each.
                  # ----------------------------------------------------------
                  # Side Effect 
                  # ---------------------
                  # Slight = 1 side effect (GP - 25)
                  # Strong = 2 side effects (GP - 50)
                  # A poison = 3 side effects (GP - 75)
                  # No side effects = no side effects (GP * 2)
                  # ----------------
                  # Effect 
                  # ----------------
                  # Temporary (GP * 1)
                  # Minor = (GP * 1.25)
                  # Regular = (GP * 1.5)
                  # Major = (GP * 1.75)
                  # Seemingly Permanant = (GP * 4)
                  # Poison = (GP - 75)
                  # ---------------------------------------------------------
                  print ()
                  
                  if "Seemingly permanent." in (strength2):
                        print ("Side Effects: \t No side effects.")
                        GP = GP * 4
                        GP = int(GP + GP2 * 2)
                  elif "Temporary but strong and wears off quickly." in (strength2):
                        print ("Side Effects: \t The side effects begin after the potion wears off. \t\n", '\t\t',random.choice(sideEffect),
                               '\t\t', random.choice(sideEffect))
                        GP = GP - 50
                        GP = int(GP + GP2 * 1)
                  elif "Minor with no side effect." in (strength2):
                        print ("Side Effect: \t No side effect.")
                        GP = GP * 2
                        GP = int(GP + GP2 * 1.25)
                  elif "Minor with a slight side effect." in (strength2):
                        print ("Side Effect: \t", random.choice(sideEffect))
                        GP = GP - 25
                        GP = int(GP + GP2 * 1.25)
                  elif "Minor with a strong side effect." in (strength2):
                        print ("Side Effects: \t", random.choice(sideEffect), '\t\t', random.choice(sideEffect))
                        GP = GP - 50
                        GP = int(GP + GP2 * 1.25)
                  elif "Regular with no side effect." in (strength2):
                        print ("Side Effects: \t No side effects.")
                        GP = int(GP + GP2 * 1.5)
                        GP = GP * 2
                  elif "Regular with a slight side effect." in (strength2): 
                        print ("Side Effect: \t", random.choice(sideEffect))
                        GP = GP - 25
                        GP = int(GP + GP2 * 1.5)
                  elif "Regular with a strong side effect." in (strength2):
                        print ("Side Effects: \t", random.choice(sideEffect), '\t\t', random.choice(sideEffect))
                        GP = GP - 50
                        GP = int(GP + GP2 * 1.5)
                  elif "Major with a strong side effect." in (strength2):
                        print ("Side Effects: \t", random.choice(sideEffect), '\t\t', random.choice(sideEffect))
                        GP = int(GP + GP2 * 1.75)
                        GP = GP - 50
                  elif "Major with a slight side effect." in (strength2):
                        print ("Side Effect: \t", random.choice(sideEffect))
                        GP = GP - 50
                        GP = int(GP + GP2 * 1.75)
                  elif "Major with no side effect." in (strength2):
                        print ("Side Effect: \t No side effect.")
                        GP = GP - 50
                        GP = int(GP + GP2 * 1.75)
                  elif "A poison. Almost no positive effect." in (strength2):
                        print ("Side Effect: \t", random.choice(sideEffect))  
                        GP = GP - 75
                        GP = int(GP + GP2)
                  else:
                        print ("Side Effects: \t", "Something's wrong! Check [strength.txt!]")
                        GP = 'broken .txt'
                  print()
                  print ("Container: \t", random.choice(container), '\n')
                  print ("Appearance: \t", random.choice(appearance1),
                         '\t\t', "with", random.choice(appearance2),
                         '\t\t', "When sloshed, it feels", random.choice(texture), '\n')
                  print ("Label: \t\t", random.choice(label), '\n')
                  print ("Taste: \t\t", random.choice(tasteSmell), '\n')
                  print ("Smell: \t\t", random.choice(tasteSmell), '\n')
                  SP = GP * 10
                  CP = GP * 100
                  print ("Cost: ", '\t\t',"GP: ",GP, '\n',
                         '\t\t',"SP: ",(SP), '\n',
                         '\t\t',"CP: ",(CP), '\n')
                        
                  print ('---------------------------------------------------------------------------------------', '\n')
      if potNum == (1):
            print ( "Here is your random potion! Enjoy!")
      else:
            print ("Here are your", potNum, "random potions! Enjoy!")
      print()
      input("- Hit ENTER to exit the program! -")
randomPot()















