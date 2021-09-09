#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int simpleArraySum(int x);
int main(){
    int count, i=0, sum=0;
    int arr[1000];
    scanf("%d", &count);
    printf("%d", simpleArraySum(count));
    return 0;
}
int simpleArraySum(int count){
	int i, sum=0, arr[1000];
	for(i=0; i<count; i++){
        scanf("%d", &arr[i]);
    }
    for(i=0; i<count; i++){
        sum+=arr[i];
    }
    return sum;
}