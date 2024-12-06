class Solution:
    def lcmAndGcd(self, a : int, b : int) -> List[int]:
        product = a*b
        while a>0 and b>0:
            if a > b:
                a = a % b
            else:
                b = b % a
        if a == 0:
            gcd = b
        else:
            gcd = a
        return [int(product/gcd), gcd]
