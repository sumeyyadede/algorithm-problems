#include <iostream>

using namespace std;

void zero_matrix(int **matrix,int x,int y){

	int rowArray[x]={0,0,0,0}, colArray[y]={0,0,0,0,0};

	for(int i=0; i<x; i++){
		for(int j=0; j<y; j++){
			if(matrix[i][j] == 0){
				rowArray[i] = 1;
				colArray[j] = 1;
			}
		}
	}

	for(int i=0; i<x; i++){
		if(rowArray[i] == 1){
			for(int z=0; z<y; z++){
				matrix[i][z] = 0;
			}
		}
	}
	
	for(int j=0; j<y; j++){
		if(colArray[j] == 1){
			for(int z=0; z<x; z++){
				matrix[z][j] = 0;
			}
		}
	}
}

int main(){

	int x=4, y=5;
	int **matrix;

	matrix = new int *[x];
	for(int i=0; i<x; i++){
		matrix[i] = new int [y]; 
		for(int j=0; j<y; j++){
			matrix[i][j] = i+j;
		}
	}

	for(int i=0; i<x; i++){
		for(int j=0; j<y; j++){
			cout<< matrix[i][j] << "\t";
		}
		cout<< endl;
	}

	cout<< endl;
	
	zero_matrix(matrix,x,y);

	for(int i=0; i<x; i++){
		for(int j=0; j<y; j++){
			cout<< matrix[i][j] << "\t";
		}
		cout<< endl;
	}
	return 0;
}
