#include <stdio.h>
int max_of_four(int a, int b, int c, int d){
	int i, temp, arr[4], max;
	arr[0]=a;
	arr[1]=b;
	arr[2]=c;
	arr[3]=d;
	max=arr[0];
	for(i=1; i<4; i++){
		if(arr[i]>max)
			max=arr[i];
		else
			continue;
	}
	return max;
}
int main(){
	int a, b, c, d;
	scanf("%d", &a);
	scanf("%d", &b);
	scanf("%d", &c);
	scanf("%d", &d);
	int max=max_of_four(a, b, c, d);
	printf("%d", max);
}