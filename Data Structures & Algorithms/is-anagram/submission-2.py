class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False

        s_dict = {}
        t_dict = {}

        for x in range(len(s)):

            s_dict[s[x]] = s_dict.get(s[x], 0) + 1
            t_dict[t[x]] = t_dict.get(t[x], 0) + 1
        

        return s_dict == t_dict
