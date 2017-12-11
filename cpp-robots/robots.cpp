#include <iostream>
#include <cstdlib>
#include <ctime>
#include <unistd.h>

#define ROWS 15
#define COLS 60

void make_empty_board(char b[ROWS][COLS]){
  int i,j;
  for (i = 0; i < ROWS; i++) {
    for (j=0; j < COLS; j++) {
      b[i][j]='.';
    }
  }
}
void print_board(char b[ROWS][COLS]){
  int i,j;
  // this moves the cursor to 0,0
  // the upper left corner of the screen
  std::cout << "[0;0H"; 

  for (i = 0; i < ROWS; i++) {
    for (j=0; j < COLS; j++) {
      std::cout << b[i][j];
    }
      std::cout << std::endl;
  }
    std::cout << std::endl;
}

void clear_screen(){
  std::cout << "[2J";
}

void add_robots(char b[ROWS][COLS],int count){
  int i;
  int r,c;
  for (i = 0; i < count; i++) {
    r = rand()%ROWS;
    c = rand()%COLS;
    b[r][c]='r';
  }
}

int main(){
  char b[ROWS][COLS];
  int i,j;
  int pr,pc;
  std::string s="";
  
  srand(time(0));
  make_empty_board(b);
  add_robots(b,10);
  pr = rand()%ROWS;
  pc = rand()%COLS;
  int opr, opc;
  b[pr][pc]='X';
  clear_screen();


  while (s[0] != 'q'){
    print_board(b);
    std::cout << "Enter move (u,d,l,r,t,q):";
    std::getline(std::cin,s);
    std::cout << "You entered: " << s << std::endl;
    /*
      All your code for this project
      should go here. 

      You have the input string in s, you
      just have to compare s[0] with each
      of the input characters and decide 
      what to do and then after that code
      add the robot code (also in here)
    */
    opr = pr;
    opc = pc;
    if (s[0]=='u' and pr>0)
      pr--;
    else if (s[0]=='d' and pr < ROWS-1)
      pr++;
    else if (s[0]=='l' and pc>0)
      pc--;
    else if (s[0]=='r' and pc< COLS-1)
      pc++;
    else if (s[0]=='t'){
      pr = rand()%ROWS;
      pc = rand()%COLS;
    }
    b[opr][opc]='.';
    b[pr][pc]='X';
  


    char b2[ROWS][COLS];
    make_empty_board(b2);
    /* copy the board robots over */
    for (i=0;i<ROWS;i++){
      for (j=0; j<COLS;j++) {
	if (b[i][j]=='r'){
	  b2[i][j]='r';
	  b[i][j]='.';
	}
      }
    }
    int dr=0,dc=0;
    int tr,tc;
    for (i=0;i<ROWS;i++){
      for (j=0; j<COLS;j++) {
        if (b2[i][j]=='r'){
          if (pr > i)
	    dr = 1;
	  else if (pr <i )
	    dr = -1;
          if (pc > j)
	    dc = 1;
	  else if (pc <j )
	    dc = -1;
	  tr = i + dr;
	  tc = j + dc;

	  if (b[tr][tc]=='X'){
	    std::cout << "BOOOOM!!!!!!"<<std::endl;
	    return 0;
	  }
	  if (b2[tr][tc]=='r'){
	    b2[tr][tc]='.';
	  }else {
	    b[tr][tc]='r';
	  }
	  
	  
	  

	}
      }
    }
    
  }
}





