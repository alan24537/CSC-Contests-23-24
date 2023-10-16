#include <bits/stdc++.h>
using namespace std;

const int MAXSZ = 10005;

int n, k, ans;
int ratings[MAXSZ];

signed main() {
    ios_base::sync_with_stdio(0);cin.tie(0);

    cin >> n >> k;
    for (int i = 0; i < n; i ++) {
        cin >> ratings[i];
    }
    sort(ratings, ratings + n, greater<int>());
    
    for (int i = 0; i < k; i ++) {
        ans += ratings[i];
    }
    cout << ans;

    return 0;
}