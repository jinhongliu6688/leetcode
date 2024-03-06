class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        length = len(matrix[0])
        width = len(matrix) - 1
        total = len(matrix) * len(matrix[0]) #number of elements in the matrix
        result = []
        count = 0 #number of elements in the result

        i = 0
        j = 0

        back = False
        
        while count < total:
            if not back:
                for x in range(length): # from left to right
                    result.append(matrix[i][j])
                    count += 1
                    j += 1
                j -= 1
                i += 1
                length -= 1
                for x in range(width): # from up to down
                    result.append(matrix[i][j])
                    count += 1
                    i += 1
                i -= 1
                j -= 1
                back = True
                width -= 1
            else:
                for x in range(length): # from right to left
                    result.append(matrix[i][j])
                    count += 1
                    j -= 1
                j += 1
                i -= 1
                length -= 1
                for x in range(width): # from down to up
                    result.append(matrix[i][j])
                    count += 1
                    i -= 1
                i += 1
                j += 1
                back = False
                width -= 1

        return result
