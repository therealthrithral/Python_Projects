import re

problems_for_saving = ["32 + 698", "3801 - 2", "45 + 43", "123 + 49"] # List of problem strings


def arithmetic_arranger(problems, show_answers=False):
    line1 = ""  # Set each line to blank
    line2 = ""  # Set each line to blank
    line3 = ""  # Set each line to blank
    line4 = ""  # Set each line to blank

    if len(problems) > 5: # Checks problem count to make sure system can handle number of problems
        return "Error: Too many problems."

    for problem in problems:
        op = re.search('\\s[+-]\\s', problem) # Regex to make sure of operator
        if op is None: # Check for ensuring operator
            return "Error: Operator must be '+' or '-'."
        op = op.group().strip()
        problem = problem.split(op)
        a, b = problem[0].strip(), problem[1].strip()
        if not a.isdigit() or not b.isdigit(): # Check for ensuring digits only
            return "Error: Numbers must only contain digits."
        if len(a) > 4 or len(b) > 4:  # Check for ensuring number doesn't exceed length
            return "Error: Numbers cannot be more than four digits."
        if len(line1) > 0:
            line1 = line1 + 4 * " "
            line2 = line2 + 4 * " "
            line3 = line3 + 4 * " "
        pad = len(a) + 2 if len(a) > len(b) else len(b) + 2
        line1 = line1 + a.rjust(pad, " ")
        line2 = line2 + op + (pad - 1 - len(b)) * " " + b
        line3 = line3 + pad * "-"
        if show_answers is True:
            if len(line4) > 0:
                line4 = line4 + 4 * " "
            if op == "+":
                x = int(a) + int(b)
                line4 = line4 + str(x).rjust(pad, " ")
            else:
                x = int(a) - int(b)
                line4 = line4 + str(x).rjust(pad, " ")
    arranged_problems = line1 + '\n' + line2 + '\n' + line3
    if len(line4) > 0: arranged_problems = arranged_problems + '\n' + line4
    return arranged_problems


def main(): # Main function
    print(arithmetic_arranger(problems_for_saving, show_answers=True)) # Print call to function call showing answers


main()


