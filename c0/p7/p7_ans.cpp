#include <bits/stdc++.h>
using namespace std;

string japanese[] = {
"a", "i", "u", "e", "o",
"ka", "ki", "ku", "ke", "ko",
"sa", "shi", "su", "se", "so",
"ta", "chi", "tsu", "te", "to",
"na", "ni", "nu", "ne", "no",
"ha", "hi", "fu", "he", "ho",
"ma", "mi", "mu", "me", "mo",
"ya", "yu", "yo",
"ra", "ri", "ru", "re", "ro",
"wa", "wo", "n"
};

string s;

signed main() {
    ios_base::sync_with_stdio(0);cin.tie(0);

    cin >> s;
    for (int i = 0, matched = false; i < s.length();) {
        matched = false;
        for (int j = 0; j < 46; j++) {
            if (s.substr(i, japanese[j].length()) == japanese[j]) {
                i += japanese[j].length();
                matched = true;
                break;
            }
        }
        if (!matched) {cout << "no"; return 0;}
    }
    cout << "yes";

    return 0;
}