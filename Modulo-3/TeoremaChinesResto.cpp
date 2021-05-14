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
  

  int A[100],M[100],B[100],B2[100],K[100],ABK[100]; 
  int Y = 1;
  int Soma = 0;
  int qtd = 0;
  cout << "São quantas equações ? " << endl;
  cin >> qtd;



  for(int i = 0 ; i < qtd ; ++i){
    cout << "Digite os valores A e M da equação " << i+1 
    << " " << "Exemplo: A M" << endl;
    cin >> A[i] >> M[i];
    Y *= M[i];
  }

  cout <<"A M B B' K ABK" << "\n";

  for(int j = 0 ; j < qtd ; ++j){
    B[j] = int(Y / M[j]);
    B2[j] = B[j] % M[j];
    K[j] = imod(B2[j], M[j]);
    ABK[j] = A[j] * B[j] * K[j];
    cout << A[j] << " " << M[j] << " " 
    << B[j] << " "<< B2[j] << " " <<
     K[j]<< " " << ABK[j] << endl;
    Soma += ABK[j]; 
  }
  cout << endl;
  cout << "Y = " << Y << endl;
  cout << "Soma = " << Soma << endl;
  cout << "Resultado = " << Soma % Y << endl;
};
