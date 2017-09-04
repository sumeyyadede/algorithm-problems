#include <iostream>

#define NULL_VALUE -1
#define SIZE 100

using namespace std;

int binarySearch(int* arr, int x){
	int start = 0;
	int end = SIZE - 1;
	while(start <= end){
		int middle = (start + end) / 2;
		if(arr[middle] > x){
			end = middle - 1;
		}
		else if(arr[middle] < x){
			start = middle + 1;
		}
		else{
			return middle;
		}
	}
	return NULL_VALUE;
}

int binarySearchTwisted(int* arr, int x){
	int origStart = 0;
	int middle = 0;
	int prev = arr[0];
	int i = 1;
	int l_arr = SIZE;
	while(i < l_arr){
		if(arr[i] < prev){
			break;
		}
		prev = arr[i];
		i += 1;
	}
	origStart = i;

	int start = 0;
	int end = SIZE - 1;
	while(start <= end){
		middle = (start + end) / 2;
		if(arr[(middle + origStart) % l_arr] > x){
			end = middle - 1;
		}
		else if(arr[(middle + origStart) % l_arr] < x){
			start = middle + 1;
		}
		else{
			return (middle + origStart) % l_arr;
		}
	}
	return NULL_VALUE;
}

int main(){

	int arr[SIZE];
	for(int i=50; i<SIZE; i++){
		arr[i] = i;
		cout << arr[i] << endl;
	}
	for(int i=0; i<50; i++){
		arr[i] = i;
		cout << arr[i] << endl;
	}

	cout << "binarySearchTwisted" << endl;

	cout << binarySearchTwisted(arr, 100) << endl;

	return 0;
}
