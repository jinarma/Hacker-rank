#include <stdio.h>
int main(){
	int s1, s2, sum;
	float d1, d2, diff;
	scanf("%d %d", &s1, &s2);
	scanf("%f %f", &d1, &d2);
	printf("%d %d\n", s1+s2, s1-s2);
	printf("%.1f %.1f\n", d1+d2, d1-d2);
}