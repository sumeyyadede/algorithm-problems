#include <map>
#include <iostream>
#include <cassert>

using namespace std;


bool isUniqueHT(string str) {

	map<char, int> ht;
	char* cstr = (char*) str.c_str();

	for(int i = 0;i < str.length(); i++) {
		if(ht[cstr[i]] == 0){
			ht[cstr[i]] = 1;
		}
		else {
			return false;
		}
	}
	return true;
}

int main(int argc, char **argv) {

	string input = "Sumeya";

	cout << isUniqueHT(input) << endl;
	
	return 0;
}
