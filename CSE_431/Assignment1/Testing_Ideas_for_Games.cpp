#include <iostream>
using namespace std;

int calculate (int n, int m, int c){
  int left_over_games = 0;
  int total_games = 0;
  
  left_over_games = n / m;
  total_games = left_over_games;
  
  while (left_over_games >= c){
    left_over_games = left_over_games - c + 1;
    total_games += 1;
  }
  
  return total_games;
}

int main() {
  int t, n, m, c, i, result;
  cin >> t;
  
  for (i = 0; i < t; i++){
    cin >> n >> m >> c;
    result = calculate(n, m, c);
    cout << result;
    if (i < t - 1){
      cout << endl;
    }
    
  }
}
