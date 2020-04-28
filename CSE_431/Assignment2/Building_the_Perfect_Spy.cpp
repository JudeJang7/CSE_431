#include <iostream>
#include <iomanip>
#include <algorithm>
#include <vector>
using namespace std;

int main() {

  long n, number, median;
  char operation;
  vector<long> numbers;

  cin >> n;
  for (int i = 0; i < n; i++){
    cin >> operation;
    cin >> number;

    if (operation == 'a'){
    
      numbers.push_back(number);
      size_t size = numbers.size(); 
      sort(numbers.begin(), numbers.end()); 
      
      if (numbers.size() == 1){
        cout << numbers[0] << endl;
      }
      
      else if (numbers.size() % 2 == 0 and numbers.size() >= 2){
        
        cout << std::fixed;
        cout << std::setprecision(1);
        
        median = numbers[size / 2 - 1] + numbers[size / 2];
        if (median % 2 == 0){
          cout << median / 2 << endl;
        }
        if (median % 2 == 1){
          cout << median / 2 + 0.5 << endl;
        }
        if (median % 2 == -1){
          cout << median / 2 - 0.5 << endl;
        }
        
      }
      
      else if (numbers.size() % 2 == 1 and numbers.size() >= 3){
        cout << numbers[size / 2] << endl;
      }
      
    }
    
    if (operation == 'r') {

      vector<long>::iterator it;
      it = find (numbers.begin(), numbers.end(), number);
        if (it != numbers.end()){
          numbers.erase(it);
          size_t size = numbers.size();
          sort(numbers.begin(), numbers.end());
          
          if (numbers.size() == 0){
            cout << "Wrong!" << endl;
          }
          
          else if (numbers.size() == 1){
            cout << numbers[0] << endl;
          }
          
          else if (numbers.size() % 2 == 0 and numbers.size() >= 2){
            
              cout << std::fixed;
              cout << std::setprecision(1);
              
              median = numbers[size / 2 - 1] + numbers[size / 2];
              // cout << median << endl;
              if (median % 2 == 0){
                cout << median / 2 << endl;
              }
              if (median % 2 == 1){
                cout << median / 2 + 0.5 << endl;
              }
              if (median % 2 == -1){
                cout << median / 2 - 0.5 << endl;
              }
          }
          
          else if (numbers.size() % 2 == 1 and numbers.size() >= 3){
            cout << numbers[size / 2] << endl;
          }
          
        }
        else{
          cout << "Wrong!" << endl; 
        }
    }
  // cout << numbers.size() << endl;
  }
}
