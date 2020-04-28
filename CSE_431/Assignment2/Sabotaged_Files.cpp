#include <iostream>
#include <algorithm> 
#include <iterator>
#include <string>
#include <vector>
using namespace std;

int main() {
  int n, value;
  string answer = "";
  vector<int> values, sorted, swapped;
  cin >> n;
  // cout << n;
  
  for (int i = 0; i < n; i++){
    cin >> value;
    values.push_back(value);
    sorted.push_back(value);
  }
  sort(sorted.begin(), sorted.end());

  for (int i = 0; i < values.size(); i++){
    // cout << values[i] << " " << sorted[i] << endl;
    if (values[i] != sorted[i]){
      // swapped.push_back(values[i]);
      swapped.push_back(i);
    }
  }
  //   for (int i = 0; i < swapped.size(); i++){
  //   cout << swapped[i] << " ";
  // }
  
  if (values[swapped[0]] == sorted[swapped[1]] and swapped.size() == 2){
    answer += "yes";
    answer += "\n";
    answer += "swap ";
    answer += to_string(swapped[0]+1);
    answer += " ";
    answer += to_string(swapped[1]+1);
    cout << answer;
    }
    
  else{
    reverse(values.begin() + swapped[0], values.begin() + swapped[swapped.size()-1] + 1);
    for (int i = 0; i <= values.size(); i++){
      if(values[i] == sorted[i] and i < values.size()){
        continue;
      }
      else if (i == values.size()){
          answer += "yes";
          answer += "\n";
          answer += "reverse ";
          answer += to_string(swapped[0]+1);
          answer += " ";
          answer += to_string(swapped[swapped.size()-1]+1);
          cout << answer;
      }
      else{
        break;
      }
    }
  }
  
  if (answer == ""){
    cout << "no";
  }

}
