def lib_func_load(lib_path):
    #functions load
    lib_functions = {}
    if lib_path != "":
        f = open(lib_path)
        lib_functions = {}
        lib_func_load_proc = True
        while lib_func_load_proc:
            current_line = f.readline()
            if "def_func" in current_line:
                current_line_temp = current_line.split()
                lib_functions[current_line_temp[1]] = current_line_temp[2]
            elif "$" in current_line:
                pass
            
            if not current_line:
                lib_func_load_proc = False
    else:
        pass
    return lib_functions

def random_value(a,b):
    import random
    return random.randint(a,b)