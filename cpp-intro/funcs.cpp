#include <iostream>


/*
def addtwo(a,b):
  return a+b;
*/

int addtwo(int a,int b){
  int sum;
  sum =  a + b;
  return sum;
}

void printStuff(){
  std::cout << "This is printing stuff\n";
}

int addOne(int x){
x=x+1;
return x;
}
		  
int main()
{
  int i = 20;
  int j = 330;
  int x;
  x = addtwo(i,j);
  std::cout << "The sum of " << i << " + " << j << " = " << x;
  std::cout << std::endl;
  printStuff();
  std::cout << x << std::endl;
  x = addOne(x);
  std::cout << x << std::endl;
  
  return 0;
}
