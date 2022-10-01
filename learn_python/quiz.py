import emoji
from colorama import Fore, Style
import random


def quiz_main_function():
    print('YOU CHOSE QUIZ')
    function_list = [types_float, types_int, types_str, types_bool, types_list, types_dict, types_tuple,
                     types_list_more, answer_one, answer_two, answer_three, answer_four, answer_five,
                     answer_six, answer_seven, answer_eight, true_false_1, true_false_2, true_false_3(), true_false_4(),
                     true_false_5(), true_false_6(), true_false_7(), true_false_8(), true_false_9(), true_false_10(),
                     true_false_11(), true_false_12(), true_false_13(), true_false_14()]
    for i in range(len(function_list)):
        random.choice(function_list)()


def rnd_color():
    colors = [Fore.BLUE, Fore.GREEN, Fore.YELLOW, Fore.CYAN, Fore.MAGENTA, Fore.RED, Fore.LIGHTYELLOW_EX,
              Fore.LIGHTBLUE_EX]
    return random.choice(colors)


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


def true_false_1():
    print(Style.BRIGHT + "SELECT RIGHT OUTPUT: \n In Python, Dictionaries are immutable?")
    print(rnd_color() + ' \t 1) True \t 2) False')
    answer('1')


def true_false_2():
    print(Style.BRIGHT + "SELECT RIGHT OUTPUT: \n dict1 = {'key1':1, 'key2':2} \n dict2 = {'key2':2, 'key1:1} \n print(dict1 == dict2)")
    print(rnd_color() + ' \t 1) True \t 2) False')
    answer('1')


def true_false_3():
    print(Style.BRIGHT + 'Please select all correct ways to empty the following dictionary')
    print(Style.BRIGHT + ' student = { \n\t"name": "Emma", \n\t"class": 9, \n\t"marks": 75 \n}')
    print(rnd_color() + ' \t 1)  del student \t 2) del student[0:2] \t 3) student.clear()')
    answer('3')


def true_false_4():
    print(Style.BRIGHT + "SELECT RIGHT OUTPUT: \n Select correct ways to create an empty dictionary")
    print(rnd_color() + ' \t 1)  sampleDict = {} \t 2) sampleDict = () \t 3) sampleDict = dict{}')
    answer('1')


def true_false_5():
    print(Style.BRIGHT + "SELECT RIGHT OUTPUT: \n  Items are accessed by their position in a dictionary and All the keys in a dictionary must be of the same type.")
    print(rnd_color() + ' \t 1) True \t 2) False')
    answer('2')


def true_false_6():
    print(Style.BRIGHT + "SELECT RIGHT OUTPUT: \n Select all correct ways to copy a dictionary in Python")
    print(rnd_color() + ' \t 1)  dict2 = dict1.copy() \t 2) dict2.append(dict1) \t 3) dict2 = dict1')
    answer('1')


def true_false_7():
    print(Style.BRIGHT + 'SELECT RIGHT OUTPUT:\n dict1 = {"name": "Mike", "salary": 8000}\n temp = dict1.pop("age")\n print(temp)')
    print(rnd_color() + ' \t 1)  KeyError: ‘age’ \t 2) None')
    answer('1')


def true_false_8():
    print(Style.BRIGHT + 'Select the correct way to print Emma’s age.')
    print(Style.BRIGHT + "SELECT RIGHT OUTPUT: \n student = {1: {'name': 'Emma', 'age': '27', 'sex': 'Female'}, \n\t2: {'name': 'Mike', 'age': '22', 'sex': 'Male'}}")
    print(rnd_color() + ' \t 1) student[0][1] \t 2) student[1]["age"] \t 3) student[0]["age"]')
    answer('2')


def true_false_9():
    print(Style.BRIGHT + 'Select the correct ways to get the value of marks key.')
    print(Style.BRIGHT + 'SELECT RIGHT OUTPUT: \n student = {\n\t"name": "Emma",\n\t"class": 9,\n\t"marks": 75}')
    print(rnd_color() + " \t1)  m = student.get(2)\t2) m = student.get('marks')\t3) m = student[2])")
    answer('2')


def true_false_10():
    print(Style.BRIGHT + 'SELECT RIGHT OUTPUT: \n dict1 = {"name": "Mike", "salary": 8000} \n temp = dict1.get("age") \n print(temp)')
    print(rnd_color() + ' \t 1)  KeyError: ‘age’ \t 2) None')
    answer('2')


def true_false_11():
    print(Style.BRIGHT + 'Select the all correct way to remove the key marks from a dictionary')
    print(Style.BRIGHT + 'SELECT RIGHT OUTPUT: \n student = { \n\t"name": "Emma", \n\t"class": 9, \n\t"marks": 75 \n}')
    print(rnd_color() + ' \t 1) student.pop("marks") \t 2) student.remove("marks") \t 3)student.popitem("marks")')
    answer('1')


def true_false_12():
    print(Style.BRIGHT + "SELECT RIGHT OUTPUT: \ndef fun1(num): \n\treturn num + 25\n\nfun1(5)\nprint(num)")
    print(rnd_color() + ' \t 1) 25 \t 2) 5 \t 3)NameError')
    answer('3')


def true_false_13():
    print(Style.BRIGHT + "SELECT RIGHT OUTPUT: \ndef fun1(name, age=20): \n\tprint(name, age)\n\nfun1('Emma', 25)")
    print(rnd_color() + ' \t 1) Emma 25 \t 2) Emma 20')
    answer('1')


def true_false_14():
    print(Style.BRIGHT + "SELECT RIGHT OUTPUT: \ndef add(a, b): \n\treturn a+5, b+5\n\nresult = add(3, 2)\nprint(result)")
    print(rnd_color() + ' \t 1) 15 \t 2) 8 \t 3) (8,7) \t 4) SyntaxError')
    answer('3')
