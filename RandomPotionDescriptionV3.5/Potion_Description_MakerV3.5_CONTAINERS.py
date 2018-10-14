
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
      
      print ("twelfthGear's Potion Description Generator V 3.5 CONTAINERS", '\n')
      potNum = eval(input("Please enter how many potions you wish to generate: "))
      print()

      for x in range(potNum):
                  strength2 = random.choice(strength)
                  title = random.choice(potTitle)
                  effect = random.choice(potEffect)
                  container2 = random.choice(container)
                  uses = 0
                  
                  # Potions cost 100 - 125 GP just as a base cost before begative effect and stuff.
                  GP = random.randint(100, 125)
                  
                  # This is a small random GP modifier just for fun.
                  GP2 = random.randint(25, 75)

                  # The title determines how the potion was crafted. This can affect the gold.
                  print ("Type: \t\t", title)

                  # This is just a precaution in case the true wish potion is created. 
                  if "of  Fairy Godmother’s Lament. You get a single wish spell. It lasts until a wish is spoken." in effect:
                       print("Effect: \t","of ",effect, '\n')
                       container2 = "A small corked bottle no bigger than your thumb."
                       strength2 = "Seemingly permanent."
                       GP = GP + 375
                       GP = GP * 25
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
                        GP = GP + GP2 * 2
                        GP = GP * 4
                  elif "Temporary but strong and wears off quickly. The side effects begin after the potion wears off." in (strength2):
                        print ("Side Effects: \t\n", '\t\t',random.choice(sideEffect),
                               '\t\t', random.choice(sideEffect))
                        GP = GP - 50
                        GP = GP + GP2 * 1
                  elif "Minor with no side effect." in (strength2):
                        print ("Side Effect: \t No side effect.")
                        GP = GP + GP2 * 1.25
                        GP = GP * 2
                  elif "Minor with a slight side effect." in (strength2):
                        print ("Side Effect: \t", random.choice(sideEffect))
                        GP = GP + GP2 * 1.25
                        GP = GP - 25
                  elif "Minor with a strong side effect." in (strength2):
                        print ("Side Effects: \t", random.choice(sideEffect), '\t\t', random.choice(sideEffect))
                        GP = GP + GP2 * 1.25
                        GP = GP - 50
                  elif "Regular with no side effect." in (strength2):
                        print ("Side Effects: \t No side effects.")
                        GP = GP + GP2 * 1.5
                        GP = GP * 2
                  elif "Regular with a slight side effect." in (strength2): 
                        print ("Side Effect: \t", random.choice(sideEffect))
                        GP = GP + GP2 * 1.5
                        GP = GP - 25
                  elif "Regular with a strong side effect." in (strength2):
                        print ("Side Effects: \t", random.choice(sideEffect), '\t\t', random.choice(sideEffect))
                        GP = GP + GP2 * 1.5
                        GP = GP - 50
                  elif "Major with a strong side effect." in (strength2):
                        print ("Side Effects: \t", random.choice(sideEffect), '\t\t', random.choice(sideEffect))
                        GP = GP + GP2 * 1.75
                        GP = GP - 50
                  elif "Major with a slight side effect." in (strength2):
                        print ("Side Effect: \t", random.choice(sideEffect))                        
                        GP = GP + GP2 * 1.75
                        GP = GP - 50
                  elif "Major with no side effect." in (strength2):
                        print ("Side Effect: \t No side effect.")                        
                        GP = GP + GP2 * 1.75
                        GP = GP - 50
                  elif "A poison. Almost no positive effect." in (strength2):
                        print ("Side Effect: \t", random.choice(sideEffect))                        
                        GP = GP + GP2
                        GP = GP - 75
                  else:
                        print ("Side Effects: \t", "Something's wrong! Check [strength.txt!]")
                        GP = 'broken .txt'
                  print()

                  # If else statement that determines how many uses a "potion" can have.
                  if "A bone flask." in (container2):
                        print ("Container: \t",container2, '\n')
                        uses = 2
                  elif "A capped bull's horn." in (container2):
                        print ("Container: \t",container2, '\n')
                        uses = 2
                  elif "A clean syringe." in (container2):
                        print ("Container: \t",container2, '\n')
                        uses = 1
                        GP = GP - 25
                  elif "A clear pill capsule the size of the tip of your pinkie." in (container2):
                        print ("Container: \t",container2, '\n')
                        uses = 1
                        GP = GP + 25
                  elif "A coloured bottle." in (container2):
                        print ("Container: \t",container2, '\n')
                        uses = 2
                  elif "A thin, conical and smooth glass bottle." in (container2):
                        print ("Container: \t",container2, '\n')
                        uses = 1
                  elif "A geometric diamond shaped bottle." in (container2):
                        print ("Container: \t",container2, '\n')
                        uses = 1
                  elif "A small glass syringe." in (container2):
                        print ("Container: \t",container2, '\n')
                        uses = 1
                        GP = GP - 25
                  elif "A large bottle." in (container2):
                        print ("Container: \t",container2, '\n')
                        uses = 4
                        GP = GP * 1.25
                  elif "A large metal bottle." in (container2):
                        print ("Container: \t",container2, '\n')
                        uses = 6
                        GP = GP * 1.75
                  elif "A metal flask." in (container2):
                        print ("Container: \t",container2, '\n')
                        uses = 4
                        GP = GP * 1.25
                  elif "A metal thermos." in (container2):
                        print ("Container: \t",container2, '\n')
                        uses = 6
                        GP = GP * 1.5
                  elif "A small corked bottle no bigger than your thumb." in (container2):
                        print ("Container: \t",container2, '\n')
                        uses = 1
                  elif "A musky watertight leather pouch." in (container2):
                        print ("Container: \t",container2, '\n')
                        uses = 2
                        GP = GP - 25
                  elif "A very decorated ornate glass bottle." in (container2):
                        print ("Container: \t",container2, '\n')
                        uses = 1
                  elif "A small medical vial." in (container2):
                        print ("Container: \t",container2, '\n')
                        uses = 1
                  elif "A large medical vial." in (container2):
                        print ("Container: \t",container2, '\n')
                        uses = 3
                  elif "A small metal vial." in (container2):
                        print ("Container: \t",container2, '\n')
                        uses = 2
                  elif "A large metal vial." in (container2):
                        print ("Container: \t",container2, '\n')
                        uses = 4
                        GP = GP * 1.25
                  elif "A small shot sized bottle." in (container2):
                        print ("Container: \t",container2, '\n')
                        uses = 1
                  elif "A tall square glass bottle." in (container2):
                        print ("Container: \t",container2, '\n')
                        uses = 2
                  elif "A stone flask." in (container2):
                        print ("Container: \t",container2, '\n')
                        uses = 3
                        GP = GP * 1.25
                  elif "A translucent beer bottle." in (container2):
                        print ("Container: \t",container2, '\n')
                        uses = 3
                        GP = GP * 1.25
                  elif "A translucent long wine bottle." in (container2):
                        print ("Container: \t",container2, '\n')
                        uses = 6
                        GP = GP * 1.5
                  elif "A watertight leather waterskin." in (container2):
                        print ("Container: \t",container2, '\n')
                        uses = 12
                        GP = GP * 1.75
                  elif "An erlenmeyer flask with drink measurements." in (container2):
                        print ("Container: \t",container2, '\n')
                        uses = 6
                        GP = GP * 1.5
                  elif "A small  perfume like spray bottle." in (container2):
                        print ("Container: \t",container2, '\n')
                        uses = 50
                        GP = GP * 2
                  elif "A large  perfume like spray bottle." in (container2):
                        print ("Container: \t",container2, '\n')
                        uses = 100
                        GP = GP * 2.5
                  else:
                        print ("Container: \t Container.txt Machine Broke. Fix plox.")
                        uses = 1

                  print ("Uses: \t\t", random.randint(1, uses), "/", uses,'\n') 
                  print ("Appearance: \t", random.choice(appearance1),
                         '\t\t', "with", random.choice(appearance2),
                         '\t\t', "When sloshed, it feels", random.choice(texture), '\n')
                  print ("Label: \t\t", random.choice(label), '\n')
                  print ("Taste: \t\t", random.choice(tasteSmell), '\n')
                  print ("Smell: \t\t", random.choice(tasteSmell), '\n')
                  
                  GP = int(GP)
                  SP = GP * 10
                  CP = GP * 100
                  
                  print ("Cost: ", '\t\t',"GP: ",int(GP), '\n',
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















