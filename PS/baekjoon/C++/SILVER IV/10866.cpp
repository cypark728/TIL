#include <iostream>
#include <deque>
#include <string>

using namespace std;

int main(){
    int n;
    cin >> n;
    string s;
    deque<int> d;
    int temp;
    for(int i = 0; i < n; i++){
        cin >> s;
        if(s == "push_front"){
            cin >> temp;
            d.push_front(temp);
        }
        else if(s == "push_back"){
            cin >> temp;
            d.push_back(temp);
        }
        else if(s == "pop_front"){
            if(d.empty()){
                printf("-1\n");
            }
            else{
                printf("%d\n", d.front());
                d.pop_front();
            }
        }
        else if(s == "pop_back"){
            if(d.empty()){
                printf("-1\n");
            }
            else{
                printf("%d\n", d.back());
                d.pop_back();
            }
        }
        else if(s == "size"){
            printf("%d\n", d.size());
        }
        else if(s == "empty"){
            if(d.empty()){
                printf("1\n");
            }
            else{
                printf("0\n");
            }
        }
        else if(s == "front"){
            if(d.empty()){
                printf("-1\n");
            }
            else{
                printf("%d\n", d.front());
            }
        }
        else if(s == "back"){
            if(d.empty()){
                printf("-1\n");
            }
            else{
                printf("%d\n", d.back());
            }
        }
    }

    return 0;
}