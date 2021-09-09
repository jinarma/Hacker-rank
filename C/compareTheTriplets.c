#include <stdio.h>
int main(){
	int i, a[3], b[3], result, alice=0, bob=0;
	for(i=0; i<3; i++)
		scanf("%d", &a[i]);
	for(i=0; i<3; i++)
		scanf("%d", &b[i]);
	for(i=0; i<3; i++){
		if(a[i]!=b[i]){
			if(a[i]>b[i])
				alice++;
			else
				bob++;
		}
		else
			continue;
	}
	printf("%d %d", alice, bob);
}