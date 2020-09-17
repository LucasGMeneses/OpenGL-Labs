
#include <GL/freeglut.h> 
#include <math.h>
#include <stdio.h>

void street(float x0, float y0, float x1, float y1){
   glColor3f(1, 1, 1);

   glBegin(GL_LINES);
      glVertex2f(x0,y0);
      glVertex2f(x1,y1);
   glEnd();
}
void init() {
   float temp = 0.7;
    glClearColor(temp, temp, temp, 1); // Black and opaque
}


void display() {
   glClear(GL_COLOR_BUFFER_BIT);        
   
   street(0,0,1,1);
   
   glFlush(); 
}



void reshape(GLsizei width, GLsizei height) {
   
}
 

int main(int argc, char** argv) {
   glutInit(&argc, argv);          
   
   glutInitWindowSize(480, 480);   
   glutInitWindowPosition(50, 50); 
   glutCreateWindow("Window");  
   
   glutDisplayFunc(display);      
   glutIdleFunc(display);
   glutReshapeFunc(reshape); 

   init();                  
   glutMainLoop();                 
   return 0;
}
