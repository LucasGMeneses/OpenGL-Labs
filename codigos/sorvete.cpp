/*
 * Aluno: Lucas Gomes Meneses - RGA.: 201819040739 
 * sorvete.cpp: Test OpenGL/GLUT C/C++ Setup
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
// cria a casquinha do sorvete
void casquinha(){
	glColor3f(1, 1, 0); //
	glBegin(GL_TRIANGLES);
	   glVertex2f(0, -0.5);
	   glVertex2f(0.2, 0.2);
	   glVertex2f(-0.2, 0.2);
   glEnd();
}

void sorvete(float raio, float cx, float cy, float cor[] ){
   float ang, x, y;

  glColor3f(cor[0], cor[1], cor[2]);
  // glColor3d(7, 163, 90);
   glBegin(GL_POLYGON);
      for(int i=0; i<=360; i++){
         ang = (i * M_PI) / 180.0; //tranforma em radianos o angulo
         x = cx + (cos(ang) * raio);
         y = cy + (sin(ang)* raio);

         glVertex2f(x,y);
      }
   glEnd();

}
/* Handler for window-repaint event. Call back when the window first appears and
   whenever the window needs to be re-painted. */
void display() {
   glClear(GL_COLOR_BUFFER_BIT);         // Clear the color buffer (background)
   float cor[3]  = {1, 1, 1}; //branco
   float ct[3]   = {0, 0, 0};
   casquinha();
   sorvete(0.17, 0.2,0.2, cor);
   sorvete(0.17, -0.2, 0.2, cor);
   sorvete(0.25, 0, 0.3, cor);
   sorvete(0.17,0.9,0.9, ct);
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
   glutCreateWindow("Sorvete");  // Create window with the given title
   
   glutDisplayFunc(display);       // Register callback handler for window re-paint event
   glutIdleFunc(display);
   glutReshapeFunc(reshape);       // Register callback handler for window re-size event
   
   init();                       // Our own OpenGL initialization
   glutMainLoop();                 // Enter the infinite event-processing loop
   return 0;
}
