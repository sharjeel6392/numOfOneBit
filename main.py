class Solution:
    def hammingWeight(self, n: int) -> int:
        if n >= 0:
            unsigned_n = n
        else:
            unsigned_n = n + (2**32)
        
        bit_Un = bin(unsigned_n).replace("0b", "")
        count = 0
        for element in bit_Un:
            if element == "1":
                count += 1
        
        return count
