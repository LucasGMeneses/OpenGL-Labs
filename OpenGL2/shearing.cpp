/*
 * To compile with windows -lfreeglut -lglu32 -lopengl32
 * To compile linux -lglut -lGL -lGLU -lm 
 */
#include <GL/freeglut.h>
#include <math.h>
#include <stdio.h>
GLfloat matrix[16];
GLfloat shear[] = {
   1,0,0,0,
   0.3f,1,0,0,
   0,0,1,0,
   0,0,0,1
};
// imprime a matriz de transformacao
void printMatrix(){
   glGetFloatv(GL_MODELVIEW_MATRIX, matrix); 
   for (int i = 0; i < 16; i=i+4){
      printf("%f %f %f %f\n",matrix[i], matrix[i+1], matrix[i+2], matrix[i+3]);
   }
   printf("\n");
}
//retangulo                   //largura  altura
void square(float x, float y, float w, float h){
   glBegin(GL_POLYGON);
      glVertex2f(x, y-h);
      glVertex2f(x+w,y-h);
      glVertex2f(x+w, y); 
      glVertex2f(x, y); 
   glEnd();
}
//casa                   //largura  altura
void home(float x, float y, float w, float h){
   float hr = y-(h/2);
   //parede
   glColor3f(0,0,1);
   square(x,hr,w,h/3);

   //telhado
   glColor3f(1,0,0);
   glBegin(GL_POLYGON);
      glVertex2f(x, hr);
      glVertex2f(x+w,hr);
      glVertex2f(x+(w/2), y); 
   glEnd();


}

 /* Initialize OpenGL Graphics */
void init() {
   // Set "clearing" or background color
   glClearColor(0, 0, 0, 1); // Black and opaque
   glMultMatrixf(shear);
   printf("== MATRIZ MODEL_VIEW ==\n");
   printMatrix();
}

void display() {
   glClear(GL_COLOR_BUFFER_BIT);         // Clear the color buffer (background)
  
   home(0,0,0.5,0.5);
   
   glFlush();  // Render now
}


void reshape(GLsizei width, GLsizei height) { 

}


int main(int argc, char** argv) {
   glutInit(&argc, argv);          // Initialize GLUT
   
   glutInitWindowSize(480, 480);   // Set the window's initial width & height - non-square
   glutInitWindowPosition(50, 50); // Position the window's initial top-left corner
   glutCreateWindow("Shearing");  // Create window with the given title
   
   glutDisplayFunc(display);       // Register callback handler for window re-paint event
   glutIdleFunc(display);
   glutReshapeFunc(reshape);       // Register callback handler for window re-size event
   
   init();                          // Our own OpenGL initialization
   glutMainLoop();                 // Enter the infinite event-processing loop
   return 0;
}
