#include <iostream>
#include <string>
#include <cmath>
#include <algorithm>

using namespace std; 
 
bool oneWay(string str1,string str2){

	int l1 = str1.length();
	int l2 = str2.length();

	if( abs(l1-l2)>1 ){
		return false;
	}

	int has_operator = 0;
	int i = 0;
	char* cstr1 = (char*) str1.c_str();
	char* cstr2 = (char*) str2.c_str();
	
	while( i <= min(l1,l2) ){
		if(cstr1[i] != cstr2[i]){
			if(has_operator==0){
				if (l1>l2){
					cout<< "first string: "<< str1 <<endl;
					str1 = str1.substr (0, i) + str1.substr(i+1);
					cout<< "new string: "<< str1 <<endl;
					cout<< "second string: "<< str2 <<endl;
				}
				else if (l1<l2){
					cout << "first string: " << str1 << endl;
					cout << "second string: " << str2 << endl;
					char letter = cstr2[i];
					str1 = str1.substr(0,i) + letter + str1.substr(i);
					cout<< "new string: " << str1 << endl;
				}
			has_operator = 1;
			}
			else{
				return false;
			}
		}
		else {
		i = i+1;
     	}
    }
    return true;
}

int main(){

	string string1 = "pale";
	string string2 = "pami";

	cout << oneWay(string1,string2) <<endl;

	return 0; 
}
