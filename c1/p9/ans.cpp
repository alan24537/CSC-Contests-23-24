#include <bits/stdc++.h>
#define pii pair<int, int>
#define fi first
#define se second
using namespace std;

double tri_area(pii A, pii B, pii C) {
    return abs((A.fi*B.se + B.fi*C.se + C.fi*A.se) - (A.se*B.fi + B.se*C.fi + C.se*A.fi)) / 2.0;
}

pii a, b, c, p;

signed main() {
    ios_base::sync_with_stdio(0);cin.tie(0);

    cin >> a.fi >> a.se >> b.fi >> b.se >> c.fi >> c.se >> p.fi >> p.se;
    cout << (tri_area(a, b, p) + tri_area(b, c, p) + tri_area(c, a, p) == tri_area(a, b, c) ? "yes" : "no"); 

    return 0;
}