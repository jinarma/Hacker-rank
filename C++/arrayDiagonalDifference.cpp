#include<iostream>
#include<cstdlib>
#include<vector>
#include<new>
using namespace std;
int diagonal_difference(int** arr, int size){
	int sum1=0, sum2=0;
	for(int i=0; i<size; i++){
		for(int j=0; j<size; j++){
			if(i==j){
				sum1+=arr[i][j];
			}
			else
				continue;
		}
	}
	for(int i=0; i<size; i++){
		for(int j=0; j<size; j++){
			if(i==(size-1)-j){
				sum2+=arr[i][j];
			}
			else
				continue;
		}
	}
	return abs(sum1-sum2);
}
int main(){
	vector<int> arr(10);
	//int (*arr1)[10] = new int[10][10];
	int size, i, j, modulusDifference;
	cout<<"What is the size of the array?\n";
	cin>>size;
	for(i=0; i<size; i++){
		for(j=0; j<size; j++){
			cin>>arr[i][j];
		}
	}
	modulusDifference=diagonal_difference((*arr), size);
	cout<<modulusDifference;
}