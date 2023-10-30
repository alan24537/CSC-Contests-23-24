#include <bits/stdc++.h>
#define pii pair<int, int>
#define fi first
#define se second
using namespace std;

const int MAXSZ = 1e4 + 5;

int n, m;
double ans = -1;
pii litter[MAXSZ], food[MAXSZ];
pii lans, fans;

double dist(pii a, pii b) {
    return sqrt(((a.fi - b.fi) * (a.fi - b.fi)) + ((a.se - b.se) * (a.se - b.se)));
}

signed main() {

    ios_base::sync_with_stdio(0);cin.tie(0);

    cin >> n >> m;
    for (int i = 0; i < n; i ++) {
        cin >> litter[i].fi >> litter[i].se;
    }
    for (int i = 0; i < m; i ++) {
        cin >> food[i].fi >> food[i].se;
    }

    for (int i = 0; i < n; i ++) {
        for (int j = 0; j < m; j ++) {
            if (dist(litter[i], food[j]) > ans) {
                ans = dist(litter[i], food[j]);
                lans = litter[i];
                fans = food[j];
            }
        }
    }
    cout << lans.fi << " " << lans.se << "\n";
    cout << fans.fi << " " << fans.se << "\n";
    
    return 0;
}