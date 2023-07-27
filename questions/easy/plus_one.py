

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        b=int("".join(str(c) for c in digits))+1
        return [int(x) for x in str(b)]