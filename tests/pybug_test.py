from pybugrepellent.pybug import line_to_charlist
from pybugrepellent.pybug import charlist_to_code_list


def test_ltcl_single_char():
    line = "a"                      # Arrange
    list = line_to_charlist(line)   # Act
    assert list == ['a']            # Assert

def test_ltcl_multi_char():
    line_2 = "ab"                       # Arrange
    list_2 = line_to_charlist(line_2)   # Act
    assert list_2 == ['a', 'b']         # Assert
    line_5 = "abcde"
    list_5 = line_to_charlist(line_5)
    assert list_5 == ['a', 'b', 'c', 'd', 'e']

def test_ctcl_alphanumonly():
    alpha_num = " !\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[]^"
    alpha_num_char_list = charlist_to_code_list(alpha_num)
    assert alpha_num_char_list == [32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42,
                                   43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53,
                                   54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64,
                                   65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75,
                                   76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86,
                                   87, 88, 89, 90, 91, 93, 94]

def test_ctcl_ahoy_special_char():
    inline_spec_char = "AB{WH}CD"
    inline_spec_char_list = charlist_to_code_list(inline_spec_char)
    assert inline_spec_char_list == [65, 66, 5, 67, 68]
    all_spec_char = "{WH}{CD}{RV}{HM}{RD}{CR}{GN}{BL}{OR}{F1}{F2}{F3}{F4}{F5}{F6}{F7}{F8}{BK}{CU}{RO}{SC}{IN}{BR}{LR}{G1}{G2}{LG}{LB}{G3}{PU}{CL}{YL}{CY}{SS}"
    all_spec_char_list = charlist_to_code_list(all_spec_char)
    assert all_spec_char_list == [5, 17, 18, 19, 28, 29, 30, 31, 129, 133, 134,
                                  135, 136, 137, 138, 139, 140, 144, 145, 146,
                                  147, 148, 149, 150, 151, 152, 153, 154, 155,
                                  156, 157, 158, 159, 160]
