#include <bits/stdc++.h>
using namespace std;

const int MAXSZ = 10005;

int n, loops;
string name, sec;
string names[MAXSZ];
bool visited[MAXSZ];
unordered_map<string, string> ss;
unordered_map<string, int> si;

void dfs(string cur) {
    if (visited[si[cur]]) {
        loops ++;
        return;
    }
    visited[si[cur]] = true;
    dfs(ss[cur]);
}

signed main() {
    ios_base::sync_with_stdio(0);cin.tie(0);

    cin >> n;
    for (int i = 0; i < n; i ++) {
        cin >> name >> sec;
        names[i] = name;
        ss[name] = sec;
        si[name] = i;
    }
    
    for (int i = 0; i < n; i ++) {
        if (!visited[i]) {
            dfs(names[i]);
        }
    }
    cout << loops;

    return 0;
}