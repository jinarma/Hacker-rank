#include <stdio.h>
#include <math.h>
void update(int *a, int *b){
	int temp1, temp2;
	temp1=*a+*b;
	temp2=abs(*a-*b);
	*a=temp1;
	*b=temp2;
}
int main(){
	int a, b;
	int *pa, *pb;
	pa=&a;
	pb=&b;
	scanf("%d %d", &a, &b);
	update(pa, pb);
	printf("%d\n%d", a, b);
}