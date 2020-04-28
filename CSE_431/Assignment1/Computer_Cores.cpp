#include <iostream>
#include <vector>
#include <string>
using namespace std;

int calculate (vector<string> grid){
  int size1 = 0;
  int size2 = 0;
  
    for(int i = 0; i < grid.size(); i++){
      for(int j = 0; j < grid[0].size(); j++){
          
          if(i == 0 or j == 0 or i == grid.size() - 1 or j == grid[0].size() - 1){
            continue;
          }
          
          int r = 0;
          
          if(size1 == 0 and grid[i][j] == 'G'){
            size1 = 1;
          }
          
          if(size2 == 0 and grid[i][j] == 'G'){
            size2 = 1;
          }
          
          if(size1 == 1 and grid[i-1][j] == 'G' and grid[i+1][j] == 'G' and grid[i][j-1] == 'G' and grid[i][j+1] == 'G'){
            size1 = 5;
            grid[i][j] = '*';
            grid[i-1][j] = '*';
            grid[i+1][j] = '*';
            grid[i][j-1] = '*';
            grid[i][j+1] = '*';
            if(i >= 2 and j >= 2 and grid[i-2][j] == 'G' and grid[i+2][j] == 'G' and grid[i][j-2] == 'G' and grid[i][j+2] == 'G'){
              size1 = 9;
              grid[i][j] = '*';
              grid[i-2][j] = '*';
              grid[i+2][j] = '*';
              grid[i][j-2] = '*';
              grid[i][j+2] = '*';
              if(i >=3 and j >= 3 and grid[i-3][j] == 'G' and grid[i+3][j] == 'G' and grid[i][j-3] == 'G' and grid[i][j+3] == 'G'){
                size1 = 13;
                grid[i][j] = '*';
                grid[i-3][j] = '*';
                grid[i+3][j] = '*';
                grid[i][j-3] = '*';
                grid[i][j+3] = '*';
                if(i >=4 and j >= 4 and grid[i-4][j] == 'G' and grid[i+4][j] == 'G' and grid[i][j-4] == 'G' and grid[i][j+4] == 'G'){
                  size1 = 17;
                  grid[i][j] = '*';
                  grid[i-4][j] = '*';
                  grid[i+4][j] = '*';
                  grid[i][j-4] = '*';
                  grid[i][j+4] = '*';
                  if(i >=5 and j >= 5 and grid[i-5][j] == 'G' and grid[i+5][j] == 'G' and grid[i][j-5] == 'G' and grid[i][j+5] == 'G'){
                    size1 = 21;
                    grid[i][j] = '*';
                    grid[i-5][j] = '*';
                    grid[i+5][j] = '*';
                    grid[i][j-5] = '*';
                    grid[i][j+5] = '*';
                  }
                }
              }
            }
          }
          
          if(size2 == 1 and grid[i-1][j] == 'G' and grid[i+1][j] == 'G' and grid[i][j-1] == 'G' and grid[i][j+1] == 'G'){
            size2 = 5;
            grid[i][j] = '+';
            grid[i-1][j] = '+';
            grid[i+1][j] = '+';
            grid[i][j-1] = '+';
            grid[i][j+1] = '+';
            if(i >= 2 and j >= 2 and grid[i-2][j] == 'G' and grid[i+2][j] == 'G' and grid[i][j-2] == 'G' and grid[i][j+2] == 'G'){
              size2 = 9;
              grid[i][j] = '+';
              grid[i-2][j] = '+';
              grid[i+2][j] = '+';
              grid[i][j-2] = '+';
              grid[i][j+2] = '+';
              if(i >= 3 and j >= 3 and grid[i-3][j] == 'G' and grid[i+3][j] == 'G' and grid[i][j-3] == 'G' and grid[i][j+3] == 'G'){
                size2 = 13;
                grid[i][j] = '+';
                grid[i-3][j] = '+';
                grid[i+3][j] = '+';
                grid[i][j-3] = '+';
                grid[i][j+3] = '+';
                if(i >= 4 and j >= 4 and grid[i-4][j] == 'G' and grid[i+4][j] == 'G' and grid[i][j-4] == 'G' and grid[i][j+4] == 'G'){
                  size2 = 17;
                  grid[i][j] = '+';
                  grid[i-4][j] = '+';
                  grid[i+4][j] = '+';
                  grid[i][j-4] = '+';
                  grid[i][j+4] = '+';
                  if(i >= 5 and j >= 5 and grid[i-5][j] == 'G' and grid[i+5][j] == 'G' and grid[i][j-5] == 'G' and grid[i][j+5] == 'G'){
                    size2 = 21;
                    grid[i][j] = '+';
                    grid[i-5][j] = '+';
                    grid[i+5][j] = '+';
                    grid[i][j-5] = '+';
                    grid[i][j+5] = '+';
                  }
                }
              }
            }
          }
          
      }
    }
    
  // for(int i = 0; i < grid.size(); i++){
  //   cout << grid[i] << endl;
  // }
  // cout << size1 << size2;
  return size1 * size2;
}

int main() {
  int n, m;
  string g;
  vector<string> grid;
  
  cin >> n >> m;
  
  for(int i = 0; i < n; i++){
    cin >> g;
    grid.push_back(g);
  }
  
  cout << calculate(grid);
}
