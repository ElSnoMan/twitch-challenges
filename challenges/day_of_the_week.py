"""
* Make an list that holds the textual values of the days of the week

* Have the user input a number corresponding to the day of the week
(Assume the week starts on Monday)

* Your program should output the string that represents the day

Examples:
    User inputs 1, your program should output "Monday"
"""


days = ['Monday', 'Tuesday', 'Wednesday',
        'Thursday', 'Friday', 'Saturday', 'Sunday']


def pick_a_day():
    number = int(input('Enter the number of the day you want. '))
    if number < 1 or number > 7:
        raise ValueError('Number must be between 1 and 7')

    day = days[number - 1]
    print(day)


if __name__ == '__main__':
    pick_a_day()
