/*
 * To compile with windows -lfreeglut -lglu32 -lopengl32
 * To compile linux -lglut -lGL -lGLU -lm 
 */
#include <GL/freeglut.h>  // ou glut.h - GLUT, include glu.h and gl.h
#include <math.h>
#include <stdio.h>
 /* Initialize OpenGL Graphics */
void init() {
   // Set "clearing" or background color
    glClearColor(0, 0, 0, 1); // Black and opaque
}
/* Handler for window-repaint event. Call back when the window first appears and
   whenever the window needs to be re-painted. */
void display() {
   glClear(GL_COLOR_BUFFER_BIT);         // Clear the color buffer (background)
   
   //draw objects//
   
   glFlush();  // Render now
}



/* Handler for window re-size event. Called back when the window first appears and
   whenever the window is re-sized with its new width and height */
void reshape(GLsizei width, GLsizei height) {  // GLsizei for non-negative integer
   // Compute aspect ratio of the new window
}
 
/* Main function: GLUT runs as a console application starting at main() */
int main(int argc, char** argv) {
   glutInit(&argc, argv);          // Initialize GLUT
   
   glutInitWindowSize(480, 480);   // Set the window's initial width & height - non-square
   glutInitWindowPosition(50, 50); // Position the window's initial top-left corner
   glutCreateWindow("Window");  // Create window with the given title
   
   glutDisplayFunc(display);       // Register callback handler for window re-paint event
   glutIdleFunc(display);
   glutReshapeFunc(reshape);       // Register callback handler for window re-size event
   
   init();                          // Our own OpenGL initialization
   glutMainLoop();                 // Enter the infinite event-processing loop
   return 0;
}
