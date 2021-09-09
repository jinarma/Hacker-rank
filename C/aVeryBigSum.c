#include <stdio.h>
int main(){
	int count, i;
	long int arr[20], sum=0, num;
	scanf("%d", &count);
	for(i=0; i<count; i++){
		scanf("%ld", &num);
		arr[i]=num;
		sum+=num;
	}
	printf("%ld", sum);
}