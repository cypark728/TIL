#include <iostream>
#include <queue>
#include <algorithm>

using namespace std;

int main(){
    int N;
    cin >> N;
    int list[N];

    int mean = 0;

    for(int i=0; i < N; i++){
        cin >> list[i];
        mean = mean + list[i];
    }

    sort(list, list + N);
    cout << mean / N << "\n";
    cout << list[N / 2] << "\n";
    cout << "Not Yet" << "\n";
    cout << list[N-1] - list[0] << "\n";



    return 0;
}