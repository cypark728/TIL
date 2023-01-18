#include <iostream>
#include <string>
#include <stack>

using namespace std;

int main(){
    int n;
    cin >> n;
    string dum;
    getline(cin, dum);
    for(int i=0; i<n; i++)
    {
        string input;
        getline(cin, input);
        stack<char> s;
        int check = 0;

        for(int j=0; j < input.length(); j++)
        {
            char temp = input[j];
            if(temp == '(')
            {
                s.push(temp);
            }
            else if(temp == ')')
            {
                if(!s.empty() && s.top() == '(')
                {
                    s.pop();
                }
                else
                {
                    check = -1;
                    break;
                }
            }
            else
            {
                check = 1;
                break;
            }
        }

        if(check == 0 && s.empty()){
            printf("YES\n");
        }
        else
        {
            printf("NO\n");
        }

    }


    return 0;
}