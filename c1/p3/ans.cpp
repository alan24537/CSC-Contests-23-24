#include <bits/stdc++.h>
using namespace std;

int n, x;

signed main() {
    ios_base::sync_with_stdio(0);cin.tie(0);

    cin >> n >> x;
    cout << (x / n) + (x % n != 0);

    return 0;
}