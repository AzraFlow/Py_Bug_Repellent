from pybugrepellent.pybug import charlist_to_code_list,  \
                                 int_list_to_hilo_bytes, \
                                 hex_to_repellent_code,  \
                                 repellent_code_to_hex


def test_ctcl_short_string():
    '''
    Unit test to check the charlist_to_code_list() function
    for proper conversion of a line of code to a list of
    corresponding c64 petscii codes as integers.  Focus on
    short lines of code.
    '''
    short_list = "A"
    short_list_char_list = charlist_to_code_list(short_list)
    assert short_list_char_list == [65]
    short_list = "AB"
    short_list_char_list = charlist_to_code_list(short_list)
    assert short_list_char_list == [65, 66]


def test_ctcl_alphanumonly():
    '''
    Unit test to check the charlist_to_code_list() function
    for proper conversion of a line of code to a list of
    corresponding c64 petscii codes as integers.  Focus on
    lines of code with all alpha numeric characters.
    '''
    alpha_num = " !\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[]^"
    alpha_num_char_list = charlist_to_code_list(alpha_num)
    assert alpha_num_char_list == [32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42,
                                   43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53,
                                   54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64,
                                   65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75,
                                   76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86,
                                   87, 88, 89, 90, 91, 93, 94]


def test_ctcl_ahoy_special_char_inline():
    '''
    Unit test to check the charlist_to_code_list() function
    for proper conversion of a line of code to a list of
    corresponding c64 petscii codes as integers.  Focus on 
    detection and handling of special characters represented
    within braces embedded inline with other characters.
    '''
    inline_spec_char = "AB{WH}CD"
    inline_spec_char_list = charlist_to_code_list(inline_spec_char)
    assert inline_spec_char_list == [65, 66, 5, 67, 68]


def test_ctcl_ahoy_special_chars():
    '''
    Unit test to check the charlist_to_code_list() function
    for proper conversion of a line of code to a list of
    corresponding c64 petscii codes as integers.  Focus on
    check for detection and accuracy of all Ahoy special
    characters represented within braces.
    '''
    all_spec_char = "{WH}{CD}{RV}{HM}{RD}{CR}{GN}{BL}{OR}{F1}{F2}{F3}{F4}{F5}{F6}{F7}{F8}{BK}{CU}{RO}{SC}{IN}{BR}{LR}{G1}{G2}{LG}{LB}{G3}{PU}{CL}{YL}{CY}{SS}"
    all_spec_char_list = charlist_to_code_list(all_spec_char)
    assert all_spec_char_list == [5, 17, 18, 19, 28, 29, 30, 31, 129, 133, 134,
                                  135, 136, 137, 138, 139, 140, 144, 145, 146,
                                  147, 148, 149, 150, 151, 152, 153, 154, 155,
                                  156, 157, 158, 159, 160]


"""
def test_ctcl_detect_leading_closing_brace():
    '''
    Unit test to check the charlist_to_code_list() function
    for proper conversion of a line of code to a list of
    corresponding c64 petscii codes as integers.  Focus on
    check for detection and error reporting of leading
    closing brace character "}" - a condition that should
    never happen in properly typed in code.
    '''
    leading_close_brace = "AB}{WH}"
    code_list_close_brace = charlist_to_code_list(leading_close_brace)
    assert code_list_close_brace == "Brace character error."
"""

def test_ilthbl_return__high_low_bytes():
    '''
    Unit test to check int_list_to_hilo_bytes() function
    to insure it returns high and low bytes based on simple
    addition of integers in list passed in.
    '''
    int_list = [1, 2, 3, 4, 5]
    hilo_bytes = int_list_to_hilo_bytes(int_list)
    assert hilo_bytes == (0, 15)

    int_list2 = [256, 1, 2, 3, 4, 5]
    hilo_bytes2 = int_list_to_hilo_bytes(int_list2)
    assert hilo_bytes2 == (1, 15)


def test_hex_to_repellent_code():
    '''
    Unit test to check that function hex_to_repellent_code()
    returns the passed in hex code as an alpha code combination.
    '''
    hex_value = "0x1d"
    alpha_code = hex_to_repellent_code(hex_value)
    assert alpha_code == "BN"

    hex_value = "0x01"
    alpha_code = hex_to_repellent_code(hex_value)
    assert alpha_code == "AB"


def test_repellent_code_to_hex():
    '''
    Unit test to check that function repellent_code_to_hex()
    returns the passed in alpha code combination as a hex value
    '''
    alpha_code = "BN"
    hex_value = repellent_code_to_hex(alpha_code)
    assert hex_value == "0x1d"

'''
def test_prog_flow():
    codeline = "GGGG"
    hilo_bytes = int_list_to_hilo_bytes(charlist_to_code_list(codeline))
    xor_hilo = hilo_bytes[0] ^ hilo_bytes[1]
    hex_xor_hilo = hex(xor_hilo)
    alpha_code = hex_to_repellent_code(hex_xor_hilo)
    assert alpha_code == "CB"
'''
