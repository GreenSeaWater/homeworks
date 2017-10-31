def print_formatted(number):
    w = len(bin(number)[2:])
    for i in range(1, number+1):
        decimal = str(i).rjust(w, ' ')
        octal = oct(i)[1:].rjust(w, ' ')
        hexadecimal = hex(i)[2:].upper().rjust(w, ' ')
        binary = bin(i)[2:].rjust(w, ' ')
        print decimal + " " + octal + " " + hexadecimal + " " + binary