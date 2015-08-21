import random
import string

SENTINEL = '*'

def get_random_letter():
    letters = string.ascii_lowercase + ' '
    random_int = random.randint(0, 26)
    random_letter = letters[random_int]
    return random_letter

def get_random_string(string_length, base_string=None):
    if base_string is None:
        random_string = ''.join([get_random_letter()
                                for _ in range(string_length)])
    else:
        base_string_length = len(base_string)
        if base_string_length != string_length:
            error_msg = 'Base string == {} but string lenght == {}'
            error_msg = error_msg.format(base_string_length, string_length)
            raise Exception(error_msg)

        random_string = ''.join([letter if letter != SENTINEL else
                                 get_random_letter()
                                 for letter in base_string])
    return random_string

def compare_strings(this_string, that_string):
    characters_that_match = [i if i == j else SENTINEL
                             for i, j in zip(this_string, that_string)]
    characters_that_match = ''.join(characters_that_match)
    number_of_characters_that_match = (len(characters_that_match) -
                                       characters_that_match.count(SENTINEL))
    return (number_of_characters_that_match, characters_that_match)

def run_monkey_test(this_string, hill_climb=True):
    number_of_runs = 0

    string_length = len(this_string)
    number_of_matches = 0
    best_random_string = ''
    characters_that_match = None

    while number_of_matches != string_length:
        random_string = get_random_string(string_length, characters_that_match)
        (this_number_of_matches,
         this_characters_that_match
        ) = compare_strings(this_string, random_string)

        if this_number_of_matches > number_of_matches:
            number_of_matches = this_number_of_matches 
            best_random_string = random_string
            if hill_climb:
                characters_that_match = this_characters_that_match
            print(best_random_string)

        number_of_runs += 1
        if number_of_runs % 1000 == 0:
            print_string = 'Best score so far: {} (number of runs: {})'
            print_string = print_string.format(number_of_matches,
                                               number_of_runs)
            print(print_string)
    print('Number of runs: {}'.format(number_of_runs))

if __name__ == '__main__':
    this_string = 'methinks it is like a weasel'
    run_monkey_test(this_string, False)
