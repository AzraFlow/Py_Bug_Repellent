from pybugrepellent.basic_to_chr import chr_dict


def line_to_charlist(line_of_code):
    return [char for char in line_of_code]

'''
def charlist_to_code_list(charlist):
    codelist = []
    for char in charlist:      
        codelist.append(int(chr_dict[char]))
    return codelist
'''


def charlist_to_code_list(charlist):
    codelist = []
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
        else:
            char = charlist[i]
            codelist.append(int(chr_dict[char]))
    return codelist


print(charlist_to_code_list("ABCD"))
