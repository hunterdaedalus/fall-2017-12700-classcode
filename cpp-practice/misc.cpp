#include <iostream>
#include <cstdlib>
#include <ctime>
#include <string>

using std::cout;
using std::endl;




int main()
{
  cout << time(0) << endl;
  srand(time(0));
  for (int i = 0; i < 10; ++i) {
    cout << rand()%10 << endl;
  
  }
  std::string s = "Hello World";
  std::string s2;

  cout << s << endl;
  s2 = s + " " + s;
  cout << s2 << endl;
  cout << s2[3] << endl;
  std::string s3;
  s3 = s2.substr(3,5);
  cout << s3 << endl;
  cout << (s2 < s3) << endl;
  return 0;
}
