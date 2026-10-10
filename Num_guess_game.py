import random

print("===================================")
print("       NUMBER GUESSING GAME")
print("===================================")

while True:
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)

    attempts = 0

    print("\nI have selected a number between 1 and 100.")
    print("Try to guess it!")

    while True:
        try:
            guess = int(input("Enter your guess: "))

            # Check if the guess is within the valid range
            if guess < 1 or guess > 100:
                print("Please enter a number between 1 and 100.")
                continue

            attempts += 1

            # Check the guess
            if guess == secret_number:
                print("\nCongratulations! You guessed the correct number!")
                print("The number was:", secret_number)
                print("Number of attempts:", attempts)
                break

            elif guess > secret_number + 10:
                print("Too high! Try again.")

            elif guess > secret_number:
                print("High! You are close.")

            elif guess < secret_number - 10:
                print("Too low! Try again.")

            elif guess < secret_number:
                print("Low! You are close.")

        except ValueError:
            print("Invalid input! Please enter a whole number.")

    # Ask if the user wants another round
    play_again = input("\nDo you want to play another round? (yes/no): ").lower()

    if play_again != "yes":
        print("\nThanks for playing!")
        print("Goodbye!")
        break