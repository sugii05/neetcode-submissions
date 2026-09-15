class Solution {
public:

    void swap_numbers(vector<int>& a,vector<int>& b, int i, int j ){
        int temp;

        temp = b[j];
        b[j] = a[i];
        a[i] = temp;    
    }

    void rotate(vector<vector<int>>& matrix) {
        int n = matrix.size();

        // eq: y = - x + 2 
        // or row = 2 - col 

        // lets say we are at x, y
        //lets hold col fixed, then for the line we are at point (2-y, y)
        // new point: (2-y ,(2-x))

        for (int row = 0; row < n; row ++){
            for (int col = 0; col < (n-1) - row; col ++) {
                swap_numbers(matrix[row],matrix[(n-1)-col], col, (n-1) - row);

            }

        }
        int t = n/2;  

        for (int col = 0; col < n; col ++) {
            for (int row = 0; row < t; row ++) {
                swap_numbers(matrix[row], matrix[(n-1)-row], col, col);
            }

        }



    }
};
