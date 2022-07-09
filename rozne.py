import random

cyfry = ["2", "3", "4", "5", "6", "7", "8", "9", "10"]
figury = ["J", "Q", "K", "A"]
karty = [cyfry, figury]


def draw_card():
    random_card = random.choice(random.choice(karty))
    return random_card


def points(card):
    points = 0
    if card == "[J]" or card == "[Q]" or card == "[K]" or card == "[10]":
        points = 10
    elif card == "[A]":
        points = 11
    elif card == "[9]":
        points = 9
    elif card == "[8]":
        points = 8
    elif card == "[7]":
        points = 7
    elif card == "[6]":
        points = 6
    elif card == "[5]":
        points = 5
    elif card == "[4]":
        points = 4
    elif card == "[3]":
        points = 3
    elif card == "[2]":
        points = 2

    return points

def points_sum(**kwargs):
    summ = 0
    for key, value in kwargs.items():
        summ += int(value)
    return summ