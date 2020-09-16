/*
 * To compile with windows -lfreeglut -lglu32 -lopengl32
 * To compile linux -lglut -lGL -lGLU -lm 
 */
#include <GL/freeglut.h>  
#include <math.h>
#include <stdio.h>

// seleciona a cor
void set_color(float color[]){
   glColor3f(color[0], color[1], color[2]);
}

//triangulo
void triangle(float x0, float y0, float x1, float y1, float x2, float y2, float color[]){
   set_color(color);
}

//quadrado                    //largura  altura
void square(float x, float y, float w, float h, float color[]){
   set_color(color);
   glBegin(GL_QUADS);
      glVertex2f(x, y-h);
      glVertex2f(x+w,y-h);
      glVertex2f(x+w, y); 
      glVertex2f(x, y); 
   glEnd();
}

//circulo
void circle(float raio, float cx, float cy, float color[] ){
   float ang, x, y;

  set_color(color);
   glBegin(GL_POLYGON);
      for(int i=0; i<=360; i++){
         ang = (i * M_PI) / 180.0; //tranforma em radianos o angulo
         x = cx + (cos(ang) * raio);
         y = cy + (sin(ang)* raio);

         glVertex2f(x,y);
      }
   glEnd();
}
//eixos
void axis(){
   float red[] = {1,0,0};
   float green[] = {0,1,0};
   
   //eixo y
   set_color(green); 
   glBegin(GL_LINES);
      glVertex2f(0,-1);
      glVertex2f(0,1);
   glEnd();

   //eixo x
   set_color(red); 
   glBegin(GL_LINES);
      glVertex2f(-1,0);
      glVertex2f(1,0);
   glEnd();
}
void init() {
   
    glClearColor(0, 0, 0, 1); // fundo preto
}

void display() {
   float red [] = {1,0,0};
   glClear(GL_COLOR_BUFFER_BIT);  //limpa a tela
   square(-0.5f, 0.5f, 0.3f, 0.3f, red);
   axis();
   glFlush(); //renderiza a proxima cena
}


void reshape(GLsizei width, GLsizei height) { 

}

int main(int argc, char** argv) {
   glutInit(&argc, argv);          
   
   //config da janela
   glutInitWindowSize(480, 480);   
   glutInitWindowPosition(50, 50); 
   glutCreateWindow("Window"); 
   
   glutDisplayFunc(display);       
   glutIdleFunc(display);
   glutReshapeFunc(reshape);       
   
   init();                          
   glutMainLoop();    //loop
   return 0;
}
