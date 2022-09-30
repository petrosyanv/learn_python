import emoji
from learn_python.quiz import quiz_main_function
from learn_python.exercises import exercises_main_function
from learn_python.load import wait

if __name__ == '__main__':
    print(emoji.emojize(":brain: :rocket: WELCOME TO THE PYTHON CLASS :party_popper: :joystick:"))
    wait()
    print(emoji.emojize(":clipboard: QUIZ :pencil: write number: 1"))
    print(emoji.emojize(":memo: exercises :pencil: write number: 2"))
    category = input(emoji.emojize(":woman_teacher: Choose category: :right_arrow: "))
    if category == "1":
        quiz_main_function()
    elif category == "2":
        exercises_main_function()
    else:
        print("Unknown")

