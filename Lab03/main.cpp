#include <iostream>
using namespace std;

//Global
int elements = 0;

//Structure for the values
struct SAM{
    int sum;
    int max;
    float avg;
};


//Function to calculate sum, average, and maximum
SAM ArrayFunctions(int arr[], int length){
    SAM sam;    
    int sum = 0;
    int max = 0;
    float avg = 0;
    for(int i = 0; i < length; i++){
        elements++;
        sum = sum + arr[i];
        if(arr[i] > max){
            max = arr[i];
        }
    }
    //Set values to structure
    sam.sum = sum;
    sam.avg = sum/length;
    sam.max = max;
    cout << "Total elements processed = " << elements << endl;
    return sam;
}

//main function
int main(int argc, char** argv){
    int arr[] = {1,7,4,98,34,2,6};
    int length = sizeof(arr)/sizeof(arr[0]);
    int arr2[] = {1,7,4,98,34,2,6,87,4,102,15,61,3,9,90};
    int length2 = sizeof(arr2)/sizeof(arr2[0]);
    SAM sam = ArrayFunctions(arr, length);
    SAM sam2 = ArrayFunctions(arr2, length2);
    cout<<"sum = " << sam.sum << endl << "avg = " << sam.avg << endl << "max = " << sam.max << endl; 
    cout<<"sum = " << sam2.sum << endl << "avg = " << sam2.avg << endl << "max = " << sam2.max << endl;
    
    //lambda function for sorting array in descending order
    auto sortedArr = [] (int arr2[],int len) -> void{
        // for(int i = 0; i<len;i++){
        //     cout << arr2[i]<< " ";
        // }
        // cout << endl;
        int temp;
        for(int i = 1; i<len;i++){
            int j = i-1;
            int z = i;
            while(arr2[z]>arr2[j] && j>=0){
                temp = arr2[j];
                arr2[j] = arr2[z];
                arr2[z] = temp;
                // cout<<"i is "<<i<<", z is "<<z<<", j is "<<j<<endl;
                z--;
                j--;
                
            }
        }
        
        for(int k = 0; k<len;k++){
            cout << arr2[k]<< " ";
        }
        cout << endl;
    };
    sortedArr(arr2,length2);
    sortedArr(arr,length);
}