#include <stdio.h>
#include <iostream>
#include <algorithm>

using namespace std;

int w[110];
int v[110];
int value[110][100101];
	
void backpack(int n, int k) {
    for (int i=1; i<=n; i++) {
    	for (int j=1; j<=k; j++) {
    		if (j >= w[i]) {
				value[i][j] = max(value[i-1][j], value[i-1][j-w[i]] + v[i]); 
			}
			else {
				value[i][j] = value[i-1][j]; 
			}
		}
	}
	cout << value[n][k] ;
}

int main() {
    int n, k;
    cin >> n >> k;
    
    for (int i=1; i<=n; i++) { cin >> w[i] >> v[i];	}
    backpack(n, k);
    
    return 0;
}
