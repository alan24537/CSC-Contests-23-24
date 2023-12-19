#include <bits/stdc++.h>
using namespace std;

string date;

int compare_dates(string d1, string d2) {
    if (stoi(d1.substr(0, 4)) > stoi(d2.substr(0, 4))) {
        return true;
    }
    else if (stoi(d1.substr(0, 4)) < stoi(d2.substr(0, 4))) {
        return false;
    }

    if (stoi(d1.substr(5, 2)) > stoi(d2.substr(5, 2))) {
        return true;
    }
    else if (stoi(d1.substr(5, 2)) < stoi(d2.substr(5, 2))) {
        return false;
    }

    if (stoi(d1.substr(8, 2)) > stoi(d2.substr(8, 2))) {
        return true;
    }
    else if (stoi(d1.substr(8, 2)) < stoi(d2.substr(8, 2))) {
        return false;
    }

    return -1;
}

signed main() {
    ios_base::sync_with_stdio(0);cin.tie(0);

    cin >> date;
    if (date == "2023/12/25") {
        cout << "Merry Chirstmas!";
    }
    else {
        cout << (compare_dates(date, "2023/12/25") ? "Too Late ;-;" : "Not Yet ;-;");
    }

    return 0;
}