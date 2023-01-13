#include <iostream>

using namespace std;

struct Person
{
    int weight;
    int height;
    int rank = 1;
};

int main(){
    int N;
    cin >> N;
    Person person[N];

    for(int i=0; i<N; i++){
        cin >> person[i].weight;
        cin >> person[i].height;
    }

    for(int j=0; j<N; j++){
        for(int k=0; k<N; k++){
            if(person[j].weight<person[k].weight && person[j].height<person[k].height){
                person[j].rank ++;
            }
        }
        printf("%d ", person[j].rank);
    }


    return 0;
}