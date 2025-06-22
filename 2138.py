def divideString(s, k, fill):
    """
    :type s: str
    :type k: int
    :type fill: str
    :rtype: List[str]
    """
    
    data = []
    indx = 0
    while indx < len(s):
        data.append(s[indx:indx+k])
        indx += k
    
    diff = k - len(data[-1])
    data[-1] += diff * fill

    return data

# Test Cases
assert divideString(s="abcdefghi", k=3, fill="x") == ["abc","def","ghi"], "Wrong"
assert divideString(s="abcdefghij", k=3, fill="x") == ["abc","def","ghi","jxx"], "Wrong"
assert divideString(s="ctoyjrwtngqwt", k=8, fill="n") == ["ctoyjrwt","ngqwtnnn"], "Wrong"