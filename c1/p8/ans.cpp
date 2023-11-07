#include <bits/stdc++.h>
using namespace std;

const int MAXSZ = 1e6 + 5;

int n, k;
unsigned long long ans;
int arr[MAXSZ];
unordered_map<int, int> freq;

signed main() {
    ios_base::sync_with_stdio(0);cin.tie(0);

    cin >> n >> k;
    for (int i = 0; i < n; i ++) {
        cin >> arr[i];
        arr[i] %= k;
        if (freq.find((k - arr[i]) % k) != freq.end()) ans += freq[(k - arr[i]) % k];
        if (freq.find(arr[i]) == freq.end()) freq[arr[i]] = 1;
        else freq[arr[i]] ++;
        
    }
    cout << ans;

    return 0;
}