import random

# A list of words to choose from
words = ["dog", "cat", "bird", "fish", "mouse", "xbox", "roblox"]

# Choose a random word from the list
answer = random.choice(words)

# Convert the word to a list of underscores the same length as the word
display = ["_"] * len(answer)

# Keep track of the letters that have been guessed
guesses = []

# Loop until the word is guessed
while "_" in display:
    print(" ".join(display))
    print("Guesses: ", " ".join(guesses))
    guess = input("Guess a letter: ")
    if guess in guesses:
        print("You already guessed that letter.")
    elif guess in answer:
        for i in range(len(answer)):
            if answer[i] == guess:
                display[i] = guess
        print("Correct!")
    else:
        print("Incorrect.")
    guesses.append(guess)

# Print a message when the word is guessed
print(" ".join(display))
print("Congratulations! You guessed the word", answer, "!")
