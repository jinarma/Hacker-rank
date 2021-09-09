#include <stdio.h>
int main()
{
	int num, i, sum=0, digit;
	scanf("%d", &num);
	for(i=1; i<=5; i++){
		digit=num%10;
		sum+=digit;
		num=num/10;
	}
	printf("%d", sum);
}
