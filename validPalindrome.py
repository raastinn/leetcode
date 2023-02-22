class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        reverse = []
        given = []
        for i in s:
            if i.isalpha() or i.isnumeric():
                given.append(i)
            else:
                s.strip(i)
        i = len(given) - 1
        while i != -1:
            reverse.append(given[i])
            i = i - 1
        if reverse == given:
            return True
        else:
            return False
