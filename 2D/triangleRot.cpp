/*
 * To compile with windows -lfreeglut -lglu32 -lopengl32
 * To compile linux -lglut -lGL -lGLU -lm 
 */
#include <GL/freeglut.h>  // ou glut.h - GLUT, include glu.h and gl.h
#include <math.h>
#include <stdio.h>
//GLfloat triangle[] = {};
float green[] = {0,1,0}; // verde

void set_color(float color[]){
   glColor3f(color[0], color[1], color[2]);
}
void triangle(float x0, float y0, float x1, float y1, float x2, float y2, float color[]){
   set_color(color);
   glBegin(GL_TRIANGLES);
      glVertex2f(x0,y0);
      glVertex2f(x1,y1);
      glVertex2f(x2,y2);
  glEnd();
}

void init() {
  
    glClearColor(0, 0, 0, 1);
}

void display() {
   glClear(GL_COLOR_BUFFER_BIT); 
   
   //draw objects//
   triangle(0,0,1,0,0.5f,1,green);

   glFlush();  // Render now
}



void reshape(GLsizei width, GLsizei height) {  

}
 
/* Main function: GLUT runs as a console application starting at main() */
int main(int argc, char** argv) {
   glutInit(&argc, argv);          // Initialize GLUT
   
   glutInitWindowSize(480, 480);   // Set the window's initial width & height - non-square
   glutInitWindowPosition(50, 50); // Position the window's initial top-left corner
   glutCreateWindow("Rotation");  // Create window with the given title
   
   glutDisplayFunc(display);       // Register callback handler for window re-paint event
   glutIdleFunc(display);
   glutReshapeFunc(reshape);       // Register callback handler for window re-size event
   
   init();                          // Our own OpenGL initialization
   glutMainLoop();                 // Enter the infinite event-processing loop
   return 0;
}
