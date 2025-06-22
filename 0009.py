def isPalindrome(x):
    """
    :type x: int
    :rtype: bool
    """

    if str(x)[::-1] == str(x):
        return True
    else:
        return False
    

assert isPalindrome(121) == True, "Wrong"
assert isPalindrome(-121) == False, "Wrong"
assert isPalindrome(10) == False, "Wrong"