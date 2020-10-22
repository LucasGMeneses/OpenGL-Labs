/*
 * To compile with windows -lfreeglut -lglu32 -lopengl32
 * To compile linux -lglut -lGL -lGLU -lm 
 */
#include <GL/freeglut.h>  // ou glut.h - GLUT, include glu.h and gl.h
#include <stdio.h>

float size = 6;

GLfloat matrix[16]; // matriz de transformacao

// imprime a matriz de transformacao
void printMatrix(){
   glGetFloatv(GL_MODELVIEW_MATRIX, matrix); 
   for (int i = 0; i < 16; i=i+4){
      printf("%f %f %f %f\n",matrix[i], matrix[i+1], matrix[i+2], matrix[i+3]);
   }
   printf("\n");
}

 /* Initialize OpenGL Graphics */
void init() {
   // Set "clearing" or background color
    glClearColor(0, 0, 0, 1); // Black and opaque
}

void square(){
   glColor3f(1,0,0);
   
   glBegin(GL_QUADS);
      glVertex2f(0, 0);
      glVertex2f(0, 1);
      glVertex2f(2, 1); 
      glVertex2f(2, 0); 
   glEnd();
}

void display() {
   glClear(GL_COLOR_BUFFER_BIT);         // Clear the color buffer (background)
   
    // transladando para (1,1)
   glTranslatef(1,1,0);

   // rotacionando 
   glRotatef(90,0,0,1);
   square();

   printMatrix();

   glFlush();  // Render now
}



/* Handler for window re-size event. Called back when the window first appears and
   whenever the window is re-sized with its new width and height */
void reshape(GLsizei width, GLsizei height) {  // GLsizei for non-negative integer
   	  glMatrixMode(GL_PROJECTION);
      glOrtho(-size, size, -size, size, 0, size);

      glMatrixMode(GL_MODELVIEW);
      glLoadIdentity();
}
 
/* Main function: GLUT runs as a console application starting at main() */
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
