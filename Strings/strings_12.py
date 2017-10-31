def capitalize(string):
    s = string.split(' ')
    new = []
    for char in s:
        new.append(char.capitalize())
    return ' '.join(new)