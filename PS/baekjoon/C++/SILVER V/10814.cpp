#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

struct Imf
{
    int order;
    int age;
    string name;
};

bool compare(const Imf& p1, const Imf& p2){
    if(p1.age == p2.age){
        return p1.order < p2.order;
    }else{
        return p1.age < p2.age;
    }
}

int main (){
    int N;

    cin >> N;

    Imf imf[N];

    for(int i=0; i<N; i++){
        imf[i].order = i + 1;
        cin >> imf[i].age;
        cin >> imf[i].name;
    }

    sort(imf, imf+N, compare);

    for(int j=0; j<N; j++){
        cout << imf[j].age << " " << imf[j].name << "\n";
    }



    return 0;
}