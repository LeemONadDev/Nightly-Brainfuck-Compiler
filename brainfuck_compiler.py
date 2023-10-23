import sys
import brainfuck_compiler_additional as bfca
Args = sys.argv
f = open(Args[1])

try:
    inc_lib = Args[2]
except:
    inc_lib = ""

#Nodet (Nightly) 1.3bfc ---> to Brainf**k compiler

#Switchers
functions = {}
lib_functions = {}
compiling_process = True
compiled_code = ""
errors = []
current_pos = 0 #0 cell for echo
f_dump_c_end = False
pointer_pos_dump_c_end = False
errors_dump_c_end_disable = False
lib_func_dump_c_end = False
#
print("\n " * 100)

try:
    lib_functions = bfca.lib_func_load(Args[2])
except:
    pass

while compiling_process:
    current_line = f.readline()
    if "echo" in current_line:
        if current_pos == 0:
            pass
        else:
            compiled_code += "<" * current_pos
        printed_text = current_line[current_line.index("echo")+5:]
        for x in range(len(printed_text)):
            compiled_code += "+" * ord(printed_text[x]) + "."
            compiled_code += "[-]"
        compiled_code += ">" * current_pos
    elif "move_r!" in current_line:
        compiled_code += ">"
        current_pos += 1

    elif "move_l!" in current_line:
        compiled_code += "<"
        current_pos -= 1

    elif "movec_l" in current_line:
        current_pos -= int(current_line[current_line.index("movec_l")+8:])
        compiled_code += int(current_line[current_line.index("movec_l")+8:]) * "<"
    elif "movec_r" in current_line:
        current_pos += int(current_line[current_line.index("movec_r")+8:])
        compiled_code += int(current_line[current_line.index("movec_r")+8:]) * ">"
    
    elif "zero!" in current_line:
        compiled_code += "[-]"

    elif "add" in current_line:
        compiled_code += int(current_line[current_line.index("add")+4:]) * "+"
    
    elif "minus" in current_line:
        compiled_code += int(current_line[current_line.index("minus")+6:]) * "-"

    elif "$" in current_line:
        pass

    elif "bf_code" in current_line:
        compiled_code += current_line[current_line.index("bf_code")+8:]
        current_pos += current_line[current_line.index("bf_code")+8:].count(">")
        current_pos -= current_line[current_line.index("bf_code")+8:].count("<")

    elif "def_func" in current_line:
        current_line_temp = current_line.split()
        functions[current_line_temp[1]] = current_line_temp[2]

    elif "func_call" in current_line:
        if ("lib_func_call" in current_line) == False:
            current_line_temp = current_line.split()
            try:
                compiled_code += functions[current_line_temp[1]]
            except:
                errors_temp = "bfc error: function " + current_line_temp[1] +" is not defined"
                errors.append(errors_temp)
        else:
            current_line_temp = current_line.split()
            try:
                compiled_code += lib_functions[current_line_temp[1]]
            except:
                errors_temp = "bfc error: lib function " + current_line_temp[1] +" is not defined"
                errors.append(errors_temp)

    elif "func_dump_c_end!" in current_line:
        f_dump_c_end = True
    
    elif "pointer_pos_dump_c_end!" in current_line:
        pointer_pos_dump_c_end = True
    
    elif "errors_dump_c_end_disable!" in current_line:
        errors_dump_c_end_disable = True

    elif "lib_func_dump_c_end!" in current_line:
        lib_func_dump_c_end = True

    if not current_line:
        break
print("- - - - - - - - - - - - - - - -Compiled code!- - - - - - - - - - - - - - - - ")
print(compiled_code)
print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
if f_dump_c_end == True:
    print(functions)
    print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
if pointer_pos_dump_c_end == True:
    print(current_pos)
    print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
if errors_dump_c_end_disable != True:
    if errors != []:
        print(*errors,sep="\n")
        print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
if lib_func_dump_c_end == True:
    print(lib_functions)
    print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
print("Program compiled")