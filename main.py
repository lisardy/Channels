import data.channel_loader
from calculations import CalculatedValues

# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from data import channel_loader


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

    X_values = channel_loader.get_X_values()
    calculator = CalculatedValues()

    b = calculator.get_b_value(X_values)
    print("b is {}".format(b))


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
