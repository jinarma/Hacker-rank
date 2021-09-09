#include <stdio.h>
#include <stdlib.h>
int main(){
	int i;
	char *s;
	s=malloc(1000*sizeof(char));
	scanf("%s", s);
	for(i=0; s[i]!='\0'; i++)
		continue;
	for(int j=i-1; j>=0; j--)
		printf("%c ", s[j]);
}