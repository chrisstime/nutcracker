# Password generator

from random import sample, choices
from string import ascii_letters, punctuation, digits

options_dict = {
    'symbols': punctuation,
    'letters': ascii_letters,
    'numbers': digits
}


def shuffle_characters(symbols: bool, letters: bool, numbers: bool):
    included_characters = list()
    characters_dict = {'symbols': symbols, 'letters': letters, 'numbers': numbers}
    for character_type, include_character in characters_dict.items():
        if include_character:
            included_characters.extend(options_dict[character_type])

    return sample(included_characters, len(included_characters))


def format_password(generated_password_array):
    return "".join(generated_password_array)


def generate_password(symbols: bool, letters: bool, numbers: bool, password_length):
    shuffled_characters = shuffle_characters(symbols=symbols, letters=letters, numbers=numbers)

    return format_password(choices(shuffled_characters, k=password_length))
