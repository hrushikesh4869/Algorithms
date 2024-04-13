#include<bits/stdc++.h>
using namespace std;


string add_string(string s1, string s2)
{
	if(s1 == "")
		return s2;
	if(s2 == "")
		return s1;

	int l1,l2,carry = 0,temp,d1,d2;
	string result = "";

	l1 = s1.length() - 1;
	l2 = s2.length() - 1;

	if(l2 > l1)
		return add_string(s2,s1);

	while(l1 >= 0 && l2 >= 0)
	{
		d1 = s1[l1--] - '0';
		d2 = s2[l2--] - '0';

		temp = d1 + d2 + carry;
		carry = temp/10;
		temp = temp%10;

		result = char(temp + '0') + result;
	}

	if(l1 >= 0)
	{
		while(l1 >= 0)
		{
			d1 = s1[l1--] - '0';
			d2 = 0;

			temp = d1 + d2 + carry;
			carry = temp/10;
			temp = temp%10;

			result = char(temp + '0') + result;
		}
	}

	if(carry)
		result = '1' + result;

	return result;

}

string factorial(int num)
{

	string s = "1",temp;

	if(num == 1 || num == 0)
		return "1";

	for(int i = 2; i <= num; i++)
	{
		temp = "0";
		for(int j = 0; j<i; j++)
		{
			temp = add_string(temp,s);
		}
		s = temp;
	}
	return s;
}

int main()
{
	string temp = factorial(100);
	int ans = 0;

	for(int i = 0; i<temp.size(); i++)
		ans += (temp[i] - '0');

	cout<<ans<<endl;
}
