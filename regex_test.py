import re
from pybugrepellent.basic_to_chr import chr_dict
# from basic_to_chr import Chr_dict

text = "{WH}{CD}{RV}{HM}{RD}{CR}{GN}{BL}{OR}{F1}{F2}{F3}{F4}{F5}{F6}{F7}{F8}{BK}{CU}{RO}{SC}{IN}{BR}{LR}{G1}{G2}{LG}{LB}{G3}{PU}{CL}{YL}{CY}{SS}"

str_split = re.split(r"\{\w{2}\}", text)
code_split = re.findall(r"\{\w{2}\}", text)
code_split.append('')  # Set proper list length to use count enumerate

codelist = []

for count, segment in enumerate(str_split):
    for char in segment:
        codelist.append(int(chr_dict[char]))
    codelist.append(int(chr_dict[code_split[count]]))

print(codelist)
