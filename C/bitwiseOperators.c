#include <stdio.h>
int main(){
	int i, j, n, k, a, b, or, and, xor, maxAnd=0, maxOr=0, maxXor=0;
	scanf("%d", &n);
	scanf("%d", &k);
	for(i=1; i<n; i++){
		for(j=i+1; j<=n; j++){
			a=i;
			b=j;
			and=a&b;
			or=a|b;
			xor=a^b;
			if(and<k)
				if(maxAnd<=and)
					maxAnd=and;
			if(or<k)
				if(maxOr<=or)
					maxOr=or;
			if(xor<k)
				if(maxXor<=xor)
					maxXor=xor;
			else
				continue;
		}
	}
	printf("%d\n%d\n%d", maxAnd, maxOr, maxXor);
}