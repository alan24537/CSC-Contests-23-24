#include <bits/stdc++.h>
using namespace std;

int n, d, ans;

signed main() {
    ios_base::sync_with_stdio(0);cin.tie(0);

    cin >> n >> d;
    for (int i = 0, c; i < n; i ++) {
        cin >> c;
        d -= c;
        if (d >= 0) ans ++;
    }
    cout << ans;

    return 0;
}