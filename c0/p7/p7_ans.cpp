#include <bits/stdc++.h>
#define pis pair<int, string>
#define fi first
#define se second
using namespace std;

const int MAXSZ = 100005;

int n, q;
pis shops[MAXSZ];

bool sort_pis(pis a, pis b) {
    if (a.fi == b.fi) return a.se < b.se;
    return a.fi < b.fi;
}

signed main() {
    ios_base::sync_with_stdio(0);cin.tie(0);

    cin >> n >> q;
    for (int i = 0; i < n; i ++) {
        cin >> shops[i].se >> shops[i].fi;
    }
    sort(shops, shops + n, sort_pis);

    for (int i = 0, x; i < q; i ++) {
        cin >> x;
        int l = 0, r = n - 1;
        pis ans = {1e9, ""};
        while (l <= r) {
            int mid = (l + r) / 2;
            if (ans.fi > abs(shops[mid].fi - x)) ans = {abs(shops[mid].fi - x), shops[mid].se};
            else if (ans.fi == abs(shops[mid].fi - x)) ans.se = min(ans.se, shops[mid].se);
            if (shops[mid].fi < x) l = mid + 1;
            else if (shops[mid].fi >= x) r = mid - 1;
        }
        cout << ans.se << '\n';
    }

    return 0;
}