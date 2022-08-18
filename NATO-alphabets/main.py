import pandas as pd

alphabet_file = pd.read_csv("nato_phonetic_alphabet.csv")
dictionary_of_nato = {row.letter: row.code for (index, row) in alphabet_file.iterrows()}


def generate_phonetics():
    word = input("Enter a word: ").upper()
    try:
        word_nato_in_list = [dictionary_of_nato[letter] for letter in list(word)]
    except KeyError:
        print("Input only letters please")
        generate_phonetics()
    else:
        print(word_nato_in_list)


generate_phonetics()
