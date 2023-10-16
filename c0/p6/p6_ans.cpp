#include <bits/stdc++.h>
using namespace std;

const int MAXSZ = 100005;

int n, q, c;
int menu[MAXSZ];
int psa[MAXSZ];

signed main() {
    ios_base::sync_with_stdio(0);cin.tie(0);

    cin >> n >> q >> c;
    for (int i = 0; i < n; i ++) {
        cin >> menu[i];
        psa[i + 1] = (menu[i] <= c) ? psa[i] + menu[i] : psa[i];
    }
    for (int i = 0, a, b; i < q; i ++) {
        cin >> a >> b;
        cout << psa[b] - psa[a - 1] << '\n';
    }

    return 0;
}