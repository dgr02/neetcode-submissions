class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        s_dict = dict()
        t_dict = dict()

        for x in s:

            if x not in s_dict:
                s_dict[x] = 1

            else:
                s_dict[x] += 1

        for x in t:

            if x not in t_dict:
                t_dict[x] = 1

            else:
                t_dict[x] += 1

        return s_dict == t_dict
