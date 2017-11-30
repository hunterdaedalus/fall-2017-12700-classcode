#include <iostream>


int main()
{
  int a;
  a = 2;
  if (a>5){
    std::cout << "A is greater than 5\n";
    std::cout << "Another line\n";
  } else {
    std::cout << "This is the else stuff\n";
  }

  int i = 0;
  while (i<10){
    std::cout << i << std::endl;
    i++;
  }
  
  std::cout << "A third line\n";

  i = 0; // initializatoin
  while (i< 10) { // i < 10 is the test
    std::cout << "stuff";
    i=i+1; // change i 
  }

  std::cout << std::endl;
  /*
  for (init ; test ; change) {
    
  }
  */
  for (i = 0; i < 10; i=i+1) {
    std::cout << i << std::endl;
  }

  
  return 0;
}

