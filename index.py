"""Index module"""

from typing import TextIO
from random import randint

WORDS_FILE_PATH = "./words.txt"

def get_replacement_word(word: str, words_file: TextIO) -> str:
    """Retrieves replacement word"""
    words_file.seek(0)

    word_length = len(word)

    potential_words = [
        potential_word.strip() for potential_word in words_file
        if (word[0].lower == potential_word[0].lower and word_length == len(potential_word.strip()))
    ]

    replacement_word_index = randint(0, word_length - 1)

    replacement_word = potential_words[replacement_word_index] if len(potential_words) > 0 else word

    return replacement_word

def replace_words(words: list[str]) -> str:
    """Replaces words with new words"""
    with open(WORDS_FILE_PATH, "r") as words_file:
        new_words = [get_replacement_word(word, words_file) for word in words]
        new_sentence = " ".join(new_words)

        return new_sentence


def main():
    """Main function"""
    sentence = input("Please input a sentence:\n")
    words = sentence.split()
    new_sentence = replace_words(words)
    
    print(new_sentence)

if __name__ == "__main__":
    main()
