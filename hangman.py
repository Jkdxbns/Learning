import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
logo = ''' 
 _                                             
| |                                            
| |__   ___ _ __    __ _ _ __ ___   __ _ _ __  
|  _ \ / _  |  _ \ / _  |  _   _ \ / _  |  _ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''
print(logo)

movies_list = ["Inception", "The Avengers", "The Doom"]
chosen_movie_name = list(random.choice(movies_list).lower())
print(f"Oops! Here is the movie name: {''.join(chosen_movie_name)}\n")

new_list = ["_" for x in range(len(chosen_movie_name))]
end_of_game = False
lives = 0
user_guess_list = []

while not end_of_game:
    user_guess = input("What letters do you think the movie name has ?\t").lower()

    if user_guess in user_guess_list:
        print("You've already entered this letter, don't worry you have all of your lives ")
        lives -= 1
    else:
        user_guess_list.append(user_guess)

    for n in range(0, len(chosen_movie_name)):
        if chosen_movie_name[n] == " ":
            new_list[n] = " "
        elif user_guess == chosen_movie_name[n]:
            new_list[n] = user_guess

    if user_guess not in chosen_movie_name :
        print("You've chosen a letter which is not there in the movie name ;(")
        print(f"{stages[6 - lives]}\t\tYour remaining life count : {6 - lives}\n")
        lives += 1

    if lives == 7:
        print("You ran out of your lives , better luck next time...")
        break
    print(f"movie name is : {(''.join(new_list)).capitalize()}")
    print("\n")
    if "_" in list(new_list):
        end_of_game = False
    elif "_" not in list(new_list):
        end_of_game = True

if end_of_game == True:
    print("CONGRATULATIONS ,YOU HAVE GUESSED THE MOVIE NAME \n\t\t\t\tYOU WIN !")
