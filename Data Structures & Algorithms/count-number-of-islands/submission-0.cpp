class Solution {
public:

    vector<int> dr = {0, 0, 1, -1};
    vector<int> dc = {1, -1, 0, 0}; 

    void bfs(const vector<vector<char>>& grid, vector<vector<bool>>& visited, int x_pos, int y_pos){
        queue<pair<int, int>> q;
        int r = grid.size();
        int c = grid[0].size();

        visited[y_pos][x_pos] = true;
        q.push({y_pos, x_pos});

        while(!q.empty()) {
            pair<int, int> curr = q.front();
            q.pop();

            for (int i = 0; i < 4; ++i) {
                int new_x_pos = curr.second + dc[i]; 
                int new_y_pos = curr.first + dr[i];

                if (new_x_pos < 0 || new_x_pos >= c || new_y_pos < 0 || new_y_pos >= r) continue;
                if (grid[new_y_pos][new_x_pos] == '0') continue;
                if (visited[new_y_pos][new_x_pos]) continue;

                visited[new_y_pos][new_x_pos] = true;
                q.push({new_y_pos, new_x_pos});

            }
        }




    }

    int numIslands(vector<vector<char>>& grid) {
        int ans = 0;
        int row = grid.size();
        int col = grid[0].size();

        vector<vector<bool>> visited(row, vector<bool> (col, false)); 

        for (int p = 0; p < row; ++p) {
            for (int q = 0; q < col; ++q){

                if ((grid[p][q] == '1') && visited[p][q] == false) {
                    ++ans;
                    bfs(grid, visited, q, p);

                }
            }
        }
    return ans;
        
    }
};
