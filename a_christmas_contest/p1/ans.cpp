#include <bits/stdc++.h>
using namespace std;

int n, p, tot;
string path;

signed main() {
    ios_base::sync_with_stdio(0);cin.tie(0);

    cin >> n >> p >> path;
    for (int i = 0; i < n; i ++) {
        if (path[i] == 'W') tot += p;
        else tot -= 1;
        if (tot < 0) {
            cout << "OH NO";
            return 0;
        }
    }
    cout << "YIPEE";

    return 0;
}