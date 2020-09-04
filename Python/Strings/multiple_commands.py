## Problem: Bash has a property by which you can specify multiple files that share prefixes using the following format
## file{1,2}.txt => file1.txt, file2.txt
## {a,b,c}eee{1,2} => aeee1, beee1, ceee1, aeee2, beee2, ceee2

## My solution: Parse the data into a list of lists.
## For each list, recursively current character, and the rest of the list.

def parse_command(command):
    commands_list = []
    i = 0
    while i < len(command):
        if command[i] == '{':
            commands_list.append([])
            i += 1
            while i < len(command) and command[i] != '}':
                c = command[i]
                i += 1

                if c == ',':
                    continue
                commands_list[-1].append(c)
            i += 1
        else:
            c = []
            while i < len(command) and command[i] != '{':
                c.append(command[i])
                i += 1
            commands_list.append([''.join(c)])
    
    return commands_list

def generate_commands(command):
    commands_list = parse_command(command)

    ret = []

    def generate_commands_recursive(command_so_far, i):
        nonlocal ret, commands_list
        if i == len(commands_list):
            ret.append(command_so_far)
            return
        for command in commands_list[i]:
            generate_commands_recursive(command_so_far + command, i + 1)

    generate_commands_recursive('', 0)

    return ret


if __name__ == "__main__":
    print(generate_commands('{a,b,c}eee{1,2}'))

                