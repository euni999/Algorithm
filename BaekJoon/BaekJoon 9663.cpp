#include <stdio.h>
#include <iostream>
#include <math.h>

using namespace std;

int col[110];
int N;
int result = 0;

bool promising(int i) 
{
    int k=0;
	
	while (k<i) {
		if (col[i] == col[k] || abs(col[i] - col[k]) == i-k)
			{ return  false; }
		k++;
	}
	return true;
}
void queens(int i)
{
    if(i == N)
        result++;
    else {
        for(int j=1; j<=N; j++) {
            col[i] = j;
            if(promising(i))
               queens(i+1);
        }
    }
}

int main()
{
    cin>>N;

    queens(0);

    cout<< result;

    return 0;
}
