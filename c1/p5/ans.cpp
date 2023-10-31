#include <bits/stdc++.h>
using namespace std;

const int MAXSZ = 1e5 + 5;

int n;
int arr[MAXSZ];

signed main() {
    ios_base::sync_with_stdio(0);cin.tie(0);

    cin >> n;
    for (int i = 0; i < n; i ++) {
        cin >> arr[i];
    }
    sort(arr, arr + n, greater<int>());

    for (int i = 0; i < n; i ++) {
        if (arr[i] != arr[0]) {
            cout << arr[i];
            return 0;
        }
    }
    cout << -1;

    return 0;
}