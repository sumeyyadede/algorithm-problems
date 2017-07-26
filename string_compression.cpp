#include <iostream>
#include <string>

using namespace std;

string compress(string str){
	int count = 1;
	char prev_s = str[0];
	string newString = "";
	for(int i = 1; i <= str.length(); i++){
		if(prev_s == str[i]){
			count +=  1;
		} 
		else{
			newString = newString + prev_s + to_string(count);
			count = 1;
			prev_s = str[i];
		}
	}	
	if (newString.length() < str.length()){
		return newString;
	}
	else{
		return str;
	}	
}

int main(){
	string str = "aaaaaaabcs";
	cout << compress(str) << endl;

	return 0;
}
