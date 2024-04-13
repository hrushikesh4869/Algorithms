#include<bits/stdc++.h>
using namespace std;

int divisor_sum_naive(long long num)
{
	int ans = 1;

	for(int i = 2; (long long)i * i <= num; i++)
	{
		if(num % i == 0)
		{
			ans += i;
			ans += num/i;
		}
	}

	return ans;
}

int divisor_sum_fast(long long num)
{
	int ans = 1, orig = num;
	int count = 0, temp;

	if(num == 1)
		return 1;

	for(int i = 2; (long long)i * i <= num; i++)
	{
		count = 0;
		if(num % i == 0)
		{
			while(num % i == 0)
			{
				count++;
				num /= i;
			}

			temp = pow(i, count + 1);
			ans = ans * ((temp - 1)/(i - 1));
		}
	}

	if(num > 1)
		ans *= (1 + num);

	return ans - orig;
}

int main()
{
	int ans = 0;
	vector<int> vis(10000, 0);
	int a,b;
	for(int i = 1; i <= 10000; i++)
	{
		a = divisor_sum_fast(i);
		b = divisor_sum_fast(a);

		if(b == i && i != a && !vis[i] && !vis[a])
		{
			ans = ans + i + a;
			vis[i] = 1;
			vis[b] = 1;
		}
	}
	cout<<ans<<endl;
}
