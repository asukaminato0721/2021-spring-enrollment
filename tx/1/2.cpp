#include <bits/stdc++.h>
using namespace std;

int test(int n)
{
    deque<int> q;
    int cnt = 0;
    q.push_back(n);
    set<int> _set;
    while (!q.empty())
    {
        auto t = q.size();
        for (unsigned int i = 0; i < t; i++)
        {
            auto tmp = q.front();
            q.pop_front();
            if (tmp == 0)
            {
                return cnt;
            }
            if (tmp % 2 == 0)
            {
                if (_set.count(tmp / 2) == 0)
                {
                    q.push_back(tmp / 2);
                    _set.insert(tmp / 2);
                }
            }
            if (tmp % 3 == 0)
            {
                if (_set.count(tmp / 3) == 0)
                {
                    q.push_back(tmp / 3);
                    _set.insert(tmp / 3);
                }
            }
            if (_set.count(tmp - 1) == 0)
            {
                q.push_back(tmp - 1);
                _set.insert(tmp - 1);
            }
        }
        cnt++;
    }
    return 0;
};
int main()
{
    int T;
    scanf("%d", &T);
    while (T--)
    {
        int n;
        scanf("%d", &n);
        cout << test(n) << endl;
    }
    return 0;
}