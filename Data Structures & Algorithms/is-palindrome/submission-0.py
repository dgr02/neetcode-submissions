class Solution:
    def isPalindrome(self, s: str) -> bool:
        result = "".join(i for i in s if i.isalnum()).lower()

        for i in range(len(result) // 2):

            if result[i] != result[-1 - i]:
                return False

        return True
        