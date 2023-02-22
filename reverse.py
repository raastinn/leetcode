class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            given = -x
            given = str(given)
        else:
            given = str(x)
        reverse = ''
        for i in range(len(given)):
            reverse += given[len(given)-1-i]
        reverse = int(reverse)
        if x < 0:
            reverse = reverse * -1
        if reverse > 2**31-1 or reverse < -2**31:
            return 0
        return reverse
