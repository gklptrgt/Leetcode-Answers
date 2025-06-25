# Arrays & Hashing

def topKFrequent(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: List[int]
    """

    hashmap = {} # 'a':2
    for n in nums:
        if n in hashmap:
            last_val = hashmap[n] # get last val from hash
            hashmap[n] = last_val + 1 # adding new found
        else:
            hashmap[n] = 1
    

    res = []
    for _ in range(k):
        max_val = max(hashmap.values())
        key = [key for key, val in hashmap.items() if val == max_val][0]
        hashmap.pop(key)
        res.append(key)

    return res


assert topKFrequent([1,1,1,2,2,3], 2) == [1,2], "Wrong"
assert topKFrequent([1], 1) == [1], "Wrong"
assert topKFrequent([4,1,-1,2,-1,2,3], 2) == [-1, 2], "Wrong"