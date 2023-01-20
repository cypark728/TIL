#include <iostream>
#include <string>
#include <stack>

using namespace std;

int main(){
    int n;
    int x;
    cin >> n;
    string s;
    stack<int> temp;
    for(int i=0; i<n; i++){
        cin >> s;
        if(s[1] == 'u'){
            cin >> x;
            temp.push(x);
        }
        else if(s == "pop"){
            if(temp.empty()){
                printf("-1\n");
            }
            else{
                printf("%d\n", temp.top());
                temp.pop();
            }
        }
        else if(s == "size"){
            printf("%d\n", temp.size());
        }
        else if(s == "empty"){
            if(temp.empty()){
                printf("1\n");
            }
            else{
                printf("0\n");
            }
        }
        else if(s == "top"){
            if(temp.empty()){
                printf("-1\n");
            }
            else{
                printf("%d\n", temp.top());
            }
        }
    }


    return 0;
}