#include <iostream>
#include <string>
#include <map>

using namespace std;

bool isPalindromeHT(string str){

	int len = str.length();
	for(int i=0; i<len; i++){
		str[i] = tolower(str[i]);
	}
	int has_visited_odd = 0;
	
	map<char, int> ht;
	char* cstr= (char*) str.c_str();
	for(int i = 0; i<len; i++) {
		ht[cstr[i]] = ht[cstr[i]] + 1;
	}

	for(int i=0; i<ht.size(); i++){
		if((ht[i]%2)==1){
			if(has_visited_odd==1){
				return false;
			}
			else{
				has_visited_odd=1;
			}
		}
	}
	return true;
}

int main(){

	string str = "TactCoa";
	cout << isPalindromeHT(str) << endl; 

	return 0;
}
