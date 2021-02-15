

from basic_to_chr import chr_dict

def line_to_charlist(line_of_code):
    charlist = []
    for char in line_of_code:
        charlist.append(char)
    return charlist


def charlist_to_code_list(charlist):
    codelist = []
    for char in charlist:
        codelist.append(chr_dict[char])
    return codelist

print(charlist_to_code_list("ABCD"))
