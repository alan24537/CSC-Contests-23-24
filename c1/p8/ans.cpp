#include <bits/stdc++.h>
using namespace std;

const int MAXSZ = 1e6 + 5;

int n, k;
unsigned long long ans;
int arr[MAXSZ];
map<int, int> freq;

signed main() {
    ios_base::sync_with_stdio(0);cin.tie(0);

    cin >> n >> k;
    for (int i = 0; i < n; i ++) {
        cin >> arr[i];
        arr[i] %= k;
        if (freq.find(arr[i]) == freq.end()) freq[arr[i]] = 1;
        else freq[arr[i]] ++;
    }
    for (int i = 0; i < n; i ++) {
        if (freq.find(k - arr[i]) != freq.end()) ans += freq[k - arr[i]];
        if (freq.find(0) != freq.end() && arr[i] == 0) ans += freq[0] - 1;
    }
    cout << ans / 2;

    return 0;
}