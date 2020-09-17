/*
 * Estrela de 5 a 20 pontas
 * To compile with windows -lfreeglut -lglu32 -lopengl32
 * To compile linux -lglut -lGL -lGLU -lm 
 */
#include <GL/freeglut.h>
#include <math.h>
#include <stdio.h>

float red[] = {1,0,0};   // vermelho
float green[] = {0,1,0}; // verde
float blue[] = {0,0,1};  // blue

// seleciona a cor
void set_color(float color[]){
   glColor3f(color[0], color[1], color[2]);
}

void init() {
   
    glClearColor(0, 0, 0, 1);
}

void display() {

   glClear(GL_COLOR_BUFFER_BIT);
   //draw objects//
   
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
