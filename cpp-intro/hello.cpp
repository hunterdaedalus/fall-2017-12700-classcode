#include <iostream>
#include <iomanip> 
// This is a single line comment

/* 
   return_type name(parameters){
   // the body of the function
   return something;
   }
*/



int main(){
  int i;
  double d1,d2;
  char c = 'c';
  
  
  d1 = 123.45678;
  
  i = 7;
  d2 = i;
  std::cout << "Hellod!\n";
  std::cout << "i = " << i << std::endl;
  std::cout << i / 2 << "\n";
  std::cout << d2 << " " << d2/2 << std::endl;
  i = d2 / 2;
  std::cout << i  << "\n";
  std::cout << d1 << std::endl;
  std::cout << std::setprecision(2) << d1 << std::endl;
  std::cout << c << '\n';
  std::cout << "Enter a number:";
  std::cin >> i;
  std::cout << "You entered: " << i << std::endl;
  return 0;
}
