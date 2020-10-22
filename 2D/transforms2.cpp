/*
 * To compile with windows -lfreeglut -lglu32 -lopengl32
 * To compile linux -lglut -lGL -lGLU -lm 
 */
#include <GL/freeglut.h>  
#include <math.h>
#include <stdio.h>

GLfloat matrix[16]; // matriz de transformacao
float size = 3;
float white[] = {1,1,1}; // branco

// seleciona a cor
void setColor(float color[]){
   glColor3f(color[0], color[1], color[2]);
}
// imprime a matriz de transformacao
void printMatrix(){
   glGetFloatv(GL_MODELVIEW_MATRIX, matrix); 
   for (int i = 0; i < 16; i=i+4){
      printf("%f %f %f %f\n",matrix[i], matrix[i+1], matrix[i+2], matrix[i+3]);
   }
   printf("\n");
}

void triangle(float x0, float y0, float x1, float y1, float x2, float y2, float color[]){
   setColor(color);
   glBegin(GL_TRIANGLES);
      glVertex2f(x0,y0);
      glVertex2f(x1,y1);
      glVertex2f(x2,y2);
  glEnd();
}

void darkening(){
   white[0]-=0.2f;
   white[1]-=0.2f;
   white[2]-=0.2f;
}

 /* Initialize OpenGL Graphics */
void init() {

    glClearColor(0, 0, 0, 1); // Black and opaque
}

void display() {
   glClear(GL_COLOR_BUFFER_BIT);
   // trianglulo original
   triangle(0,0,1,0,0.5,1,white);
   // transladando para (1,1)
   glTranslatef(1,1,0);

   // rotacionando 
   glRotatef(30,0,0,1);

   // triangulo transformado
   darkening(); // deixar um pouco mais cinza
   triangle(0,0,1,0,0.5,1,white);
   
   //imprime matriz
   printMatrix();
   glFlush(); 
}


void reshape(GLsizei width, GLsizei height) { 

      glMatrixMode(GL_PROJECTION);
      glOrtho(-size, size, -size, size, 0, size);

      glMatrixMode(GL_MODELVIEW);
      glLoadIdentity();
}

int main(int argc, char** argv) {
   glutInit(&argc, argv);          // Initialize GLUT
   
   glutInitWindowSize(480, 480);   // Set the window's initial width & height - non-square
   glutInitWindowPosition(50, 50); // Position the window's initial top-left corner
   glutCreateWindow("Triangle5");  // Create window with the given title
   
   glutDisplayFunc(display);       // Register callback handler for window re-paint event
   glutReshapeFunc(reshape);       // Register callback handler for window re-size event
   init();                          // Our own OpenGL initialization
   glutMainLoop();                 // Enter the infinite event-processing loop
   return 0;
}
