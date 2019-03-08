#!/usr/bin/env python3

"""Password generator module"""

from random import sample, choices
from string import ascii_letters, punctuation, digits

options_dict = {
    'symbols': punctuation,
    'letters': ascii_letters,
    'numbers': digits
}


def _shuffle_characters(symbols: bool, letters: bool, numbers: bool):
    included_characters = list()
    characters_dict = {'symbols': symbols, 'letters': letters, 'numbers': numbers}
    for character_type, include_option in characters_dict.items():
        if include_option:
            included_characters.extend(options_dict[character_type])

    if included_characters:
        return sample(included_characters, len(included_characters))


def _format_password(generated_password_array):
    return "".join(generated_password_array)


def generate_password(symbols: bool, letters: bool, numbers: bool, password_length):
    shuffled_characters = _shuffle_characters(symbols=symbols, letters=letters, numbers=numbers)

    if shuffled_characters:
        return _format_password(choices(shuffled_characters, k=password_length))
