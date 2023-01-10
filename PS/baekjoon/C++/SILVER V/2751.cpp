#include <iostream>
#include <algorithm>

using namespace std;

int main(){
    int n = 0;
    cin >> n;
    int list[n];

    for(int i=0;i<n;i++){
        cin >> list[i];
    }
    
    sort(list, list+n);

    for(int j=0;j<n;j++){
        printf("%d\n", list[j]);
    }

    return 0;
}