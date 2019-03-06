# Password generator

from random import sample, choices
from string import ascii_letters, printable, digits

all_characters = printable
letters_only = ascii_letters
letters_and_numbers_only = letters_only + digits


def split_characters(characters):
    return [characters[i:i+1] for i in range(0, len(characters), 1)]


def shuffle_characters(character_range):
    if character_range == 'all_characters':
        return sample(all_characters, len(all_characters))
    elif character_range == 'letters_and_numbers_only':
        return sample(letters_and_numbers_only, len(letters_and_numbers_only))
    elif character_range == 'letters_only':
        return sample(letters_only, len(letters_only))


def format_password(generated_password_array):
    return "".join(generated_password_array)


def generate_password(character_range, password_length):
    shuffled_characters = shuffle_characters(character_range)

    return format_password(choices(shuffled_characters, k=password_length))
