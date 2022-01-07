import random


number_list = []
for i in range(0, 101):
    number_list.append(i)
number = random.choice(number_list)
print(number)

print(f'''Welcome to the Number Guessing Game!
I'm thinking of a number between {min(number_list)} and {max(number_list)}''')
level = input("\nChoose a difficulty level. Type 'easy' or 'hard'\n").lower()


def get_level():
    global attempts
    level_stop = True
    while level_stop:
        new_level = input("type 'easy' or 'hard'\n").lower()
        if new_level == "easy":
            print("You have 5 guesses")
            attempts += 5
            level_stop = False
        elif new_level == "hard":
            print("You hve 3 guesses")
            attempts += 3
            level_stop = False


def compare():
    global attempts
    attempts -= 1
    if int(user_guess) > max(number_list) or int(user_guess) < min(number_list):
        print(f"enter value between {min(number_list)} and {max(number_list)}")
        attempts += 1
    elif int(user_guess) < number:
        print("Your guess is too low")
    elif int(user_guess) > number:
        print("Your guess is too high")
    else:
        print('''You guessed the correct number
        YOU WIN !!!''')
        return True


def take_integer():
    ask_again = True
    while ask_again:
        new_user_guess = input("Enter only integer value:")
        for k in new_user_guess:
            if k.isdecimal():
                return new_user_guess


attempts = 0
if level == "easy":
    attempts += 5
    print(f"You have {attempts} guesses")
elif level == "hard":
    attempts += 3
    print(f"You hve {attempts} guesses")
else:
    get_level()


exit_game = False
while not exit_game:
    user_guess = input("Enter your guess: ")
    for i in user_guess:
        if i.isdecimal():
            continue
        else:
            user_guess = take_integer()
    exit_game = compare()
    if attempts == 0:
        print(f'''\nYour ran out of your attempts
        the correct number was {number}''')
        break
