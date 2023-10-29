#include <iostream>
#define psi pair<string, int>
#define fi first
#define se second
using namespace std;

const int MAXSZ = 1005;

int n, q;
psi shops[MAXSZ];

signed main() {
    ios_base::sync_with_stdio(0);cin.tie(0);

    cin >> n >> q;
    for (int i = 0; i < n; i ++) {
        cin >> shops[i].fi >> shops[i].se;
    }

    for (int i = 0, x; i < q; i ++) {
        cin >> x;
        psi ans = {"", 1e9};
        for (int j = 0; j < n; j ++) {
            if (abs(shops[j].se - x) < abs(ans.se - x)) {
                ans = shops[j];
            }
        }
        cout << ans.fi << '\n';
    }
    return 0;
}