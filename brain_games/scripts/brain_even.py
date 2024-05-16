#!/usr/bin/env python3
import prompt
from random import randint


def even_number():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    correct = 0
    while correct >= 0:
        if correct == 3:
            print(f'Congratulation, {name}!')
            break
        number = randint(1, 100)
        print('Question: ', number)
        answer = input()
        if number % 2 == 0 and answer == 'yes':
            print('Correct!')
            correct += 1
        elif number % 2 != 0 and answer == 'no':
            print('Correct!')
            correct += 1
        else:
            print(f"Let's try again, {name}!")
            break


def main():
    even_number()


if __name__ == '__main__':
    even_number()

