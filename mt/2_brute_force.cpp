#pragma GCC optimize(3, "Ofast", "inline")
#include <bits/stdc++.h>
using namespace std;
#define all(x) (x).begin(), (x).end()
vector<int> a, b;
long long get(vector<int> &arr, int &d)
{
    long long sum = 0;
    for (auto &&i : arr)
    {
        sum += (i <= d) ? 1 : 2;
    }
    return sum;
}
int main()
{
    int n, m;
    scanf("%d%d", &n, &m);
    for (int i = 0; i < n; i++)
    {
        int tmp;
        scanf("%d", &tmp);
        a.push_back(tmp);
    }
    for (int i = 0; i < m; i++)
    {
        int tmp;
        scanf("%d", &tmp);
        b.push_back(tmp);
    }
    long long _max = -999999999;
    for (int i = 1; i <= 1000; i++)
    {
        _max = max(_max, get(b, i) - get(a, i));
    }
    cout << _max << endl;
    return 0;
}