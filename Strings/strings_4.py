def mutate_string(string, position, character):                
    string_list = list(string)
    string_list[position] = character
    return ''.join(string_list)