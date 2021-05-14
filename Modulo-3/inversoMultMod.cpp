#include <iostream>

using namespace std;
int imod(int a,int n){
  int c,i=0;
  while(1){
    c = n * i + 1;
    if(c%a==0){
        c = c/a;
        break;
    }
    i++;
  }
  return c;
}

int main() {
    cout << "Digite x e y : para x mod y" << endl;
    int x, y;
    cin >> x >> y;
    cout << "inverso mod = " << imod(x,y) << endl;
};
