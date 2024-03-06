class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        columns = set()
        length = len(matrix[0])

        for array in matrix:
            if 0 in array:
                for i in range(length):
                    if array[i] == 0:
                        columns.add(i)
                    else:
                        array[i] = 0
        
        for col in columns:
            for array in matrix:
                array[col] = 0
