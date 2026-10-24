from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list)

        for s in strs:
        # Sort the character array of the string and use it as a tuple key
          key = "".join(sorted(s))
          anagram_map[key].append(s)

    # Return the grouped lists
        return list(anagram_map.values())