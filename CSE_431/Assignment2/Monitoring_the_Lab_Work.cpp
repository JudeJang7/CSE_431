#include <iostream>
#include <vector>
#include <algorithm> 
using namespace std;

int main() {
  int n, type, value;
  vector<int> values;
  
  cin >> n;
  
  for (int i = 0; i < n; i++){
    cin >> type;
    // cout << type;
    if (type == 1){
      cin >> value;
      // cout << ' ' << value;
      values.push_back(value);
    }
    else if (type == 2){
      values.pop_back();
    }
    else if (type == 3){
      int size = values.size();
      cout << *max_element(values.begin(),values.end()) << endl;
    }
    // cout << endl;
  }
}
