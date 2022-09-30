import time

import animation
import emoji

one = emoji.emojize(":new_moon:")
two = emoji.emojize(":waxing_crescent_moon:")
three = emoji.emojize(":first_quarter_moon:")
four = emoji.emojize(":waxing_gibbous_moon:")
five = emoji.emojize(":full_moon:")
six = emoji.emojize(":waning_gibbous_moon:")
seven = emoji.emojize(":last_quarter_moon:")
eight = emoji.emojize(":waning_crescent_moon:")

moon = [f'{one}',
        f'{one}{two}',
        f'{one}{two}{three}',
        f'{one}{two}{three}{four}',
        f'{one}{two}{three}{four}{five}',
        f'{one}{two}{three}{four}{five}',
        f'{one}{two}{three}{four}{five}{six}',
        f'{one}{two}{three}{four}{five}{six}{seven}',
        f'{one}{two}{three}{four}{five}{six}{seven}{eight}{one}'
        ]


@animation.wait(moon)
def wait():
    time.sleep(3)
