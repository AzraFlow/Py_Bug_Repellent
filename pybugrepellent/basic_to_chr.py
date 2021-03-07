chr_dict = {
            "": "0",    
            "": "1",
            "": "2",
            "": "3",
            "": "4",
            "{WH}": "5",
            "": "6",
            "": "7",
            "disSHIFT+C=": "8",
            "enaSHIFT+C=": "9",
            "": "10",
            "": "11",
            "": "12",
            "return": "13",
            "lower case": "14",
            "": "15",
            "": "16",
            "{CD}": "17",
            "{RV}": "18",
            "{HM}": "19",
            "{del}": "20",
            "": "21",
            "": "22",
            "": "23",
            "": "24",
            "": "25",
            "": "26",
            "": "27",
            "{RD}": "28",
            "{CR}": "29",
            "{GN}": "30",
            "{BL}": "31",
            " ": "32",
            "!": "33",
            '"': "34",
            "#": "35",
            "$": "36",
            "%": "37",
            "&": "38",
            "'": "39",
            "(": "40",
            ")": "41",
            "*": "42",
            "+": "43",
            ",": "44",
            "-": "45",
            ".": "46",
            "/": "47",
            "0": "48",
            "1": "49",
            "2": "50",
            "3": "51",
            "4": "52",
            "5": "53",
            "6": "54",
            "7": "55",
            "8": "56",
            "9": "57",
            ":": "58",
            ";": "59",
            "<": "60",
            "=": "61",
            ">": "62",
            "?": "63",
            "@": "64",
            "A": "65",
            "B": "66",
            "C": "67",
            "D": "68",
            "E": "69",
            "F": "70",
            "G": "71",
            "H": "72",
            "I": "73",
            "J": "74",
            "K": "75",
            "L": "76",
            "M": "77",
            "N": "78",
            "O": "79",
            "P": "80",
            "Q": "81",
            "R": "82",
            "S": "83",
            "T": "84",
            "U": "85",
            "V": "86",
            "W": "87",
            "X": "88",
            "Y": "89",
            "Z": "90",
            "[": "91",
            "pound": "92",
            "]": "93",
            "^": "94",
            "{arrow left}": "95",
            "": "96",
            "": "97",
            "": "98",
            "": "99",
            "": "100",
            "": "101",
            "": "102",
            "": "103",
            "": "104",
            "": "105",
            "": "106",
            "": "107",
            "": "108",
            "": "109",
            "": "110",
            "": "111",
            "": "112",
            "": "113",
            "": "114",
            "": "115",
            "": "116",
            "": "117",
            "": "118",
            "": "119",
            "": "120",
            "": "121",
            "": "122",
            "": "123",
            "": "124",
            "": "125",
            "": "126",
            "": "127",
            "": "128",
            "{OR}": "129",
            "": "130",
            "": "131",
            "": "132",
            "{F1}": "133",
            "{F2}": "134",
            "{F3}": "135",
            "{F4}": "136",
            "{F5}": "137",
            "{F6}": "138",
            "{F7}": "139",
            "{F8}": "140",
            "shift+ret.": "141",
            "upper case": "142",
            "": "143",
            "{BK}": "144",
            "{CU}": "145",
            "{RO}": "146",
            "{SC}": "147",
            "{IN}": "148",
            "{BR}": "149",
            "{LR}": "150",
            "{G1}": "151",
            "{G2}": "152",
            "{LG}": "153",
            "{LB}": "154",
            "{G3}": "155",
            "{PU}": "156",
            "{CL}": "157",
            "{YL}": "158",
            "{CY}": "159",
            "{SS}": "160",
            "": "161",
            "": "162",
            "": "163",
            "": "164",
            "": "165",
            "": "166",
            "": "167",
            "": "168",
            "": "169",
            "": "170",
            "": "171",
            "": "172",
            "": "173",
            "": "174",
            "": "175",
            "": "176",
            "": "177",
            "": "178",
            "": "179",
            "": "180",
            "": "181",
            "": "182",
            "": "183",
            "": "184",
            "": "185",
            "": "186",
            "": "187",
            "": "188",
            "": "189",
            "": "190",
            "": "191"
            }

# CODES 192-223 SAME AS  96-127
# CODES 224-254 SAME AS 160-190
# CODE 255 SAME AS 126

if __name__ == "__main__":
    pass

""" Reference data:

    '\ufffe'   0 #  0x00 -> UNDEFINED
    '\ufffe'   1 #  0x01 -> UNDEFINED
    '\ufffe'   2 #  0x02 -> UNDEFINED
    '\ufffe'   3 #  0x03 -> UNDEFINED
    '\ufffe'   4 #  0x04 -> UNDEFINED
    '\uf100'   5 #  0x05 -> WHITE COLOR SWITCH (CUS)
    '\ufffe'   6 #  0x06 -> UNDEFINED
    '\ufffe'   7 #  0x07 -> UNDEFINED
    '\uf118'   8 #  0x08 -> DISABLE CHARACTER SET SWITCHING (CUS)
    '\uf119'   9 #  0x09 -> ENABLE CHARACTER SET SWITCHING (CUS)
    '\ufffe'  10 #  0x0A -> UNDEFINED
    '\ufffe'  11 #  0x0B -> UNDEFINED
    '\ufffe'  12 #  0x0C -> UNDEFINED
    '\r'      13 #  0x0D -> CARRIAGE RETURN
    '\x0e'    14 #  0x0E -> SHIFT OUT
    '\ufffe'   15 #  0x0F -> UNDEFINED
    '\ufffe'   16 #  0x10 -> UNDEFINED
    '\uf11c'   17 #  0x11 -> CURSOR DOWN (CUS)
    '\uf11a'   18 #  0x12 -> REVERSE VIDEO ON (CUS)
    '\uf120'   19 #  0x13 -> HOME (CUS)
    '\x7f'     20 #  0x14 -> DELETE
    '\ufffe'   21 #  0x15 -> UNDEFINED
    '\ufffe'   22 #  0x16 -> UNDEFINED
    '\ufffe'   23 #  0x17 -> UNDEFINED
    '\ufffe'   24 #  0x18 -> UNDEFINED
    '\ufffe'   25 #  0x19 -> UNDEFINED
    '\ufffe'   26 #  0x1A -> UNDEFINED
    '\ufffe'   27 #  0x1B -> UNDEFINED
    '\uf101'   28 #  0x1C -> RED COLOR SWITCH (CUS)
    '\uf11d'   29 #  0x1D -> CURSOR RIGHT (CUS)
    '\uf102'   30 #  0x1E -> GREEN COLOR SWITCH (CUS)
    '\uf103'   31 #  0x1F -> BLUE COLOR SWITCH (CUS)
    ' '        32 #  0x20 -> SPACE
    '!'        33 #  0x21 -> EXCLAMATION MARK
    '"'        34 #  0x22 -> QUOTATION MARK
    '#'        35 #  0x23 -> NUMBER SIGN
    '$'        36 #  0x24 -> DOLLAR SIGN
    '%'        37 #  0x25 -> PERCENT SIGN
    '&'        38 #  0x26 -> AMPERSAND
    "'"        39 #  0x27 -> APOSTROPHE
    '('        40 #  0x28 -> LEFT PARENTHESIS
    ')'        41 #  0x29 -> RIGHT PARENTHESIS
    '*'        42 #  0x2A -> ASTERISK
    '+'        43 #  0x2B -> PLUS SIGN
    ','        44 #  0x2C -> COMMA
    '-'        45 #  0x2D -> HYPHEN-MINUS
    '.'        46 #  0x2E -> FULL STOP
    '/'        47 #  0x2F -> SOLIDUS
    '0'        48 #  0x30 -> DIGIT ZERO
    '1'        49 #  0x31 -> DIGIT ONE
    '2'        50 #  0x32 -> DIGIT TWO
    '3'        51 #  0x33 -> DIGIT THREE
    '4'        52 #  0x34 -> DIGIT FOUR
    '5'        53 #  0x35 -> DIGIT FIVE
    '6'        54 #  0x36 -> DIGIT SIX
    '7'        55 #  0x37 -> DIGIT SEVEN
    '8'        56 #  0x38 -> DIGIT EIGHT
    '9'        57 #  0x39 -> DIGIT NINE
    ':'        58 #  0x3A -> COLON
    ';'        59 #  0x3B -> SEMICOLON
    '<'        60 #  0x3C -> LESS-THAN SIGN
    '='        61 #  0x3D -> EQUALS SIGN
    '>'        62 #  0x3E -> GREATER-THAN SIGN
    '?'        63 #  0x3F -> QUESTION MARK
    '@'        64 #  0x40 -> COMMERCIAL AT
    'A'        65 #  0x41 -> LATIN CAPITAL LETTER A
    'B'        66 #  0x42 -> LATIN CAPITAL LETTER B
    'C'        67 #  0x43 -> LATIN CAPITAL LETTER C
    'D'        68 #  0x44 -> LATIN CAPITAL LETTER D
    'E'        69 #  0x45 -> LATIN CAPITAL LETTER E
    'F'        70 #  0x46 -> LATIN CAPITAL LETTER F
    'G'        71 #  0x47 -> LATIN CAPITAL LETTER G
    'H'        72 #  0x48 -> LATIN CAPITAL LETTER H
    'I'        73 #  0x49 -> LATIN CAPITAL LETTER I
    'J'        74 #  0x4A -> LATIN CAPITAL LETTER J
    'K'        75 #  0x4B -> LATIN CAPITAL LETTER K
    'L'        76 #  0x4C -> LATIN CAPITAL LETTER L
    'M'        77 #  0x4D -> LATIN CAPITAL LETTER M
    'N'        78 #  0x4E -> LATIN CAPITAL LETTER N
    'O'        79 #  0x4F -> LATIN CAPITAL LETTER O
    'P'        80 #  0x50 -> LATIN CAPITAL LETTER P
    'Q'        81 #  0x51 -> LATIN CAPITAL LETTER Q
    'R'        82 #  0x52 -> LATIN CAPITAL LETTER R
    'S'        83 #  0x53 -> LATIN CAPITAL LETTER S
    'T'        84 #  0x54 -> LATIN CAPITAL LETTER T
    'U'        85 #  0x55 -> LATIN CAPITAL LETTER U
    'V'        86 #  0x56 -> LATIN CAPITAL LETTER V
    'W'        87 #  0x57 -> LATIN CAPITAL LETTER W
    'X'        88 #  0x58 -> LATIN CAPITAL LETTER X
    'Y'        89 #  0x59 -> LATIN CAPITAL LETTER Y
    'Z'        90 #  0x5A -> LATIN CAPITAL LETTER Z
    '['        91 #  0x5B -> LEFT SQUARE BRACKET
    '\xa3'     92 #  0x5C -> POUND SIGN
    ']'        93 #  0x5D -> RIGHT SQUARE BRACKET
    '\u2191'   94 #  0x5E -> UPWARDS ARROW
    '\u2190'   95 #  0x5F -> LEFTWARDS ARROW
    '\u2500'   96 #  0x60 -> BOX DRAWINGS LIGHT HORIZONTAL
    '\u2660'   97 #  0x61 -> BLACK SPADE SUIT
    '\u2502'   98 #  0x62 -> BOX DRAWINGS LIGHT VERTICAL
    '\u2500'   99 #  0x63 -> BOX DRAWINGS LIGHT HORIZONTAL
    '\uf122'  100 #  0x64 -> BOX DRAWINGS LIGHT HORIZONTAL ONE QUARTER UP (CUS)
    '\uf123'  101 #  0x65 -> BOX DRAWINGS LIGHT HORIZONTAL TWO QUARTERS UP (CUS)
    '\uf124'  102 #  0x66 -> BOX DRAWINGS LIGHT HORIZONTAL ONE QUARTER DOWN (CUS)
    '\uf126'  103 #  0x67 -> BOX DRAWINGS LIGHT VERTICAL ONE QUARTER LEFT (CUS)
    '\uf128'  104 #  0x68 -> BOX DRAWINGS LIGHT VERTICAL ONE QUARTER RIGHT (CUS)
    '\u256e'  105 #  0x69 -> BOX DRAWINGS LIGHT ARC DOWN AND LEFT
    '\u2570'  106 #  0x6A -> BOX DRAWINGS LIGHT ARC UP AND RIGHT
    '\u256f'  107 #  0x6B -> BOX DRAWINGS LIGHT ARC UP AND LEFT
    '\uf12a'  108 #  0x6C -> ONE EIGHTH BLOCK UP AND RIGHT (CUS)
    '\u2572'  109 #  0x6D -> BOX DRAWINGS LIGHT DIAGONAL UPPER LEFT TO LOWER RIGHT
    '\u2571'  110 #  0x6E -> BOX DRAWINGS LIGHT DIAGONAL UPPER RIGHT TO LOWER LEFT
    '\uf12b'  111 #  0x6F -> ONE EIGHTH BLOCK DOWN AND RIGHT (CUS)
    '\uf12c'  112 #  0x70 -> ONE EIGHTH BLOCK DOWN AND LEFT (CUS)
    '\u25cf'  113 #  0x71 -> BLACK CIRCLE
    '\uf125'  114 #  0x72 -> BOX DRAWINGS LIGHT HORIZONTAL TWO QUARTERS DOWN (CUS)
    '\u2665'  115 #  0x73 -> BLACK HEART SUIT
    '\uf127'  116 #  0x74 -> BOX DRAWINGS LIGHT VERTICAL TWO QUARTERS LEFT (CUS)
    '\u256d'  117 #  0x75 -> BOX DRAWINGS LIGHT ARC DOWN AND RIGHT
    '\u2573'  118 #  0x76 -> BOX DRAWINGS LIGHT DIAGONAL CROSS
    '\u25cb'  119 #  0x77 -> WHITE CIRCLE
    '\u2663'  120 #  0x78 -> BLACK CLUB SUIT
    '\uf129'  121 #  0x79 -> BOX DRAWINGS LIGHT VERTICAL TWO QUARTERS RIGHT (CUS)
    '\u2666'  122 #  0x7A -> BLACK DIAMOND SUIT
    '\u253c'  123 #  0x7B -> BOX DRAWINGS LIGHT VERTICAL AND HORIZONTAL
    '\uf12e'  124 #  0x7C -> LEFT HALF BLOCK MEDIUM SHADE (CUS)
    '\u2502'  125 #  0x7D -> BOX DRAWINGS LIGHT VERTICAL
    '\u03c0'  126 #  0x7E -> GREEK SMALL LETTER PI
    '\u25e5'  127 #  0x7F -> BLACK UPPER RIGHT TRIANGLE
    '\ufffe'  128 #  0x80 -> UNDEFINED
    '\uf104'  129 #  0x81 -> ORANGE COLOR SWITCH (CUS)
    '\ufffe'  130 #  0x82 -> UNDEFINED
    '\ufffe'  131 #  0x83 -> UNDEFINED
    '\ufffe'  132 #  0x84 -> UNDEFINED
    '\uf110'  133 #  0x85 -> FUNCTION KEY 1 (CUS)
    '\uf112'  134 #  0x86 -> FUNCTION KEY 3 (CUS)
    '\uf114'  135 #  0x87 -> FUNCTION KEY 5 (CUS)
    '\uf116'  136 #  0x88 -> FUNCTION KEY 7 (CUS)
    '\uf111'  137 #  0x89 -> FUNCTION KEY 2 (CUS)
    '\uf113'  138 #  0x8A -> FUNCTION KEY 4 (CUS)
    '\uf115'  139 #  0x8B -> FUNCTION KEY 6 (CUS)
    '\uf117'  140 #  0x8C -> FUNCTION KEY 8 (CUS)
    '\n'      141 #  0x8D -> LINE FEED
    '\x0f'    142 #  0x8E -> SHIFT IN
    '\ufffe'    #  0x8F -> UNDEFINED
    '\uf105'    #  0x90 -> BLACK COLOR SWITCH (CUS)
    '\uf11e'    #  0x91 -> CURSOR UP (CUS)
    '\uf11b'    #  0x92 -> REVERSE VIDEO OFF (CUS)
    '\x0c'      #  0x93 -> FORM FEED
    '\uf121'    #  0x94 -> INSERT (CUS)
    '\uf106'    #  0x95 -> BROWN COLOR SWITCH (CUS)
    '\uf107'    #  0x96 -> LIGHT RED COLOR SWITCH (CUS)
    '\uf108'    #  0x97 -> GRAY 1 COLOR SWITCH (CUS)
    '\uf109'    #  0x98 -> GRAY 2 COLOR SWITCH (CUS)
    '\uf10a'    #  0x99 -> LIGHT GREEN COLOR SWITCH (CUS)
    '\uf10b'    #  0x9A -> LIGHT BLUE COLOR SWITCH (CUS)
    '\uf10c'    #  0x9B -> GRAY 3 COLOR SWITCH (CUS)
    '\uf10d'    #  0x9C -> PURPLE COLOR SWITCH (CUS)
    '\uf11d'    #  0x9D -> CURSOR LEFT (CUS)
    '\uf10e'    #  0x9E -> YELLOW COLOR SWITCH (CUS)
    '\uf10f'    #  0x9F -> CYAN COLOR SWITCH (CUS)
    '\xa0'      #  0xA0 -> NO-BREAK SPACE
    '\u258c'    #  0xA1 -> LEFT HALF BLOCK
    '\u2584'    #  0xA2 -> LOWER HALF BLOCK
    '\u2594'    #  0xA3 -> UPPER ONE EIGHTH BLOCK
    '\u2581'    #  0xA4 -> LOWER ONE EIGHTH BLOCK
    '\u258f'    #  0xA5 -> LEFT ONE EIGHTH BLOCK
    '\u2592'    #  0xA6 -> MEDIUM SHADE
    '\u2595'    #  0xA7 -> RIGHT ONE EIGHTH BLOCK
    '\uf12f'    #  0xA8 -> LOWER HALF BLOCK MEDIUM SHADE (CUS)
    '\u25e4'    #  0xA9 -> BLACK UPPER LEFT TRIANGLE
    '\uf130'    #  0xAA -> RIGHT ONE QUARTER BLOCK (CUS)
    '\u251c'    #  0xAB -> BOX DRAWINGS LIGHT VERTICAL AND RIGHT
    '\u2597'    #  0xAC -> QUADRANT LOWER RIGHT
    '\u2514'    #  0xAD -> BOX DRAWINGS LIGHT UP AND RIGHT
    '\u2510'    #  0xAE -> BOX DRAWINGS LIGHT DOWN AND LEFT
    '\u2582'    #  0xAF -> LOWER ONE QUARTER BLOCK
    '\u250c'    #  0xB0 -> BOX DRAWINGS LIGHT DOWN AND RIGHT
    '\u2534'    #  0xB1 -> BOX DRAWINGS LIGHT UP AND HORIZONTAL
    '\u252c'    #  0xB2 -> BOX DRAWINGS LIGHT DOWN AND HORIZONTAL
    '\u2524'    #  0xB3 -> BOX DRAWINGS LIGHT VERTICAL AND LEFT
    '\u258e'    #  0xB4 -> LEFT ONE QUARTER BLOCK
    '\u258d'    #  0xB5 -> LEFT THREE EIGTHS BLOCK
    '\uf131'    #  0xB6 -> RIGHT THREE EIGHTHS BLOCK (CUS)
    '\uf132'    #  0xB7 -> UPPER ONE QUARTER BLOCK (CUS)
    '\uf133'    #  0xB8 -> UPPER THREE EIGHTS BLOCK (CUS)
    '\u2583'    #  0xB9 -> LOWER THREE EIGHTHS BLOCK
    '\uf12d'    #  0xBA -> ONE EIGHTH BLOCK UP AND LEFT (CUS)
    '\u2596'    #  0xBB -> QUADRANT LOWER LEFT
    '\u259d'    #  0xBC -> QUADRANT UPPER RIGHT
    '\u2518'    #  0xBD -> BOX DRAWINGS LIGHT UP AND LEFT
    '\u2598'    #  0xBE -> QUADRANT UPPER LEFT
    '\u259a'    #  0xBF -> QUADRANT UPPER LEFT AND LOWER RIGHT
    '\u2500'    #  0xC0 -> BOX DRAWINGS LIGHT HORIZONTAL
    '\u2660'    #  0xC1 -> BLACK SPADE SUIT
    '\u2502'    #  0xC2 -> BOX DRAWINGS LIGHT VERTICAL
    '\u2500'    #  0xC3 -> BOX DRAWINGS LIGHT HORIZONTAL
    '\uf122'    #  0xC4 -> BOX DRAWINGS LIGHT HORIZONTAL ONE QUARTER UP (CUS)
    '\uf123'    #  0xC5 -> BOX DRAWINGS LIGHT HORIZONTAL TWO QUARTERS UP (CUS)
    '\uf124'    #  0xC6 -> BOX DRAWINGS LIGHT HORIZONTAL ONE QUARTER DOWN (CUS)
    '\uf126'    #  0xC7 -> BOX DRAWINGS LIGHT VERTICAL ONE QUARTER LEFT (CUS)
    '\uf128'    #  0xC8 -> BOX DRAWINGS LIGHT VERTICAL ONE QUARTER RIGHT (CUS)
    '\u256e'    #  0xC9 -> BOX DRAWINGS LIGHT ARC DOWN AND LEFT
    '\u2570'    #  0xCA -> BOX DRAWINGS LIGHT ARC UP AND RIGHT
    '\u256f'    #  0xCB -> BOX DRAWINGS LIGHT ARC UP AND LEFT
    '\uf12a'    #  0xCC -> ONE EIGHTH BLOCK UP AND RIGHT (CUS)
    '\u2572'    #  0xCD -> BOX DRAWINGS LIGHT DIAGONAL UPPER LEFT TO LOWER RIGHT
    '\u2571'    #  0xCE -> BOX DRAWINGS LIGHT DIAGONAL UPPER RIGHT TO LOWER LEFT
    '\uf12b'    #  0xCF -> ONE EIGHTH BLOCK DOWN AND RIGHT (CUS)
    '\uf12c'    #  0xD0 -> ONE EIGHTH BLOCK DOWN AND LEFT (CUS)
    '\u25cf'    #  0xD1 -> BLACK CIRCLE
    '\uf125'    #  0xD2 -> BOX DRAWINGS LIGHT HORIZONTAL TWO QUARTERS DOWN (CUS)
    '\u2665'    #  0xD3 -> BLACK HEART SUIT
    '\uf127'    #  0xD4 -> BOX DRAWINGS LIGHT VERTICAL TWO QUARTERS LEFT (CUS)
    '\u256d'    #  0xD5 -> BOX DRAWINGS LIGHT ARC DOWN AND LEFT
    '\u2573'    #  0xD6 -> BOX DRAWINGS LIGHT DIAGONAL CROSS
    '\u25cb'    #  0xD7 -> WHITE CIRCLE
    '\u2663'    #  0xD8 -> BLACK CLUB SUIT
    '\uf129'    #  0xD9 -> BOX DRAWINGS LIGHT VERTICAL TWO QUARTERS RIGHT (CUS)
    '\u2666'    #  0xDA -> BLACK DIAMOND SUIT
    '\u253c'    #  0xDB -> BOX DRAWINGS LIGHT VERTICAL AND HORIZONTAL
    '\uf12e'    #  0xDC -> LEFT HALF BLOCK MEDIUM SHADE (CUS)
    '\u2502'    #  0xDD -> BOX DRAWINGS LIGHT VERTICAL
    '\u03c0'    #  0xDE -> GREEK SMALL LETTER PI
    '\u25e5'    #  0xDF -> BLACK UPPER RIGHT TRIANGLE
    '\xa0'      #  0xE0 -> NO-BREAK SPACE
    '\u258c'    #  0xE1 -> LEFT HALF BLOCK
    '\u2584'    #  0xE2 -> LOWER HALF BLOCK
    '\u2594'    #  0xE3 -> UPPER ONE EIGHTH BLOCK
    '\u2581'    #  0xE4 -> LOWER ONE EIGHTH BLOCK
    '\u258f'    #  0xE5 -> LEFT ONE EIGHTH BLOCK
    '\u2592'    #  0xE6 -> MEDIUM SHADE
    '\u2595'    #  0xE7 -> RIGHT ONE EIGHTH BLOCK
    '\uf12f'    #  0xE8 -> LOWER HALF BLOCK MEDIUM SHADE (CUS)
    '\u25e4'    #  0xE9 -> BLACK UPPER LEFT TRIANGLE
    '\uf130'    #  0xEA -> RIGHT ONE QUARTER BLOCK (CUS)
    '\u251c'    #  0xEB -> BOX DRAWINGS LIGHT VERTICAL AND RIGHT
    '\u2597'    #  0xEC -> QUADRANT LOWER RIGHT
    '\u2514'    #  0xED -> BOX DRAWINGS LIGHT UP AND RIGHT
    '\u2510'    #  0xEE -> BOX DRAWINGS LIGHT DOWN AND LEFT
    '\u2582'    #  0xEF -> LOWER ONE QUARTER BLOCK
    '\u250c'    #  0xF0 -> BOX DRAWINGS LIGHT DOWN AND RIGHT
    '\u2534'    #  0xF1 -> BOX DRAWINGS LIGHT UP AND HORIZONTAL
    '\u252c'    #  0xF2 -> BOX DRAWINGS LIGHT DOWN AND HORIZONTAL
    '\u2524'    #  0xF3 -> BOX DRAWINGS LIGHT VERTICAL AND LEFT
    '\u258e'    #  0xF4 -> LEFT ONE QUARTER BLOCK
    '\u258d'    #  0xF5 -> LEFT THREE EIGTHS BLOCK
    '\uf131'    #  0xF6 -> RIGHT THREE EIGHTHS BLOCK (CUS)
    '\uf132'    #  0xF7 -> UPPER ONE QUARTER BLOCK (CUS)
    '\uf133'    #  0xF8 -> UPPER THREE EIGHTS BLOCK (CUS)
    '\u2583'    #  0xF9 -> LOWER THREE EIGHTHS BLOCK
    '\uf12d'    #  0xFA -> ONE EIGHTH BLOCK UP AND LEFT (CUS)
    '\u2596'    #  0xFB -> QUADRANT LOWER LEFT
    '\u259d'    #  0xFC -> QUADRANT UPPER RIGHT
    '\u2518'    #  0xFD -> BOX DRAWINGS LIGHT UP AND LEFT
    '\u2598'    #  0xFE -> QUADRANT UPPER LEFT
    '\u03c0'    #  0xFF -> GREEK SMALL LETTER PI

"""