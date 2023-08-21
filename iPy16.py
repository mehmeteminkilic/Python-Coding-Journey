""" Q.16. You own a Goal Parser that can interpret a string command. 
The command consists of an alphabet of "G", "()" and/or "(al)" in some order. 
The Goal Parser will interpret "G" as the string "G", "()" as the string "o", and "(al)" as the string "al". 
The interpreted strings are then concatenated in the original order. 
Given the string command, return the Goal Parser's interpretation of command.
Example 1:
Input: command = "G()(al)"
Output: "Goal"
Explanation: The Goal Parser interprets the command as follows: G -> G () -> o (al) -> al The final concatenated result is "Goal".
Example 2:
Input: command = "G()()()()(al)"
Output: "Gooooal" """

# Q16 Solution
import re

def interpret(command: str):
    dct = {"G":"G", "()": "o", "(al)":"al"}
    res = ""
    while len(command) > 0:
        if command[0] in dct:
            res += dct[command[0]]
            command = command[1:]
        elif command[:2] in dct:
            res += dct[command[:2]]
            command = command[2:]
        else:
            res += dct[command[:4]]
            command = command[4:]
    return res

def interpret2(command:str):
    return command.replace('()','o').replace('(al)','al')

def interpret3(command:str):
    return re.sub('\(\)', 'o', re.sub('\(al\)', 'al', command))

def interpret4(command:str):
    interpret = ""
    i = 0
    while i < len(command):
        if command[i] == 'G':
            interpret += 'G'
            i = i + 1
        elif command[i:i+2] == '()':
            interpret += 'o'
            i = i + 2
        elif command[i:i+4] == '(al)':
            interpret += 'al'
            i = i + 4
        else:
            i = i + 1
    return interpret

print(interpret("G()(al)"))
print(interpret2("G()(al)"))
print(interpret3("G()(al)"))
print(interpret4("G()(al)"))

print(interpret("G()()()()(al)"))
print(interpret2("G()()()()(al)"))
print(interpret3("G()()()()(al)"))
print(interpret4("G()()()()(al)"))
