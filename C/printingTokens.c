#include <stdio.h>
#include <stdlib.h>
int main(){
	int i=0, j=0;
	char *s;
	s=malloc(1024*sizeof(char));
	gets(s);
	char token;
	char buffer[20];
	while(s[i]!='\0'){
		token=s[i];
		if(token!=' '){
			printf("%c", token);
			j=0;
		}
		else if(token==' '){
			j++;
			if(j==1){
				printf("\n");
				j==0;
			}
			else
				printf('\0');;
		}
		i++;
	}
}