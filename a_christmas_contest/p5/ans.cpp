#include <bits/stdc++.h>
#define pii pair<int,int>
#define fi first
#define se second
using namespace std;

const int MAXSZ = 2005;
const pii moves[] = {{1, 0}, {0, 1}, {-1, 0}, {0, -1}};

int n, m, x, y, dist;
char grid[MAXSZ][MAXSZ];
pii start, home, pos;
bool visited[MAXSZ][MAXSZ];
queue<pair<pii, int>> q;
pair<pii, int> p;

signed main() {
    ios_base::sync_with_stdio(0);cin.tie(0);
    memset(visited, false, sizeof(visited));

    cin >> n >> m;
    for (int i = 0; i < n; i ++) {
        for (int j = 0; j < m; j ++) {
            cin >> grid[i][j];
            if (grid[i][j] == 'E') start = {i, j};
            if (grid[i][j] == 'H') home = {i, j};
        }
    }

    q.push({start, 0});
    visited[start.fi][start.se] = true;

    while (!q.empty()) {
        p = q.front(); q.pop();
        pos = p.fi;
        dist = p.se;
    
        if (pos == home) {
            cout << dist << endl;
            return 0;
        }

        for (pii move : moves) {
            x = pos.fi + move.fi; y = pos.se + move.se;
            if (x < 0 || x >= n || y < 0 || y >= m) continue;
            if (visited[x][y] || grid[x][y] == 'X') continue;
            visited[x][y] = true;
            q.push({{x, y}, dist + 1});
        }
    }
    cout << -1;

    return 0;
}