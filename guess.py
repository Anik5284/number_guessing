import random

def guess_game(low=1, high=100, max_tries=7):
    secret = random.randint(low, high)
    print(f"🎯 I'm thinking of a number between {low} and {high}. You have {max_tries} tries!")

    for attempt in range(1, max_tries + 1):
        while True:
            try:
                guess = int(input(f"Try {attempt}/{max_tries} — your guess: "))
                break
            except ValueError:
                print("Please enter a whole number.")

        if guess == secret:
            print(f"✅ Correct! The number was {secret}. You got it in {attempt} tries.")
            return
        hint = "too low" if guess < secret else "too high"
        print(f"❌ {hint}.")
    print(f"😅 Out of tries! The number was {secret}.")


