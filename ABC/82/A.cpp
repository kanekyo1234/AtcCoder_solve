#include <bits/stdc++.h>
using namespace std;

int main() {
    int a,b;
    cin >> a>>b;
    cout << (max(a,b)-min(a,b)+1)/2+min(a,b)<< endl;
    return 0;
}
