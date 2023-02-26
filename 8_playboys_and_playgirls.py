import csv
import random


players = ['Josh', 'Luke', 'Kate', 'Mark', 'Mary']


def playscore(list_: list):
    with open("score.csv", mode="w+") as score_file:
        fieldnames = ["Player name", "Score"]
        writer = csv.DictWriter(score_file, fieldnames=fieldnames)
        writer.writeheader()

        for _ in range(10):
            for player in list_:
                writer.writerow({
                    'Player name': f'{player}',
                    'Score': f'{random.randint(0, 100)}'
                })
        score_file.close()


def highest_score(list_: list):
    score_dict = dict()

    for player in list_:
        with open("score.csv", mode="r") as score_file:
            reader = csv.DictReader(score_file)
            score = 0

            for row in reader:
                if (int(row['Score']) > score) and (player == row['Player name']):
                    score_dict[player] = int(row['Score'])
                    score = int(row['Score'])

        score_file.close()

    score_file.close()

    score_dict = sorted(score_dict.items(), key=lambda x: x[1], reverse=True)

    with open("high_scores.csv", mode="w+") as high_scores:
        fieldnames = ["Player name", "Score"]
        writer = csv.DictWriter(high_scores, fieldnames=fieldnames)
        writer.writeheader()

        for player in score_dict:
            writer.writerow({
                'Player name': f'{player[0]}',
                'Score': f'{player[1]}'
            })

    high_scores.close()


playscore(players)
highest_score(players)
