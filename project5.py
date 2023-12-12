def get_user_input():
    # Function to get user input for their full name
    user_name = input("Enter your full name: ")
    return user_name

def display_character_count(user_name):
    # Display the number of characters in the string
    count = len(user_name)
    print(f"1. Number of characters in the string: {count}")

def display_last_character(user_name):
    # Display the last character in the string
    last_char = user_name[-1]
    print(f"2. Last character in the string: {last_char}")

def display_first_occurrence_of_e(user_name):
    # Display the location of the first occurrence of the letter 'e'
    e_index = user_name.find('e')
    print(f"3. Location of the first occurrence of 'e': {e_index if e_index != -1 else 0}")

def display_word_count(user_name):
    # Display the number of words in the string
    word_count = len(user_name.split())
    print(f"4. Number of words in the string: {word_count}")

def display_first_word(user_name):
    # Display the first word of the string
    first_word = user_name.split()[0]
    print(f"5. First word of the string: {first_word}")

def display_vowel_count(user_name):
    # Display the number of vowels in the string
    vowels = "aeiouAEIOU"
    vowel_count = sum(1 for char in user_name if char in vowels)
    print(f"6. Number of vowels in the string: {vowel_count}")

def capitalize_vowels(user_name):
    # Display the string after capitalizing all vowels and lowercasing consonants
    vowels = "aeiouAEIOU"
    modified_string = ''.join(char.upper() if char in vowels else char.lower() for char in user_name)
    print(f"7. String after capitalizing vowels: {modified_string}")

def display_centered_string(user_name):
    # Display the string centered between 50 '~'s and 70 '+'s
    centered_string = user_name.center(50, '~').center(70, '+')
    print(f"8. Centered string between 50 '~'s and 70 '+'s:\n{centered_string}")

def display_split_string(user_name):
    # Display the string split in half on either end of 70 '*'s
    split_string = user_name.split()
    half_length = len(split_string) // 2
    first_half = ' '.join(split_string[:half_length])
    second_half = ' '.join(split_string[half_length:])
    split_result = f"{first_half} {'*' * 70} {second_half}"
    print(f"9. String split in half on either end of 70 '*'s:\n{split_result}")

# Main program
user_name = get_user_input()
display_character_count(user_name)
display_last_character(user_name)
display_first_occurrence_of_e(user_name)
display_word_count(user_name)
display_first_word(user_name)
display_vowel_count(user_name)
capitalize_vowels(user_name)
display_centered_string(user_name)
display_split_string(user_name)
