repellent_data = [
32, 161, 192, 165, 43,133, 251, 165, 44, 133,
252, 160, 0, 132, 254, 32, 37, 193, 234, 177,
251, 208, 3, 76, 138, 192, 230, 251, 208, 2,
230, 252, 76, 43, 192, 76, 73, 78, 69, 32,
35, 32, 0, 169, 35, 160, 192, 32, 30, 171,
160, 0, 177, 251, 170, 230, 251, 208, 2, 230,
252, 177, 251, 32, 205, 189, 169, 58, 32, 210,
255, 169, 0, 133, 253, 230, 254, 32, 37, 193,
234, 165, 253, 160, 0, 76, 13, 193, 133, 253,
177, 251, 208, 237, 165, 253, 41, 240, 74, 74,
74, 74, 24, 105, 65, 32, 210, 255, 165, 253,
41, 15, 24, 105, 65, 32, 210, 255, 169, 13,
32, 220, 192, 230, 63,208, 2, 230, 64, 230,
251, 208, 2, 230, 252, 76, 11, 192, 169, 153,
160, 192, 32, 30, 171, 166, 63, 165, 64, 76,
231, 192, 96, 76, 73, 78, 69, 83, 58, 32,
0, 169, 247, 160, 192, 32, 30, 171, 169, 3,
133, 254, 32, 228, 255, 201, 83, 240, 6, 201,
80, 208, 245, 230, 254, 32, 210, 255, 169, 4,
166, 254, 160, 255, 32, 186, 255, 169, 0, 133,
63, 133, 64, 133, 2, 32, 189, 255, 32, 192, 
255, 166, 254, 32, 201, 255, 76, 73, 193, 96,
32, 210, 255, 173, 141, 2, 41, 1, 208, 249,
96, 32, 205, 189, 169, 13, 32, 210, 255, 32,
204, 255, 169, 4, 76, 195, 255, 147, 83, 67,
82, 69, 69, 78, 32, 79, 82, 32, 80, 82,
73, 78, 84, 69, 82, 32, 63, 32, 0, 76,
44, 193, 234, 177, 251, 201, 32, 240, 6, 138,
113, 251, 69, 254, 170, 138, 76, 88, 192, 0,
0, 0, 0, 230, 251, 208, 2, 230, 252, 96,
170, 177, 251, 201, 34, 208, 6, 165, 2, 73,
255, 133, 2, 165, 2, 208, 218, 177, 251, 201,
32, 208, 212, 198, 254, 76, 29, 193, 0, 169,
13, 76, 210, 255, 0, 0, 0
]

asm_dict = {
            "0": "BRK",
            "1": "ORA(I,X)", 
            "5": "ORA Z",
            "6": "ASL Z",
            "8": "PHP",
            "9": "ORA #",
            "10": "ASL A",
            "13": "ORA",
            "14": "ASL",
            "16": "BPL",
            "17": "ORA(I),Y",	 	 
            "21": "ORA Z,X",
            "22": "ASL Z,X",
            "24": "CLC",
            "25": "ORA Y",
            "29": "ORA X",
            "30": "ASL X",
            "32": "JSR",
            "33": "AND(I,X)", 
            "36": "BIT Z",
            "37": "AND Z",
            "38": "ROL Z",
            "40": "PLP",
            "41": "AND #",
            "42": "ROL A",
            "44": "BIT",
            "45": "AND",
            "46": "ROL",
            "48": "BMI",
            "49": "AND(I),Y",
            "53": "AND Z,X",
            "54": "ROL Z,X",
            "56": "SEC",
            "57": "AND Y", 
            "61": "AND X",
            "62": "ROL X",
            "64": "RTI",
            "65": "EOR(I,X)",
            "69": "EOR Z",
            "70": "LSR Z",
            "72": "PHA",
            "73": "EOR #",
            "74": "LSR A",
            "76": "JMP",
            "77": "EOR",
            "78": "LSR",
            "80": "BVC",
            "81": "EOR(I),Y",
            "85": "EOR Z,X",
            "86": "LSR Z,X",
            "88": "CLI",
            "89": "EOR Y",
            "93": "EOR X",
            "94": "LSR X",
            "96": "RTS",
            "97": "ADC(I,X)",
            "101": "ADC Z",
            "102": "ROR Z",
            "104": "PLA",
            "105": "ADC #",
            "106": "ROR A",
            "108": "JMP(I)",
            "109": "ADC",
            "110": "ROR",
            "112": "BVS",
            "113": "ADC(I),Y",
            "117": "ADC Z,X",
            "118": "ROR Z,X",
            "120": "SEI",
            "121": "ADC Y",
            "125": "ADC X",
            "126": "ROR X",
            "129": "STA(I,X)", 
            "132": "STY Z",
            "133": "STA Z",
            "134": "STX Z",
            "136": "DEY",	 
            "138": "TXA",
            "140": "STY",
            "141": "STA",
            "142": "STX",
            "144": "BCC",
            "145": "STA(I),Y",
            "148": "STY Z,X",
            "149": "STA Z,X",
            "150": "STX Z,X",
            "152": "TYA",
            "153": "STA Y",
            "154": "TXS",
            "157": "STA X",
            "160": "LDY #",
            "161": "LDA(I,X)",
            "162": "LDX #",
            "164": "LDY Z",
            "165": "LDA Z",
            "168": "TAY",
            "169": "LDA #",
            "170": "TAX",
            "172": "LDY",
            "173": "LDA",
            "174": "LDX",
            "176": "BCS",
            "177": "LDA(I),Y",
            "180": "LDY Z,X",
            "181": "LDA Z,X",
            "182": "LDX Z,X",
            "184": "CLV",
            "185": "LDA Y",
            "186": "TSX",
            "188": "LDY X",
            "189": "LDA X",
            "190": "LDX Y",
            "192": "CPY #",
            "193": "CMP(I),X",
            "196": "CPY Z",
            "197": "CMP Z",
            "198": "DEC Z ",
            "200": "INY",
            "201": "CMP #",
            "202": "DEX",
            "204": "CPY",
            "205": "CMP",
            "206": "DEC",
            "208": "BNE",
            "209": "CMP(I),Y",	 
            "213": "CMP Z,X",
            "214": "DEC Z,X",
            "216": "CLD",
            "217": "CMP Y",
            "221": "CMP X",
            "222": "DEC X",
            "224": "CPX #",
            "225": "SBC(I),X",
            "228": "CPX Z",
            "229": "SBC Z",
            "230": "INC Z",
            "232": "INX",
            "233": "SBC #",
            "234": "NOP",
            "236": "CPX",
            "237": "SBC",
            "238": "INC",
            "240": "BEQ",
            "241": "SBC(I),Y",
            "245": "SBC Z,X",
            "246": "INC Z,X",
            "248": "SED",
            "249": "SBC Y",
            "253": "SBC X",
            "254": "INC X"
            }

for data in repellent_data:
    if str(data) in asm_dict.keys():
        print(asm_dict[str(data)], str(data))
    else:
        print(str(data), str(data))