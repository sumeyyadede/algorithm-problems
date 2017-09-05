#include <iostream>

using namespace std;

int sorted_merge(int* a, int* b, int l_a){
	int l_b = 3;
	int l_m = 7;
	l_a -= 1;
	while(l_m > -1){
		if(l_a > -1 and a[l_a] > b[l_b]){
			a[l_m] = a[l_a];
			l_a -= 1;
		}
		else if (l_b > -1){
			a[l_m] = b[l_b];
			l_b -= 1;
		}
		l_m -= 1;
	}  
}

int main(){
	
	int b[] = {1,3,5,7};
	int a[] = {0,2,4,6,-1,-1,-1,-1};

	int l_a = sizeof(a)/sizeof(a[0]);
	int l_b = sizeof(b)/sizeof(b[0]);
	l_a -= l_b;

	sorted_merge(a, b, l_a); 

	for(int i=0; i<8; i++){
		cout << a[i] << endl;
	}
	
	return 0;
}

// int main(){
	
// 	int size = 4;
// 	int b[] = {1,3,5,7};
// 	int* a = new int[size];

// 	int l_a = size;
// 	int l_b = sizeof(b)/sizeof(b[0]);
// 	cout << l_a << endl;
// 	cout << l_b << endl;

// 	for(int i=0; i<l_a; i++){
// 		a[i] = 2*i;
// 		cout << a[i] << endl;
// 	}

// 	a = (int*)malloc((l_a+l_b)*sizeof(int));
// 	for(int i=l_a; i<l_a+l_b; i++){
// 		a[i] = -1;
// 		cout << a[i] << endl;
// 	}

// 	for(int i=0; i<l_a+l_b; i++){
// 		cout << a[i] << endl;
// 	}


// 	// cout << sorted_merge(a, b, l_a) << endl;

// 	return 0;
// }
