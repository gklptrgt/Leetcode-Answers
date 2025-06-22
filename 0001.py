
def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    hashmap = {} # val indx
    for i, num in enumerate(nums):
        diff = target - num
        if diff in hashmap:
            return [hashmap[diff], i]
        
        hashmap[num] = i

        
# Test Cases
assert twoSum([2,7,11,15],9) == [0,1], "Wrong"
assert twoSum([3,2,4],6) == [1,2], "Wrong"
assert twoSum([3,3],6) == [0,1], "Wrong"
assert twoSum([3,2,3],6) == [0,2], "Wrong"
