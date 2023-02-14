import random

capitals = {
    'Ukraine': 'Kyiv',
    'France': 'Paris',
    'Germany': 'Berlin',
    'Italy': 'Rome',
    'USA': 'Washington',
    'Canada': 'Ottawa',
    'Switzerland': 'Bern',
    'Austria': 'Vienna',
    'Belgium': 'Brussels',
    'Sweden': 'Stockholm',
    'Norway': 'Oslo',
    'Denmark': 'Copenhagen',
    'Finland': 'Helsinki',
    'Poland': 'Warsaw',
    'Romania': 'Bucharest',
    'Bulgaria': 'Sofia',
    'Greece': 'Athens',
}


def game_in_capitals(dict_: dict):
    score = 0
    lives = 3
    hint = ''
    new_one = True
    while True:

        if new_one:
            random_country = random.choice(list(dict_))
            question = input(
                f"Ok, what is the capital of {random_country}: ").title()

        if question == "exit":
            print(f"Your score: {score}, your HP: {lives}. See ya.")
            break

        elif question == dict_[random_country]:
            score += 1
            print(
                f"You are right! Your score: {score}, your HP: {lives}.\nLet's take one more)")
            hint = ''
            new_one = True

        else:
            letter_index = 0
            new_one = False

            while lives > 0 and question != dict_[random_country]:
                print('Oh no, here we go again...')
                lives -= 1
                hint += dict_[random_country][letter_index]
                question = input(
                    f"Here is your hint: {hint}. The answer is...: ").title()

                if question == "exit":
                    break

                letter_index += 1

            if lives == 0:
                ending = input(
                    f"Oh no... Your score is {score}, but your HP is 0( Game ower. Do you want to start new one?(Y/n): ")
                if ending == "Y":
                    score = 0
                    lives = 3
                    hint = ''
                    new_one = True

                elif ending == "exit" or ending == "n":
                    continue

                else:
                    print("I see you like this game >:) Alright, let's play one more)")
                    score = 0
                    lives = 3
                    hint = ''
                    new_one = True
