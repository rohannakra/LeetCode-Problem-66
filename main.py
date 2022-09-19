# https://leetcode.com/problems/plus-one/

def plus_one(digits):
    str_num = "".join([str(digit) for digit in digits])
    index = -1
    while True:
        if abs(index) > len(digits):
            return digits
        digits[index] += 1
        if digits[index] == 10:
            digits[index] = 0
            if abs(index) == len(digits):
                digits.insert(0, 1)
                return digits
            index -= 1
        else:
            return digits

print(plus_one([1,2,3]))
print(plus_one([9, 9]))
print(plus_one([2, 2]))
print(plus_one([9]))
print(plus_one([9, 9, 9]))

# ---- LeetCode Accepted Solution ----

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        str_num = "".join([str(digit) for digit in digits])
        index = -1
        while True:
            if abs(index) > len(digits):
                return digits
            digits[index] += 1
            if digits[index] == 10:
                digits[index] = 0
                if abs(index) == len(digits):
                    digits.insert(0, 1)
                    return digits
                index -= 1
            else:
                return digits

# NOTE: This solution is faster than 99% of python 3 submissions and uses less memory than 96% of submissions.
