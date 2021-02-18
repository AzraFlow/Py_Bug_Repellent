from pybugrepellent.basic_to_chr import chr_dict

# Should rewrite this function using regex to recognize proper braced char codes
def charlist_to_code_list(charlist):
    '''
    Function to accept a line of code as
    a strings and return a list
    of corresponding cbm codes as integers
    '''
    codelist = []
    if len(charlist) <= 3:
        for i in range(len(charlist)):
            char = charlist[i]
            codelist.append(int(chr_dict[char]))
    else:
        for i in range(len(charlist)):
            if charlist[i] == "{":
                char = charlist[i:i+4]
                codelist.append(int(chr_dict[char]))
            elif charlist[i - 1] == "{":
                continue
            elif charlist[i - 2] == "{":
                continue
            elif charlist[i - 3] == "{":
                continue
            elif charlist[i] == "}":
                error = "Closing brace"
                return error
            else:
                char = charlist[i]
                codelist.append(int(chr_dict[char]))
    return codelist


def int_list_to_hilo_bytes(int_list):
    '''
    Function to take a list of integers, add them, and convert result into
    high and low bytes.
    '''
    num_total = 0
    for num in int_list:
        num_total += num
        hi_byte = int(num_total/256)
        lo_byte = num_total - hi_byte * 256
    return (hi_byte, lo_byte)


def hex_to_repellent_code(hex_value):
    hex_alpha_dict = {"0": "A", "1": "B", "2": "C", "3": "D",
                      "4": "E", "5": "F", "6": "G", "7": "H",
                      "8": "I", "9": "J", "a": "K", "b": "L",
                      "c": "M", "d": "N", "e": "O", "f": "P",
                      }
    left_two = str(hex_value)[-2:]
    left_two_to_alpha = hex_alpha_dict[left_two[0]] + hex_alpha_dict[left_two[1]]
    return left_two_to_alpha



codeline = "GOTO120"
print(codeline)

hilo_bytes = int_list_to_hilo_bytes(charlist_to_code_list(codeline))
print(hilo_bytes)

xor_hilo = hilo_bytes[0] ^ hilo_bytes[1]
print(xor_hilo)

hex_xor_hilo = hex(xor_hilo)

print(hex_xor_hilo)

print(hex_to_repellent_code(hex_xor_hilo))
