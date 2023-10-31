#include <bits/stdc++.h>
using namespace std;

const string names[] = {"miso", "hakuto", "ringo", "paula", "sprite"}; 

string s;

signed main() {
    ios_base::sync_with_stdio(0);cin.tie(0);

    cin >> s;
    cout << (s == "miso" || s == "hakuto" || s == "ringo" || s == "paula" || s == "sprite" ? "no" : "yes");

    return 0;
}