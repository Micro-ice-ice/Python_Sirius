import re
from sys import argv
import csv

# 0. Get input data

def regular_exp(lines, input_string):
    # lines = []
    #
    # while True:
    #     try:
    #         line = input()
    #         lines.append(line)
    #     except EOFError:
    #         break

    # input_string = ""
    # for i in range(1, len(argv)):
    #     input_string = input_string + argv[i]
    input_string = re.sub(r'\s+', '', input_string)
    # 1. check the string for the correctness

    # 2. Get the set of substrings (format <var> = %<type>)

    pattern_substring = r"[0-9]*[A-Za-z][A-Za-z0-9]*\s*=\s*%[dsf]"
    substrings = re.findall(pattern_substring, input_string)

    # 3. Get the dict of substrings (key = var, value = type)

    variables = []
    types = []

    for elem in substrings:
        v, t = elem.replace('%', '').split('=')
        variables.append(v)
        types.append(t)

    # 4. Generate regex string for searching using the dict

    pattern_d = r"-?[0-9]+"
    pattern_s = r".*"
    pattern_f = r"-?[0-9]+(?:\.[0-9]+)?"
    pattern_main = r""
    pattern_spaces = r"[ \t]*"
    pattern_split = r""

    for i in range(0, len(variables)):
        pattern_split += r'(?:'
        pattern_main += pattern_spaces + variables[i] + pattern_spaces + r"=" + pattern_spaces
        pattern_split += pattern_spaces + variables[i] + pattern_spaces + r"=" + pattern_spaces
        if types[i] == 'd':
            pattern_main += pattern_d
            pattern_split += pattern_d
        if types[i] == 'f':
            pattern_main += pattern_f
            pattern_split += pattern_f
        if types[i] == 's':
            pattern_main += pattern_s
            pattern_split += pattern_s
            if i != len(variables) - 1:
                pattern_split += r'(?=,)'
        pattern_main += pattern_spaces
        pattern_split += pattern_spaces
        pattern_split += r')'
        if i != len(variables) - 1:
            pattern_main += r','
            pattern_split += r'|'

    # 5. Find the equals in text

    equals = []

    for line in lines:
        if re.fullmatch(pattern_main, line):
            equals.append(line)

    headers_CSV = ['ID'] + variables

    with open('CSVFILE.csv', 'w', newline='') as f_object:
        dict_writer_object = csv.DictWriter(f_object, fieldnames=headers_CSV)
        dict_writer_object.writeheader()
        f_object.close()

    j = 0
    for elem in equals:
        i = 0
        result = dict()
        result["ID"] = j
        for sub_element in re.findall(pattern_split, elem):
            value = sub_element.split('=')[1]
            if types[i] != 's':
                value = value.replace(' ', '')
            result[variables[i]] = value
            i += 1
        with open('CSVFILE.csv', 'a', newline='') as f_object:
            dict_writer_object = csv.DictWriter(f_object, fieldnames=headers_CSV)
            dict_writer_object.writerow(result)
            f_object.close()
        j += 1


