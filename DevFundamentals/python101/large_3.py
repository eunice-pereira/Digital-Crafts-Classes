import random 

guess, guess_count, s_num = None, 0, random.randint(1,10)

while guess != s_num and guess_count < 5: 

    while True:
        guess_count += 1
        try: 
            guess = int(input("Please guess a number: \n"))
            break
        except ValueError:
            print("You did not enter a number. Try again!")

    if guess == s_num: 
        print("You win!")
    elif guess < s_num: 
        print("Your number is too low, try again.")
    else: 
        print("Your number is too high, try again.")

if guess_count >= 5: 
    print("You guessed too many times. Goodbye!")

play_again = input("Do you want to play again?")