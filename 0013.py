# UNCOMPLETE
def romanToInt(s):
    """
    :type s: str
    :rtype: int
    """
    roman_data = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
    total = 0
    for val in s:
        total += roman_data[val] 
        print(total)
    return total



# assert romanToInt("III") == 3, "Wrong"
# assert romanToInt("LVIII") == 58, "Wrong"
assert romanToInt("MCMXCIV") == 1994, "Wrong"
