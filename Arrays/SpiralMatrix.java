package Arrays;
import java.util.*;

public class SpiralMatrix {
    public static void main(String[] args) {
        int[][] matrix = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};
        System.out.println(spiralOrder(matrix));
    }

    public static List<Integer> spiralOrder(int[][] matrix){
        List<Integer> res = new ArrayList<>();
        if (matrix == null || matrix.length == 0){
            return res;
        }
        int rows = matrix.length, cols = matrix[0].length;
        int left = 0, right = cols-1, top = 0, bottom = rows-1;
        while(left <= right && top <= bottom){
            for(int i=left; i<=right; i++){
                res.add(matrix[top][i]);
            }
            top++;
            for(int i=top; i<=bottom; i++){
                res.add(matrix[i][right]);
            }
            right--;
            if(top <= bottom){
                for(int i=right; i>=left;i--){
                    res.add(matrix[bottom][i]);
                }
                bottom--;
            }
            if(left <= right){
                for(int i=bottom; i>=top; i--){
                    res.add(matrix[i][left]);
                }
            }
        }

        return res;
    }
}
