#include <iostream>
#include <string>

using namespace std;

int main (){
    int n;
    int temp = 0;
    int i = 666;
    string str;

    cin >> n;

    while(true){
        str = to_string(i);
        if(str.find("666") != std::string::npos){
            temp ++;
        }

        if(temp == n){
            cout << i << endl;
            break;
        }
        i++;
    }



    return 0;
}