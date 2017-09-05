#include <iostream>
#include <math.h>

#define NULL_VALUE -1
#define SIZE 100

using namespace std;

class Listy{
public:
	Listy();
	~Listy();
	int elementAt(int);
	int l[SIZE];
};

Listy::Listy(){
	for(int i=0; i<SIZE; i++){
		l[i] = 2*i;
	}
}

int Listy::elementAt(int i){
	if(i < SIZE){
		return l[i];
	}
	return NULL_VALUE;
}

int bsListy(Listy* listy,int x){
	int start = 0;
	int end = 0;
	int c = 0;
	int middle = 0;
	while(listy->elementAt(end) != -1 && listy->elementAt(end) <= x){
		start = end;
		end = pow(2,c) - 1;
		c += 1;
	}
	while(start <= end){
		middle = (start + end)/2;
		if(listy->elementAt(middle) == -1 || listy->elementAt(middle) > x){
			end = middle - 1;
		}
		else if(listy->elementAt(middle) < x){
			start = middle + 1;
		}
		else{
			return middle;
		}
	}
	return NULL_VALUE;
}

int main(){

	Listy* listy = new Listy();
	cout << bsListy(listy, 20) << endl;

	return 0;
}
