#include <iostream>

using namespace std;

bool rotate(int **matrix,int len){

	if(len == 0){
	//((matrix.sizeof())/(matrix[0].sizeof()))){
		return false;
	}

	for(int layer=0; layer<len/2; layer++){
		cout << "layer " << layer << endl;
		int first=layer;
		int last=len-1-layer;

		for(int i=first; i<last; i++){
			int offset = i-first;
			int temp;
			printf("offset %d\n", offset);

			//keep the top
			temp = matrix[first][i];
			//left to top;
			matrix[first][i] = matrix[last-offset][first];
			//bottom to left
			matrix[last-offset][first] = matrix[last][last-offset];
			//right to bottom
			matrix[last][last-offset] = matrix[i][last];
			//temp to right
			matrix[i][last] = temp; 
	    }
	}
	return true;
}

int main(){

	int **matrix;
	int len = 4;
	matrix = new int *[len];
	for (int i = 0; i < len; i++) {
		matrix[i] = new int[len];
		for (int j = 0; j < len; j++) {
			matrix[i][j] = i * len + j;
		}
	}
	for (int i = 0; i < len; i++) {
		for (int j = 0; j < len; j++) {
			cout << matrix[i][j] << "\t";
		}
		cout << endl;
	}
	rotate(matrix,len);

	for (int i = 0; i < len; i++) {
		for (int j = 0; j < len; j++) {
			cout << matrix[i][j] << "\t";
		}
		cout << endl;
	}

	return 0;
}
