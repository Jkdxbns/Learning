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

print("Welcome to Hangman !")

movies_list = ["Inception", "The Avengers", "The Dhoom"]
chosen_movie_name = list(str(random.choice(movies_list)).lower())
print("\n")

new_list =["_" for x in range(len(chosen_movie_name))]
end_of_game = False
lives = 0

while not end_of_game:
    user_guess = input("What letters do you think the movie name has ?\t").lower()
    for n in range(0, len(chosen_movie_name)):
        if chosen_movie_name[n] == " ":
            new_list[n] = " "
        elif user_guess == chosen_movie_name[n]:
            new_list[n] = user_guess

    if user_guess not in chosen_movie_name:
        print(stages[6 - lives])
        lives += 1

    print(f"movie name is : {(''.join(new_list)).capitalize()}")
    print("\n")
    if "_" in list(new_list):
        end_of_game = False
    elif "_" not in list(new_list):
        end_of_game = True

print("CONGRATULATIONS ,YOU HAVE WON !")
