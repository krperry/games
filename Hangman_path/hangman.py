"""Play a text-based game of Hangman in the terminal."""

import random

MAX_WRONG_GUESSES = 6


def load_words(file_name):
    """Read and return the words in the file at ``file_name``."""
    words = []
    word_file = open(file_name, "r")
    for word in word_file:
        words.append(word.strip())
    word_file.close()
    return words


def make_display_word(secret_word, guessed_letters):
    """Return the secret word with unguessed letters replaced by underscores.

    Separate the displayed characters with spaces so they can be read aloud
    one by one by a screen reader.
    """
    display = []
    for letter in secret_word:
        if letter.lower() in guessed_letters:
            display.append(letter)
        else:
            display.append("_")
    return " ".join(display)


def has_won(secret_word, guessed_letters):
    """Return whether every letter in ``secret_word`` has been guessed."""
    return count_blanks(secret_word, guessed_letters) == 0


def has_lost(wrong_guesses):
    """Return whether the number of wrong guesses has reached the limit."""
    return wrong_guesses >= MAX_WRONG_GUESSES


def spell_word(word):
    """Return ``word`` with spaces between its letters for spoken output."""
    return " ".join(word)


def show_score(wins, losses):
    """Print the totals for games won and lost."""
    print("Games won: " + str(wins) + ". Games lost: " + str(losses) + ".")


def count_blanks(secret_word, guessed_letters):
    """Return the number of letters in ``secret_word`` not yet guessed."""
    blanks = 0
    for letter in secret_word:
        if letter.lower() not in guessed_letters:
            blanks = blanks + 1
    return blanks


def get_guess(guessed_letters):
    """Prompt until the player enters a valid letter or a supported command.

    Return a new guessed letter, ``"quit"``, or ``"status"``. The ``help``
    command displays instructions and then prompts again.
    """
    while True:
        guess = input("Your guess: ")
        guess = guess.strip().lower()

        if guess == "help":
            show_help()
        elif guess in ["quit", "status"]:
            return guess
        elif len(guess) != 1:
            print("Please type just one letter.")
        elif not guess.isalpha():
            print("That is not a letter. Please type a letter from a to z.")
        elif guess in guessed_letters:
            print("You already guessed " + guess + ". Try a different letter.")
        else:
            return guess


def check_guess(secret_word, guess):
    """Print whether ``guess`` occurs in ``secret_word`` and return the result."""
    count = secret_word.lower().count(guess)
    if count == 0:
        print("Sorry, there is no", guess, "in the word.")
        return False
    if count == 1:
        print("Yes! There is one", guess, "in the word.")
        return True
    print("Yes! There are", count, "of the letter", guess, "in the word.")
    return True


def show_welcome():
    """Print the welcome message and basic game instructions."""
    print("Welcome to Hangman.")
    print("I am thinking of a word. Guess it one letter at a time.")
    print("Each unknown letter is shown as an underscore.")
    print("You can make", MAX_WRONG_GUESSES, "wrong guesses before you lose.")
    print("Type the word help at any time to hear the commands.")
    print()


def show_help():
    """Print the available commands and how to use them."""
    print("Commands:")
    print("Type one letter and press Enter to guess it.")
    print("Type status to hear the word and your guesses again.")
    print("Type help to hear these commands.")
    print("Type quit to stop playing.")
    print()


def show_status(secret_word, guessed_letters, wrong_guesses):
    """Print the current word display, guessed letters, and guesses remaining."""
    print("The word has", len(secret_word), "letters.")
    print("Word:", make_display_word(secret_word, guessed_letters))
    print(count_blanks(secret_word, guessed_letters), "letters are still unknown.")

    if len(guessed_letters) == 0:
        print("You have not guessed any letters yet.")
    else:
        sorted_letters = sorted(guessed_letters)
        print("Letters guessed so far:", ", ".join(sorted_letters))

    guesses_left = MAX_WRONG_GUESSES - wrong_guesses
    print("Wrong guesses left:", guesses_left)
    print()


def play_one_game(words):
    """Play one game using ``words`` and return ``"won"``, ``"lost"``, or ``"quit"``."""
    secret_word = random.choice(words)
    guessed_letters = []
    wrong_guesses = 0

    show_status(secret_word, guessed_letters, wrong_guesses)

    while True:
        guess = get_guess(guessed_letters)

        if guess == "quit":
            print(
                "The word was "
                + secret_word
                + ". It is spelled "
                + spell_word(secret_word)
                + "."
            )
            return "quit"

        if guess == "status":
            show_status(secret_word, guessed_letters, wrong_guesses)
            continue

        guessed_letters.append(guess)
        correct = check_guess(secret_word, guess)
        if not correct:
            wrong_guesses = wrong_guesses + 1

        if has_won(secret_word, guessed_letters):
            print("You win! The word was " + secret_word + ".")
            print("You had", MAX_WRONG_GUESSES - wrong_guesses, "wrong guesses left.")
            return "won"

        if has_lost(wrong_guesses):
            print("Out of guesses. You lose.")
            print(
                "The word was "
                + secret_word
                + ". It is spelled "
                + spell_word(secret_word)
                + "."
            )
            return "lost"

        show_status(secret_word, guessed_letters, wrong_guesses)


def ask_play_again():
    """Prompt until the player answers yes or no, then return their choice."""
    while True:
        answer = input("Do you want to play again? Type yes or no: ")
        answer = answer.strip().lower()
        if "yes".startswith(answer.lower()):
            return True
        if "no".startswith(answer.lower()):
            return False
        print("Please type yes or no.")


def main():
    """Load the word list and run games until the player chooses to stop."""
    words = load_words("new_words.txt")
    show_welcome()

    wins = 0
    losses = 0

    while True:
        print("Starting a new game.")
        result = play_one_game(words)

        if result == "won":
            wins = wins + 1
        elif result == "lost":
            losses = losses + 1

        show_score(wins, losses)

        if result == "quit":
            break
        if not ask_play_again():
            break
        print()

    print("Thanks for playing Hangman. Goodbye.")


main()
