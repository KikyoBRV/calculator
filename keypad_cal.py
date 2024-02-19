from keypad_ui import KeypadUI
from math import *


class CalculatorController:
    def __init__(self):
        # Initialize any variables or state needed for the calculator
        self.result = 0

    def add(self, num1, num2):
        # Method to add two numbers
        return num1 + num2

    def subtract(self, num1, num2):
        # Method to subtract num2 from num1
        return num1 - num2

    def multiply(self, num1, num2):
        # Method to multiply two numbers
        return num1 * num2

    def divide(self, num1, num2):
        # Method to divide num1 by num2
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Division by zero"

    def exp(self, num1, num2):
