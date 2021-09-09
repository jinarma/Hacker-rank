#include <stdio.h>
#include <string.h>
int main(){
	char arr[1000];
	int result[10]={0,0,0,0,0,0,0,0,0,0};
	int i=0;
	scanf("%s", &arr);
	while(arr[i]!='\0'){
		if(arr[i]=='0')
			result[0]++;
		else if(arr[i]=='1')
			result[1]++;
		else if(arr[i]=='2')
			result[2]++;
		else if(arr[i]=='3')
			result[3]++;
		else if(arr[i]=='4')
			result[4]++;
		else if(arr[i]=='5')
			result[5]++;
		else if(arr[i]=='6')
			result[6]++;
		else if(arr[i]=='7')
			result[7]++;
		else if(arr[i]=='8')
			result[8]++;
		else if(arr[i]=='9')
			result[9]++;
		else if(arr[i]>'9' || arr[i]<'0'){
			i++;
			continue;
		}
		i++;
	}
	for(i=0; i<10; i++)
		printf("%d ", result[i]);
}