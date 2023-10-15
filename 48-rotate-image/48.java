class Solution {
    public void rotate(int[][] matrix) {
        int length = matrix.length - 1;
        for (int i  = 0; i < matrix.length / 2; i++) {
            int[] temp = matrix[i];
            matrix[i] = matrix[length];
            matrix[length] = temp;
            length -= 1;
        }

        for (int i = 0; i < matrix.length; i++) {
            for (int j = i + 1; j < matrix.length; j++) {
                int temp = matrix[i][j];
                matrix[i][j] = matrix[j][i];
                matrix[j][i] = temp;
            }
        }
    }
}
