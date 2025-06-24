def containsDuplicate(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    return len(nums)!=len(set(nums))

assert containsDuplicate([1,2,3,1]) == True, "Wrong"
assert containsDuplicate([1,2,3,4]) == False, "Wrong"
assert containsDuplicate([1,1,1,3,3,4,3,2,4,2]) == True, "Wrong"

