#include <iostream>
using namespace std;

int calculate (int s, int k){
  int r = s;
  int i;
  
  for (i = 0; i < k; i++){
    
    if (r % 2 == 0){
      // cout << endl << r << endl;
      r = r - 99;
      // cout << endl << r << endl;
      if (r < 0){
        r = 1000000 + r;
      }
      // cout << endl << r << endl;
      r = r * 3;
      // cout << endl << r << endl;
      if (r > 1000000){
        r = r % 1000000;
      }
      // cout << endl << r << endl;
    }
      
    else if (r % 2 == 1){
      // cout << endl << r << endl;
      r = r - 15;
      // cout << endl << r << endl;
      if (r < 0){
        r = 1000000 + r;
      }
      // cout << endl << r << endl;
      r = r * 2;
      // cout << endl << r << endl;
      if (r > 1000000){
        r = r % 1000000;
      }
      // cout << endl << r << endl;
    }
  }
  return r;
}

int main() {
  int t, s, k, i, result;
  cin >> t;
  
  for (i = 0; i < t; i++){
    cin >> s >> k;
    result = calculate(s, k);
    cout << result;
    if (i < t - 1){
      cout << endl;
    }
    
  }
}
