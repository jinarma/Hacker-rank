#include <stdio.h>
#include <stdlib.h>
int diagonalDifference(int size){
	int arr[10][10], i, j, leftToRight=0, rightToLeft=0, difference;
	for(i=0; i<size; i++){
		for(j=0; j<size; j++)
			scanf("%d", &arr[i][j]);
	}
	for(i=0, j=0; i<size, j<size; i++, j++)
		leftToRight+=arr[i][j];
	for(i=size-j-1, j=0; i>=0, j<size; i--, j++)
		rightToLeft+=arr[i][j];
	return abs(leftToRight-rightToLeft);
}
int main(){
	int size;
	int difference=diagonalDifference(size);
	printf("%d", difference);
}