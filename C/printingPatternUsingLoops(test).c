#include <stdio.h>
int main(){
	int n, i, j, k, l=0;
	scanf("%d", &k);
	n=k*2-1;
	for(i=0; i<n; i++){
		for(j=0; j<n; j++){
			printf("(%d, %d)", i, j);
			if(j==n-1)
				printf("\n");
			else
				printf(" ");
		}
	}
}