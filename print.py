import random
print("welcome to guess game")
name =input("what is your name ")
print("well "+ name +" guess number between 1 to 20")
number = random.randint(1, 20)
for guess_num in range(5):
guess = int(input("\ntake a guess "))
if guess < number:
print("your guess is too low")
elif guess > number:
print("your guess is too high")
else:
break

if guess == number:
print("\ngood job "+ name +" your guess my number in "+ str(guess_num + 1) +" guesses")
else:
print("\nGame over, the number was "+ str(number) + ".")
