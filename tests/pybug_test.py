from pybugrepellent.pybug import line_to_charlist


def test_ltcl_single_char():
    line = "a"                      # Arrange
    list = line_to_charlist(line)  # Act
    assert list == ['a']            # Assert

def test_ltcl_multi_char():
    line_2 = "ab"                       # Arrange
    list_2 = line_to_charlist(line_2)  # Act
    assert list_2 == ['a', 'b']         # Assert
    line_5 = "abcde"
    list_5 = line_to_charlist(line_5)
    assert list_5 == ['a', 'b', 'c', 'd', 'e']

def test_ctcl_alphanumonly():
    alpha_num = " !\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[]^"
    alpha_num_char_list = charlist_to_code_list(alph_num)
    assert alpha_num == [32, 33, 34, 35, 36, 37, 388, 39, 40, 41, 42, 43]