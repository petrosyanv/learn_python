import emoji
from colorama import Fore, Style
import random


def quiz_main_function():
    print('YOU CHOSE QUIZ')
    function_list = [types_float, types_int, types_str, types_bool, types_list, types_dict, types_tuple,
                     types_list_more, answer_one, answer_two, answer_three, answer_four, answer_five,
                     answer_six, answer_seven, answer_eight]
    for i in range(len(function_list)):
        random.choice(function_list)()


def answer(right_answer: str):
    while True:
        answer_ = input(emoji.emojize(":ballot_box_with_ballot: YOUR ANSWER: :right_arrow: "))
        if answer_ == right_answer:
            print(emoji.emojize(":check_mark_button: Right answer"))
            return False
        else:
            print(emoji.emojize(":cross_mark: Wrong answer"))


def types_float():
    print(Style.BRIGHT + "SELECT TYPE: \n 10.30")
    print(Fore.GREEN + ' \t 1) int \t 2) float \t 3) long \t 4) double')
    answer('2')


def types_int():
    print(Style.BRIGHT + "SELECT TYPE: \n 1452")
    print(Fore.BLUE + ' \t 1) int \t 2) float \t 3) long \t 4) double')
    answer('1')


def types_str():
    print(Style.BRIGHT + "SELECT TYPE: \n 'False' ")
    print(Fore.CYAN + ' \t 1) bool \t 2) long \t 3) str')
    answer('3')


def types_bool():
    print(Style.BRIGHT + "SELECT TYPE: \n True ")
    print(Fore.YELLOW + ' \t 1) bool \t 2) long \t 3) str')
    answer('1')


def types_list():
    print(Style.BRIGHT + "SELECT TYPE: \n ['Tom', 'Sam', 'Bob'] ")
    print(Fore.CYAN + ' \t 1) list \t 2) tuple \t 3) dict \t 4) set')
    answer('1')


def types_dict():
    print(Style.BRIGHT + "SELECT TYPE: \n {1: 'Tom', 2: 'Bob', 3: 'Bill'} ")
    print(Fore.BLUE + ' \t 1) list \t 2) tuple \t 3) dict \t 4) set')
    answer('3')


def types_tuple():
    print(Style.BRIGHT + "SELECT TYPE: \n ('Tom', 23, '54') ")
    print(Fore.YELLOW + ' \t 1) list \t 2) tuple \t 3) dict \t 4) set')
    answer('2')


def types_list_more():
    print(Style.BRIGHT + "SELECT TYPE: \n [1, 2, 3, 4, 5] ")
    print(Fore.MAGENTA + ' \t 1) list \t 2) tuple \t 3) dict \t 4) set')
    answer('1')


def answer_one():
    print(Style.BRIGHT + "SELECT RIGHT OUTPUT: \n i = int('-2') \n print(len(i))")
    print(Fore.BLUE + ' \t 1) 2 \t 2) -2 \t 3) 1 \t 4) Error')
    answer('4')


def answer_two():
    print(Style.BRIGHT + "SELECT RIGHT OUTPUT: \n s = str(10.0) \n print(s)")
    print(Fore.GREEN + ' \t 1) 10.0 \t 2) 10 \t 3) 100 \t 4) Error')
    answer('1')


def answer_three():
    print(Style.BRIGHT + "SELECT RIGHT OUTPUT: \n d = dict('py') \n print(d)")
    print(Fore.CYAN + ' \t 1) py \t 2) {"p":"y"} \t 3) {"p", "y"} \t 4) Error')
    answer('4')


def answer_four():
    print(Style.BRIGHT + "SELECT RIGHT OUTPUT: \n b = bool('False') \n print(b)")
    print(Fore.YELLOW + ' \t 1) True \t 2) False \t 3) 0 \t 4) Error')
    answer('1')


def answer_five():
    print(Style.BRIGHT + "SELECT RIGHT OUTPUT: \n b = len(True) \n print(b)")
    print(Fore.CYAN + ' \t 1) 4 \t 2) 5 \t 3) 1 \t 4) Error')
    answer('4')


def answer_six():
    print(Style.BRIGHT + "SELECT RIGHT OUTPUT: \n a = '2' - 1 \n print(a)")
    print(Fore.BLUE + ' \t 1) 1 \t 2) 2-1 \t 3) -3 \t 4) Error')
    answer('4')


def answer_seven():
    print(Style.BRIGHT + "SELECT RIGHT OUTPUT: \n b = 'string'[3] \n print(b)")
    print(Fore.GREEN + ' \t 1) r \t 2) i \t 3) str \t 4) Error')
    answer('2')


def answer_eight():
    print(Style.BRIGHT + "SELECT RIGHT OUTPUT: \n d = dict(('01', 'py')) \n print(len(d))")
    print(Fore.MAGENTA + ' \t 1) 2 \t 2) 3 \t 3) 4 \t 4) Error')
    answer('1')


