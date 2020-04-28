#include <iostream>
#include <algorithm> 
#include <set>
#include <vector>
using namespace std;

int main() {
int n, k, outpost, distance, first, last;
vector<int> outposts;
vector<int> distances;
vector<int> choices;

cin >> n >> k;

for (int i = 0; i < k; i++){
  cin >> outpost;
  outposts.push_back(outpost);
}

sort(outposts.begin(), outposts.end()); 

if (outposts.size() > 1){
  for (int i = 0; i < outposts.size() - 1; i++){
  distances.push_back(outposts[i+1] - outposts[i]);
  }
  sort(distances.begin(), distances.end()); 

  distance = distances.back() / 2;
  first = outposts.front();
  last = n - 1 - outposts.back();
  
  choices.push_back(first);
  choices.push_back(last);
  choices.push_back(distance);
  sort(choices.begin(), choices.end()); 
  cout << choices.back();
}

if (k == 1){
  cout << n-1;
}

}
