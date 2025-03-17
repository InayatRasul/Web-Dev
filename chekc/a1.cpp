// Online C++ compiler to run C++ program online
#include <iostream>
using namespace std;

int main() {
    int arr[3];
    for(int i = 0;i < 3;i++){
        int x;
        cin >> x;
        arr[i] = x;
    }
    if( arr[0] == 0 && arr[1] == 0 && arr[2] == 0){
        cout << 0;
        return 0;
    }
    for(int i = 0;i < 3;i++){
        for(int j = i+1;j < 3;j++){
            if(arr[i] < arr[j]){
                int v = arr[i];
                arr[i] = arr[j];
                arr[j] = v;
            }
        }
    }
    for(int i = 0;i < 3;i++){
        cout << arr[i];
    }
    

    return 0;
}