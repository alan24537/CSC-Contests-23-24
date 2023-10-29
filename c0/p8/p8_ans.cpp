#include <bits/stdc++.h>
#define pii pair<int, int>
#define fi first
#define se second
using namespace std;

const int MAXSZ = 100005;

int n, q;
pii claw[MAXSZ];
int pma[MAXSZ];

signed main() {
    ios_base::sync_with_stdio(0);cin.tie(0);

    cin >> n >> q;
    for (int i = 0; i < n; i ++) {
        cin >> claw[i].fi >> claw[i].se;
    }
    sort(claw, claw + n);

    pma[0] = claw[0].se;
    for (int i = 1; i < n; i ++) {
        pma[i] = max(pma[i - 1], claw[i].se);
    }

    for (int i = 0, d; i < q; i ++) {
        cin >> d;
        int hi = n - 1, lo = 0, mid, idx = 0;
        while (lo <= hi) {
            mid = (hi + lo) / 2;
            if (claw[mid].fi <= d) {lo = mid + 1; idx = max(mid, idx);}
            else hi = mid - 1;
        }
        cout << pma[idx] << "\n";
    }

    return 0;
}