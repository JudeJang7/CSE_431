#include <iostream>
#include <vector>
#include <ctime>
#include <algorithm>
#include <stdio.h>
#include <set>

using namespace std;

const int N = 500000;
const int NUM_ITERS = 1;




int main()
{
  vector<int> ordered_vector;
  std::multiset<int> mset;
	clock_t time_tot_vec = 0;
  clock_t time_tot_ms = 0;
	int i;
	int num_items = N;

  srand(time(0));

	for (int j = 0; j < NUM_ITERS; j++)
	{
    mset.clear();
    ordered_vector.clear();
		for (i = 0; i < N; i++)
		{
      int r = rand();
			std::clock_t start_time_vec = std::clock();
		  vector<int>::iterator iter = upper_bound(ordered_vector.begin(), ordered_vector.end(), r);
			ordered_vector.insert(iter, r);
			time_tot_vec += clock() - start_time_vec;

      std::clock_t start_time_ms = std::clock();
      mset.insert(r);
      time_tot_ms += clock() - start_time_ms;
		}
	}

	printf("For %d items: \n", num_items);
	printf("Vector Time:        %.8f seconds \n", (((((double) time_tot_vec) / (double)CLOCKS_PER_SEC)) / (double)NUM_ITERS));
	printf("Multiset Time:      %.8f seconds \n", (((((double)time_tot_ms)   / (double)CLOCKS_PER_SEC)) / (double)NUM_ITERS));
}
