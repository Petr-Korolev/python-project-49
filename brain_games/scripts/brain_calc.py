#!/usr/bin/env python3
import random
import operator
import prompt

from random import randint, choice


def even_culc():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('What is the result of the expression?')
    correct = 0
    while correct >= 0:
        if correct == 3:
            print(f'Congratulation, {name}!')
            break
        number_1 = randint(10, 20)
        number_2 = randint(1, 20)
        operation = ['*', '+', '-']
        to_do = random.choice(operation)
        results = ''
        print('Question: ', number_1, to_do, number_2)
        answer_user = input('Your answer: ')
        if to_do == '*':
            results = operator.mul(number_1, number_2)
        elif to_do == '+':
            results = operator.add(number_1, number_2)
        elif to_do == '-':
            results = operator.sub(number_1, number_2)
        if int(results) == int(answer_user):
            print('Correct!')
            correct += 1
        else:
            print(f"'{answer_user}' is wrong answer ;( Correct answer was '{results}'"
                  f"\nLet's try again, {name}!")
            break


def main():
    even_culc()


if __name__ == '__main__':
    even_culc()
