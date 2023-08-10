import os
import random
import platform

ACTUAL_SYSTEM = platform.system()


def clear():
    if ACTUAL_SYSTEM == 'Windows':
        os.system('cls')
    else:
        os.system('clear')


def load_data() -> dict:
    archive = open('preguntas_respuestas.txt', mode='r', encoding='UTF8')

    questions_answers_list: list = archive.read().split('\n\n')
    questions_answers_list: list = [
        x.replace('\n', ' ') for x in questions_answers_list]
    questions: list = []
    answers: list = []

    for index, sentence in enumerate(questions_answers_list):
        if not (index % 2):
            questions.append(sentence)
        else:
            answers.append(sentence)
    
    archive.close()

    return dict(zip(questions, answers))


def view_question(metrics, question):
    clear()
    print(
        f'''Puntuacion: {metrics["success"]} de {metrics["total"]}

Pregunta:
{question}

''')


def view_question_answer(metrics, question, data):
    clear()
    print(
        f'''Puntuacion: {metrics["success"]} de {metrics["total"]}

Pregunta:
{question}

Respuesta:
{data[question]}

Seleccione una de las siguientes opciones en base a su respuesta...
''')


def show_question(data: dict, questions: list, metrics: dict) -> bool:
    question = random.choice(questions)
    view_question(metrics, question)
    res = input('Presione la tecla Enter para mostrar la respuesta...')
    view_question_answer(metrics, question, data)
    option = input('1. Correcta   2. Incorrecta  3. Salir\n')
    while (option != '1' and option != '2' and option != '3'):
        print('Seleccione una de las siguientes opciones en base a su respuesta...')
        option = input('1. Correcta   2. Incorrecta  3. Salir\n')

    if option != '3':
        metrics['total'] += 1

    if option == '1':
        metrics['success'] += 1

    return option != '3'


def run():
    data: dict = load_data()
    questions = list(data.keys())
    metrics = {'total': 0,
               'success': 0}

    play = True
    while (play):
        play = show_question(data, questions, metrics)

    clear()
    if metrics['total'] != 0:
        result = round((metrics["success"] * 10) / metrics["total"], 1)
        print(
            f'Puntuacion final = {result}')


if __name__ == '__main__':
    run()
