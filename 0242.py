def isAnagram(s:str, t:str):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    return sorted(t)==sorted(s)

# An anagram is a word or phrase formed by rearranging 
# the letters of a different word or phrase, using all 
# the original letters exactly once.

assert isAnagram("anagram","nagaram") == True, "Wrong."
assert isAnagram("rat","car") == False, "Wrong."
assert isAnagram("a","ab") == False, "wrong"