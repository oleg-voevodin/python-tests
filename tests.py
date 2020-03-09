#! /usr/bin/env python
# -*- coding: utf-8 -*-

import os

if os.name == 'nt':
    os.system('cls')
else:
    os.system('clear')

file_with_test = open('test.txt', 'r', encoding='utf-8')

quantity_of_questions = 0
quantity_of_right_answers = 0

print('===== TEST =====')

while True:
    question = file_with_test.readline().strip()
    if (not question):
        break
    first_answer = file_with_test.readline().strip()
    second_answer = file_with_test.readline().strip()
    third_answer = file_with_test.readline().strip()
    fourth_answer = file_with_test.readline().strip()
    right_answer = file_with_test.readline().strip()
    print(f'\n{question}\n\n 1. {first_answer}\n 2. {second_answer}\n 3. {third_answer}\n 4. {fourth_answer}')
    answer = input('\nОтвет: ')
    quantity_of_questions += 1
    if answer == right_answer:
        quantity_of_right_answers += 1

print(f'\nТест завершен.\nВсего вопросов: {quantity_of_questions}\nВерных ответов: {quantity_of_right_answers}\nТест пройден на {int(quantity_of_right_answers / quantity_of_questions * 100)}%')