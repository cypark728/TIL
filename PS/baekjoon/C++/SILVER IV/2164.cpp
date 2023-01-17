#include <iostream>
#include <queue>

using namespace std;

int main(){
    int n;
    int temp;
    cin >> n;
    queue<int> q; 
    for(int i=1; i<n+1; i++){
        q.push(i);
    }

    for(int j=1; j<n; j++){
        q.pop();
        temp = q.front();
        q.pop();
        q.push(temp);
    }   
    cout << q.front();



    return 0;
}