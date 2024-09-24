def evaluate_condition(variable, operation, value) -> bool:
    """Evaluate a condition"""

    if operation == ">":
        return variable > value
    elif operation == "<":
        return variable < value
    elif operation == ">=":
        return variable >= value
    elif operation == "<=":
        return variable <= value
    elif operation == "==":
        return variable == value
    elif operation == "!=":
        return variable != value


def process_instructions(texte) -> int:
    """Process all instructions"""

    list_instructions = texte.strip().split("\n")

    dic_variables = {}
    max_value_running = float("-inf")

    for instruction in list_instructions:

        # Split the instruction into parts
        var, op, val, _, cond_var, cond_op, cond_val = instruction.split()

        # Add the variables to the dictionary if they do not exist
        if cond_var not in dic_variables.keys():
            dic_variables[cond_var] = 0
        if var not in dic_variables.keys():
            dic_variables[var] = 0

        # if the condition is met
        if evaluate_condition(dic_variables[cond_var], cond_op, int(cond_val)):
            if op == "inc":
                dic_variables[var] += int(val)
            elif op == "dec":
                dic_variables[var] -= int(val)

            max_value_running = max(max_value_running, dic_variables[var])

    max_value_final = max(dic_variables.values())

    return max_value_final * max_value_running


if __name__ == "__main__":

    text_input = open("doc/remise-en-jambe/tp2/2024/data/instructions.txt", "r").read()

    example1 = """b inc 4 if a > 1
a inc 1 if b < 2
c dec -5 if a >= 1
c inc -10 if c == 5"""

    print("Exemple1 :", process_instructions(example1), process_instructions(example1) == 5)
    print("Fichier : ", process_instructions(text_input))
