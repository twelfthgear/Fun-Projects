import random
print ("Hello there!")
print ("This program helps generate random potion decriptions!", '\n')

def randomPot ():
      title = (open('title.txt').readlines())
      effect = (open('effect.txt').readlines())
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
                  print ("This is a", random.choice(title),'of', random.choice(effect))
                  print ("Strength: ", random.choice(strength))
                  if strength == "Regular with no side effect.":
                        print ("Side Effects: No side effects.")
                  else:
                        print ("Side Effects: ", random.choice(sideEffect))
                  print ("Container: ", random.choice(container))
                  print ("Appearance: ", random.choice(appearance1),
                         'with', random.choice(appearance2), 'When sloshed, it feels,',
                         random.choice(texture))
                  print ("Label: ", random.choice(label))
                  print ("Taste: ", random.choice(tasteSmell))
                  print ("Smell: ", random.choice(tasteSmell))
                  print ('-----------------------------------------------------------------------------')
      if potNum == 1:
            print ( "Here is your random potion! Enjoy!")
      else:
            ("Here are your", potNum, "random potions! Enjoy!")
      print()
      input("- Hit ENTER to exit the program! -")
randomPot()















