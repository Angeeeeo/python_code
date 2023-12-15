import tkinter as tk
from tkinter import messagebox
import random

# Первый набор вопросов и ответов
questions1 = [
    {
        'question': 'Команда, которая используется для передачи управления из функции к вызывающей функции - это ...',
        'answers': ['go back', 'goto', 'return', 'switch'],
        'correct_index': 2
    },
    {
        'question': 'Выберете однострочные комментарии в С++',
        'answers': ['//', '##', '()', '/*'],
        'correct_index': 0
    },
    {
        'question': 'Тело любого цикла выполняется до тех пор, пока его условие',
        'answers': ['не закончится точкой с запятой', 'у цикла нет условия', 'истинно', 'ложно'],
        'correct_index': 3
    },
    {
        'question': 'Укажите правильный вариант объявления указателя в C++',
        'answers': ['int *x', 'int & x', 'int x', 'ptr x'],
        'correct_index': 0
    },
]

# Второй набор вопросов и ответов
questions2 = [
    {
        'question': 'В каком случае выражение С++ будет исчисляться быстрее',
        'answers': ['X+=Y', 'X=Y+X', 'X=X+Y', 'Одинаковая скоростью у всех 3 выражений'],
        'correct_index': 3
    },
    {
        'question': 'Какой операции нет в С++',
        'answers': ['Последовательной', 'Бинарной', 'Тернарной', 'Унарной'],
        'correct_index': 0
    },
    {
        'question': 'Число, используемое для обращения к отдельному элементу массива',
        'answers': ['индекс', 'позиция', 'тип', 'значение'],
        'correct_index': 0
    },
    {
        'question': 'Списки и таблицы значений хранятся в',
        'answers': ['массиве', 'в библиотеке', 'указателе', 'списке'],
        'correct_index': 0
    },
]

# Переменная для отслеживания количества правильных ответов
correct_answers = 0

# Функция для проверки ответа
def check_answer(answer):
    global correct_answers
    correct_index = current_questions[current_question]['correct_index']
    if answer == current_questions[current_question]['answers'][correct_index]:
        correct_answers += 1
        answer_buttons[correct_index].config(bg='green')  # Подсветим правильный ответ
    else:
        answer_buttons[correct_index].config(bg='green')
        for i, btn in enumerate(answer_buttons):
            if i != correct_index and btn['text'] == answer:
                btn.config(bg='red')  # Подсветим неправильный ответ

    root.after(1000, next_question)  # Переходим к следующему вопросу через 1 секунду

# Функция для перехода к следующему вопросу
def next_question():
    global current_question
    if current_question < len(current_questions) - 1:
        current_question += 1
        show_question()
    else:
        if current_question == len(current_questions) - 1:
            show_result()

# Функция для отображения результата
def show_result():
    result = messagebox.showinfo('Результат', f'Вы ответили правильно на {correct_answers} из {len(current_questions)} вопросов.')
    if result:
        root.quit()

# Функция для отображения текущего вопроса и вариантов ответов
def show_question():
    question_label.config(text=current_questions[current_question]['question'])
    for i, answer in enumerate(current_questions[current_question]['answers']):
        answer_buttons[i].config(text=answer, bg='#ce93d8')  # Сбросим цвет кнопок

# Функция для выбора теста
def choose_test():
    global current_questions, current_question, correct_answers
    current_question = 0
    correct_answers = 0
    current_questions = random.choice([questions1, questions2])
    show_question()

# Функция для завершения работы программы
def on_closing():
    if messagebox.askokcancel("Выход", "Хотите завершить программу?"):
        root.destroy()

# Создание графического интерфейса
root = tk.Tk()
root.title('Тренажер по программированию')
root.configure(bg='#e1bee7')  # Изменим фон окна
root.option_add('*Font', 'Arial 14 bold')  # Изменим стиль и размер шрифта
root.protocol("WM_DELETE_WINDOW", on_closing)

# Рамка для отображения вопроса
question_frame = tk.Frame(root, bg='#e1bee7')  # Добавим рамку вокруг вопроса
question_frame.pack(pady=10)

question_label = tk.Label(question_frame, text='', font=('Arial', 16, 'bold'), bg='#e1bee7')  # Изменим стиль текста
question_label.pack()

# Рамка для кнопок с вариантами ответов
button_frame = tk.Frame(root, bg='#e1bee7')  # Изменим фон рамки кнопок
button_frame.pack(pady=5)

# Кнопки для вариантов ответов
answer_buttons = []
for i in range(4):
    button = tk.Button(button_frame, text='', font=('Arial', 14), width=45, bg='#ce93d8', fg='white', command=lambda i=i: check_answer(answer_buttons[i]['text']))
    button.pack(pady=5, fill=tk.X)
    answer_buttons.append(button)

# Выбор теста
choose_test()

# Запуск главного цикла приложения
root.mainloop()
