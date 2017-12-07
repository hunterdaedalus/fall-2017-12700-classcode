#include <iostream>

using std::cout;
using std::endl;

int f(int a[], int size){
  a[2]=54321;
  return a[1];
}

int main()
{
  int a;
  int data[4] = {5,2,5,22};
  int b;
  cout << a << " " <<  b << endl;
  for (int i = 0; i < 4; ++i) {
    cout << i << " : " << data[i] << endl;
  }

  for (int i = 0 ; i < 4; ++i) {
    data[i] = i*100+5;
  }

  for (int i = 0; i < 4; ++i) {
    cout << i << " : " << data[i] << endl;
  }

  
    for (int i = 0; i < 4; ++i) {
    cout << i << " : " << data[i] << endl;
  }

    cout << "\n------------------\n\n";
    a=12345;
    b=54321;


    for (int i = -5; i < 9; ++i) {
    cout << i << " : " << data[i] << endl;
    }
    cout << "\n------------------\n\n";


    
    data[-2]=99999;
    data[-1]=88888;
   for (int i = -5; i < 9; ++i) {
    cout << i << " : " << data[i] << endl;
    }

   cout << "a : " << a << " b : " << b << endl;

   cout << "\n\n------------------\n\n";

   int x = f(data,4);
   cout << "x : " << x << endl;
   for (int i = 0; i < 4; ++i) {
    cout << i << " : " << data[i] << endl;
    }

   return 0;
}
