/*
 * To compile with windows -lfreeglut -lglu32 -lopengl32
 * To compile linux -lglut -lGL -lGLU -lm 
 */
#include <GL/freeglut.h>  
#include <math.h>
#include <stdio.h>
 /* Initialize OpenGL Graphics */
void init() {

    glClearColor(0, 0, 0, 1); // Black and opaque
}

void display() {
   glClear(GL_COLOR_BUFFER_BIT);         
   
   
   
   glFlush(); 
}


void reshape(GLsizei width, GLsizei height) {  
   
}

int main(int argc, char** argv) {
   glutInit(&argc, argv);          // Initialize GLUT
   
   glutInitWindowSize(480, 480);   // Set the window's initial width & height - non-square
   glutInitWindowPosition(50, 50); // Position the window's initial top-left corner
   glutCreateWindow("Window");  // Create window with the given title
   
   glutDisplayFunc(display);       // Register callback handler for window re-paint event
   glutReshapeFunc(reshape);       // Register callback handler for window re-size event
   
   init();                          // Our own OpenGL initialization
   glutMainLoop();                 // Enter the infinite event-processing loop
   return 0;
}
