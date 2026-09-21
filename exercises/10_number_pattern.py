# freeCodeCamp python-v9 — Loops and Sequences
# Lab: Build a Number Pattern Generator
# This is a lab: I write the code myself from the requirements.
def number_pattern(n):
    if not isinstance(n, int):
        return "Argument must be an integer value."
    if n < 1:
        return "Argument must be an integer greater than 0."
    result = ""
    for i in range(1, n + 1):
        if result == "":
            result = str(i)
        else:
            result += " " + str(i)
    return result