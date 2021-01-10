/*
 ____       __  __
/ ___|  ___|  \/  | ___
\___ \ / _ \ |\/| |/ _ \
 ___) |  __/ |  | | (_) |
|____/ \___|_|  |_|\___/

*/
#include <bits/stdc++.h>
using namespace std;
#define fast  ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
#define test freopen("in", "r", stdin);
typedef long long ll;
typedef long int li;
typedef long double ld;
#define pi 3.141592653
#define endl '\n'

int main() 
{
  fast;
  //test
  int n, k, res = 0;
  cin >> n >> k;
  for(int i = 0; i < n; i++)
  {
    int x;
    cin >> x;
    if(x % k == 0)
    {
      res++;
    }
  }
  cout << res << endl;
}
