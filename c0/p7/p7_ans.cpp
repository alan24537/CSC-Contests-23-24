#include <bits/stdc++.h>
using namespace std;

const string jp1[] = {"a", "i", "u", "e", "o", "n"};

const string jp2[] = {
    "ka", "ki", "ku", "ke", "ko",
    "sa", "su", "se", "so",
    "ta", "te", "to",
    "na", "ni", "nu", "ne", "no",
    "ha", "hi", "fu", "he", "ho",
    "ma", "mi", "mu", "me", "mo",
    "ya", "yu", "yo",
    "ra", "ri", "ru", "re", "ro",
    "wa", "wo"
};

const string jp3[] = {"shi","chi", "tsu"};

string s;

signed main() {
    ios_base::sync_with_stdio(0);cin.tie(0);

    cin >> s;
    for (int i = 0, matched = false; i < s.length();) {
        matched = false;
        for (string c3 : jp3) {
            if (i + 2 < s.length() && s[i] == c3[0] && s[i + 1] == c3[1] && s[i + 2] == c3[2]) {
                i += 3;
                matched = true;
                break;
            }
        }
        if (matched) continue;
        for (string c2 : jp2) {
            if (i + 1 < s.length() && s[i] == c2[0] && s[i + 1] == c2[1]) {
                i += 2;
                matched = true;
                break;
            }
        }
        if (matched) continue;
        for (string c1 : jp1) {
            if (s[i] == c1[0]) {
                i += 1;
                matched = true;
                break;
            }
        }
        if (!matched) {cout << "no"; return 0;}
    }
    cout << "yes";

    return 0;
}