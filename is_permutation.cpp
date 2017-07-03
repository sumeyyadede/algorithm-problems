#include <iostream>
#include <string>
#include <map>
#include <cassert>

using namespace std;

bool isPermutationHT(string str1,string str2){

	if(str1.length() != str2.length()){
		return false;
	}

	if (str1.compare(str2) == 0){
		return false;
	}

	map<char, int> ht;
	char* cstr1= (char*) str1.c_str();
	for(int i = 0; i<str1.length(); i++) {

		if(ht[cstr1[i]] == 0){
			ht[cstr1[i]] = ht[cstr1[i]] + 1;
		}
		else {
			ht[cstr1[i]] = ht[cstr1[i]] + 1;
		}
	}

	char* cstr2 = (char*) str2.c_str();
	for(int i=0; i<str2.length(); i++){

		if(ht[cstr2[i]] != 0){
			ht[cstr2[i]] = ht[cstr2[i]] - 1;

		 if(ht[cstr2[i]] < 0){
		 	return false;
		 }
		}

		else {
			return false;
		}

		return true;
	}
}

int main(int argc, char **argv){

	string string1 = "sumeyya";
	string string2 = "suyyaem";

	cout << isPermutationHT(string1,string2) << endl;

	return 0;
}
