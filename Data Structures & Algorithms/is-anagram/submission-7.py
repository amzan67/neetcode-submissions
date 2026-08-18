from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_ = Counter(s)
        t_ = Counter(t)
        if len(s) == len(t):
            if set(s) == set(t):
              if s_ == t_:
                return True
              else:
                return False
            else:
                return False
      
        else:
            return False