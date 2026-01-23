import random


wins = 0
runs = 0
for i in range(0,100):
     runs = runs + 1
     print("Simulation #" + str(runs))
     winningDoor = random.randint(1, 3)
     contestChoice = random.randint(1, 3)
     revealDoor = random.randint(1,3)
     contestFinal = random.randint(1,3)
     while revealDoor == winningDoor or revealDoor == contestChoice:
        revealDoor = random.randint(1,3)
     while contestFinal == contestChoice or contestFinal == revealDoor:
              contestFinal = random.randint(1,3)
     if contestFinal == winningDoor:
          wins = wins + 1

print(wins)
print(runs)