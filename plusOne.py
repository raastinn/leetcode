class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[len(digits)-1] == 9 and digits[len(digits)-2] == 9:
            i = len(digits)-1
            while i != 0:
                print(digits[i])
                if digits[i] != 9:
                    digits[i] = digits[i] + 1
                    print(digits[i])
                    break
                digits[i] = 0
                i = i - 1
            if i == 0 and digits[i] == 9:
                digits[0] = 0
                digits.insert(0, 1)
            elif i == 0 and digits[i] != 9:
                digits[0] = digits[0] + 1
        elif digits[len(digits)-1] == 9:
            digits[len(digits)-2] = digits[len(digits)-2] + 1
            digits[len(digits)-1] = 0
        else:
            digits[len(digits)-1] = digits[len(digits)-1] + 1
        return digits
