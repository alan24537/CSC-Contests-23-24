#include <bits/stdc++.h>
using namespace std;

int n, odd, even;

signed main() {
    ios_base::sync_with_stdio(0);cin.tie(0);

    cin >> n;
    for (int i = 0, x; i < n; ++i) {
        cin >> x;
        odd += x % 2 == 1;
        even += x % 2 == 0;
    }
    cout << (odd == even ? "meow" :"...");

    return 0;
}