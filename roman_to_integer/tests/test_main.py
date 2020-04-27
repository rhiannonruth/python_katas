from roman_to_integer.main import roman_to_integer


def test_i_to_1():
    assert roman_to_integer("I") == 1


def test_ii_to_2():
    assert roman_to_integer("II") == 2


def test_iii_to_3():
    assert roman_to_integer("III") == 3


def test_iv_to_4():
    assert roman_to_integer("IV") == 4


def test_v_to_5():
    assert roman_to_integer("V") == 5


def test_vi_to_6():
    assert roman_to_integer("VI") == 6


def test_vii_to_7():
    assert roman_to_integer("VII") == 7


def test_viii_to_8():
    assert roman_to_integer("VIII") == 8


def test_ix_to_9():
    assert roman_to_integer("IX") == 9


def test_x_to_10():
    assert roman_to_integer("X") == 10


def test_xi_to_11():
    assert roman_to_integer("XI") == 11


def test_xii_to_12():
    assert roman_to_integer("XII") == 12


def test_xiii_to_13():
    assert roman_to_integer("XIII") == 13


def test_xiv_to_14():
    assert roman_to_integer("XIV") == 14


def test_xv_to_15():
    assert roman_to_integer("XV") == 15


def test_xvi_to_16():
    assert roman_to_integer("XVI") == 16


def test_xvii_to_17():
    assert roman_to_integer("XVII") == 17


def test_xviii_to_18():
    assert roman_to_integer("XVIII") == 18


def test_xix_to_19():
    assert roman_to_integer("XIX") == 19


def test_xx_to_20():
    assert roman_to_integer("XX") == 20


def test_xxx_to_30():
    assert roman_to_integer("XXX") == 30


def test_xlv_to_45():
    assert roman_to_integer("XLV") == 45


def test_lviii_to_58():
    assert roman_to_integer("LVIII") == 58


def test_xc_to_90():
    assert roman_to_integer("XC") == 90


def test_c_to_100():
    assert roman_to_integer("C") == 100


def test_mcm_to_1900():
    assert roman_to_integer("MCM") == 1900


def test_mcmxciv_to_1994():
    assert roman_to_integer("MCMXCIV") == 1994
