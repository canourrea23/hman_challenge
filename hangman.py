import random
from word import words


def get_word():
    word = random.choice(words)
    return word.upper()


def play(world):
    word_completion = "_" * len(words)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 7
    print("Let's play Hangman!")
    print(display_hangman(tries))
    print(word_completion)
    print("\n")
    while not guessed and tries > 0:
        guess = input('Please guess a letter or word: ').upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print('You already guessed the letter', guess)
            elif guess not in words:
                print(guess, "is not in the word.")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print("Good Job,", guess, "is in the word.")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(
                    words) if letter == guess]
            for index in indices:
                word_as_list[index] = guess
            word_completion = ''.join(word_as_list)
            if '_' not in word_completion:
                guessed = True
        elif len(guess) == len(words) and guess.isalpha():
            if guess in guessed_words:
                print("You already guessed the word", guess)
            elif guess != words:
                print(guess, "is not the word.")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = words
        else:
            print("Not a valid guess.")
        print(display_hangman(tries))
        print(word_completion)
        print("\n")
    if guessed:
        print("Congrats, you guessed the word! You win!")
    else:
        print("Sorry, you ran out of tries. The word was " +
              words + ". Maybe next time!")


def display_hangman(tries):
    hangman = [
        """
    ____
    |     |
    |     O
    |   - | -
    |    /\
    |
    -
    """,

        """
    ____
    |     |
    |     O
    |   - | -
    |    /
    |
    -
    """,
        """
    ____
    |     |
    |     O
    |   - | -
    |    
    |
    -
    """,
        """
    ____
    |     |
    |     O
    |   - | 
    |    
    |
    -
    """,
        """
    ____
    |     |
    |     O
    |   - 
    |    
    |
    -
    """,
        """
    ____
    |     |
    |     O
    |   
    |    
    |
    -
    """,
        """
    ____
    |     |
    |    
    |   
    |    
    |
    -
    """
    ]
    print(len(hangman))
    print('hello', tries)
    return hangman[tries - 1]


def main():
    word = get_word()
    play(word)
    while input('Play Again? (Y/N) ').upper() == 'Y':
        words = get_word()
        play(words)


if __name__ == '__main__':
    main()
