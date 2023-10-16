#include <bits/stdc++.h>
using namespace std;

int t1, t2, t3, x;

signed main() {
    ios_base::sync_with_stdio(0);cin.tie(0);

    cin >> t1 >> t2 >> t3 >> x;
    cout << max(0, max({t1, t2, t3}) - x);

    return 0;
}