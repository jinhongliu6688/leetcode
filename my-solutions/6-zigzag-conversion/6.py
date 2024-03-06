class Solution:
    def convert(self, s: str, numRows: int) -> str:
        result = ["" for x in range(numRows)]
        down = True
        row = 0
        for letter in s:
            if down:
                result[row] += letter
                row += 1
                if row > numRows - 1:
                    down = False
                    row -= 2
            elif not down:
                result[row] += letter
                row -= 1
                if row < 0:
                    down = True
                    row += 2
        
        answer = ""
        for word in result:
            answer += word

        return answer
