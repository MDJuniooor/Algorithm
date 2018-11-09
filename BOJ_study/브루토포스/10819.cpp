#include <iostream>
#include <algorithm>
#include <cmath>
#include <vector>
using namespace std;
int a[10];
int n;
int ans;
int calculate(int *a){
	int sum =0;
	for(int i=0;i<n-1;i++){
		sum+=abs(a[i]-a[i+1]);
	}
	return sum;
}
int main(){
	cin >> n;
	for(int i=0;i<n;i++){
		cin >>a[i];
	}
	sort(a,a+n);
	do{
		int temp = calculate(a);
		ans = max(ans,temp);
	} while(next_permutation(a.begin(),a.end()));
	count << ans << '\n';
	return 0;	
}
