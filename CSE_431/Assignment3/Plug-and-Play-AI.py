#include<iostream>
#include<vector>
using namespace std;
int main()
{
  int t, n, l, brick;
  
  cin >> t;
  
  for (int i = 0; i < t; i++){
    cin >> n >> l;

    vector<int> bricks;
    for (int j = 0; j < n; j++){
      cin >> brick;
      bricks.push_back(brick);
    }
    
    vector<int> answers(l+1, 1);
  
    for (int j = 1; j < l+1; j++){
      int answer = 0;
      for (int k = 0; k < bricks.size(); k ++){
        if (j - bricks[k] >= 0){
          answer += answers[j-bricks[k]];
          answer = answer % 1000000009; 
        }
      }
      answers[j] = answer;
    }
    
    cout << answers[l] << endl;
  }
  
}
