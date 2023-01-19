#include <iostream>

using namespace std;

int main(){
    int n;
    int result = 0;
    scanf("%d", &n);
    int list[n];
    int temp;
    int j = 0;
    
    for(int i=0; i<n; i++){
        cin >> temp;
        if(temp == 0){
            list[j-1] = 0;
            j = j -1;
        }
        else{
            list[j] = temp;
            j++;
        }
        
    }
    for(int i=0; i<j; i++){
        result = result + list[i];
    }
    printf("%d", result);



    return 0;
}