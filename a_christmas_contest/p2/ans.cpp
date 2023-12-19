#include <bits/stdc++.h>
using namespace std;

const int section_values[4] = {1, 3, 7, 11};

int n, max_len;
string tree[200][5];

string center(string s, int sz) {
    int l = (sz - s.size()) / 2;
    int r = sz - s.size() - l;
    return string(l, ' ') + s + string(r, ' ');
}

signed main() {
    ios_base::sync_with_stdio(0);cin.tie(0);

    cin >> n;
    for (int i = 0; i < n; i ++) {
        for (int j = 0; j < 4; j ++) {
            tree[i][j] = string(section_values[j] + (i * 5), '*');
            max_len = max(max_len, (int) tree[i][j].size());
        }
    }
    for (int i = 0; i < 5; i ++) {
        tree[n][i] = string(3, '#');
    }

    for (int i = 0; i < n; i ++) {
        for (int j = 0; j < 4; j ++) {
            tree[i][j] = center(tree[i][j], max_len);
            cout << tree[i][j] << '\n';
        }
    }
    for (int i = 0; i < 5; i ++) {
        tree[n][i] = center(tree[n][i], max_len);
        cout << tree[n][i] << '\n';
    }

    return 0;
}

