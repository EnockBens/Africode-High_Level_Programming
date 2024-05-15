import random
random_number = random.randint(1, 5)
secret_number = random_number
guess_count = 0

while guess_count < 3:
    guess = int (input("guess a number (1-10): "))
    guess_count += 1

    if guess == secret_number:
        print("Congratulations , You guessed it!")
        break
    else:
        print ("Try Again!")

if guess_count == 3:
    print("sorry, you ran out of guesses . The number was ", secret_number)