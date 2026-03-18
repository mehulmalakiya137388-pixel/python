class Solution:
    def convert(self, s: str, numRows: int) -> str:
        zigzag = list(range(0, numRows)) + list(range(numRows - 2, 0, -1))
        res = [""] * numRows

        for i in range(len(s)):
            res[zigzag[i % len(zigzag)]] += s[i] 

        return "".join(res)