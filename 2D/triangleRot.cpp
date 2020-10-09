/*
 * Precione ESPACO p/ Rotacionar ou ESC para Sair
 *  To compile with windows -lfreeglut -lglu32 -lopengl32
 * To compile linux -lglut -lGL -lGLU -lm 
 */
#include <GL/freeglut.h>  // ou glut.h - GLUT, include glu.h and gl.h
#include <stdio.h>

GLfloat matrix[16]; // matriz de transformacao

float white[] = {1,1,1}; // branco
bool start = false;

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
//desenha  o triangulo
void triangle(float x0, float y0, float x1, float y1, float x2, float y2, float color[]){
   setColor(color);
   glBegin(GL_TRIANGLES);
      glVertex2f(x0,y0);
      glVertex2f(x1,y1);
      glVertex2f(x2,y2);
  glEnd();
}

void init() {
   printf("Precione ESPACO p/ Rotacionar ou ESC para Sair\n\n");
   glClearColor(0, 0, 0, 1);


}

void display() {
   glClear(GL_COLOR_BUFFER_BIT); 
   glPushMatrix();
   //draw objects//
   if(start == true){
      printf("Matriz Original\n");
      printMatrix();
      
      glTranslatef(0.5f,0.5f,0); // translada o eixo para a posicao(0.5,0.5)
      printf("Matriz dps da Translacao\n");
      printMatrix();
      
      glRotatef(90,0,0,1); // rotaciona 90 graus sentido anti horario no eixo z
      printf("Matriz dps da Rotacao\n");
      printMatrix();
      
      glTranslatef(-0.5f,-0.5f,0); // retorna o eixo para a posicao(0,0)
      printf("Matriz dps da translacao p/ origem\n");
      printMatrix();
      
   }
   triangle(0,0,1,0,0.5f,1,white);
   glPopMatrix();

   glFlush();  // Render now
}



void reshape(GLsizei width, GLsizei height) {  

}

void keyEvent(unsigned char key, int x, int y){
   switch (key){
   case 32: // ESPACO
      start = true;
      break;
   case 27: // ESCAPE
      exit(0);
   default:
      printf("Precione ESPACO p/ Rotacionar ou ESC para Sair\n\n");
      break;
   }
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
   glutKeyboardFunc(keyEvent);     // Eventos do teclado
   init();                         // Our own OpenGL initialization
   glutMainLoop();                 // Enter the infinite event-processing loop
   return 0;
}
