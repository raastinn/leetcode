class Solution:
    def isPalindrome(self, x: int) -> bool:
        y = str(x)
        length = len(y)
        reverse = []
        given = []
        for i in range(length):
            given.append(y[i])
            reverse.append(y[length-1-i])
        if given == reverse:
            return True
        else:
            return False
