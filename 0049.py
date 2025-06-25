from collections import defaultdict
# Arrays & Hashing
def groupAnagrams(strs):
    """
    :type strs: List[str]
    :rtype: List[List[str]]
    """
    # n log n
    res = defaultdict(list)
    for s in strs:
        sorted_ = ''.join(sorted(s))
        res[sorted_].append(s)
    
    return list(res.values())


assert groupAnagrams(["eat","tea","tan","ate","nat","bat"]) == [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']], "Wrong"