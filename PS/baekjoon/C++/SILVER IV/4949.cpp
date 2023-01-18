#include <iostream>
#include <string>
#include <stack>

using namespace std;

int main(){
    while(true){
        string input;
        getline(cin, input);

        if(input == "."){
            break;
        }

        stack<char> s;
        bool check = 0;

        for(int i=0; i<input.length(); i++){
            char temp = input[i];

            if((temp =='[') || (temp == '('))
            {
                s.push(temp);
            }
            else if(temp == ']')
            {
                if(!s.empty() && s.top() == '['){
                    s.pop();
                }else{
                    check = 1;
                    break;
                }
            }
            else if(temp == ')')
            {
                if(!s.empty() && s.top() == '('){
                    s.pop();
                }else{
                    check = 1;
                    break;
                }
            }
        }

        if(check == 0 && s.empty()){
            printf("yes\n");
        }else{
            printf("no\n");
        }


    }



    return 0;
}