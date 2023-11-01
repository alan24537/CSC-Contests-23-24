#include <bits/stdc++.h>
using namespace std;

const int MAXSZ = 1e5 + 5;

int n, k, ans;
int arr[MAXSZ];

signed main() {
    ios_base::sync_with_stdio(0);cin.tie(0);

    cin >> n >> k;
    for (int i = 0; i < n; i ++) {
        cin >> arr[i];
    }

    for (int i = 0; i < n; i ++) {
        for (int j = i + 1; j < n; j ++) {
            if ((arr[i] + arr[j]) % k == 0) {
                ans ++;
            }
        }
    }
    cout << ans;

    return 0;
}