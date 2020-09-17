/*
 * To compile with windows -lfreeglut -lglu32 -lopengl32
 * To compile linux -lglut -lGL -lGLU -lm 
 */
#include <GL/freeglut.h>  
#include <math.h>
#include <stdio.h>

GLfloat win = 1;         // variavel que usaremos pra escalonar a area de trabalho
float red[] = {1,0,0};   // vermelho
float green[] = {0,1,0}; // verde
float blue[] = {0,0,1};  // blue

// seleciona a cor
void set_color(float color[]){
   glColor3f(color[0], color[1], color[2]);
}

//triangulo
void triangle(float x0, float y0, float x1, float y1, float x2, float y2, float color[]){
   set_color(color);
   glBegin(GL_TRIANGLES);
      glVertex2f(x0,y0);
      glVertex2f(x1,y1);
      glVertex2f(x2,y2);
  glEnd();
}

//retangulo                   //largura  altura
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
   
   
   //eixo y
   set_color(green); 
   glBegin(GL_LINES);
      glVertex2f(0,-win);
      glVertex2f(0,win);
   glEnd();

   //eixo x
   set_color(red); 
   glBegin(GL_LINES);
      glVertex2f(-win,0);
      glVertex2f(win,0);
   glEnd();
}

void init() {
   
    glClearColor(0, 0, 0, 1); // fundo preto
}

void display() {

   glClear(GL_COLOR_BUFFER_BIT);  //limpa a tela
      square(-0.5f, 0.5f, 0.3f, 0.3f, red);
      triangle(0.1f, -0.3f, 0.5f, -0.3f, 0.3f, -0.1f, blue);
      circle(0.2f, -0.5f, -0.6f, green);
      axis();
   glFlush(); //renderiza a proxima cena
}

void mouse_event(int button, int state, int x, int y){
   if(button == GLUT_LEFT_BUTTON){ // botao do mouse esquerdo
      
      if(state == GLUT_DOWN){ // se for presionado
         win++;
         // fazendo a mudanca de projecao
         // zoom in
         glMatrixMode(GL_PROJECTION);
         glLoadIdentity();
         gluOrtho2D(-win,win,-win,win);
      }
   }

   if(button == GLUT_RIGHT_BUTTON){ // botao do mouse direito
      
      if(state == GLUT_DOWN){ //se for precionado
        if(win > 1){
            win--;
            // efeito zoom out
            glMatrixMode(GL_PROJECTION);
            glLoadIdentity();
            gluOrtho2D(-win,win,-win,win);
        } 

         
      }
   }
   glutPostRedisplay();
}

void reshape(GLsizei width, GLsizei height) { 

}

int main(int argc, char** argv) {
   glutInit(&argc, argv);          
    
   //config da janela
   glutInitWindowSize(480, 480);   
   glutInitWindowPosition(50, 50); 
   glutCreateWindow("Zoom Object"); 
   
   glutDisplayFunc(display);       
   glutIdleFunc(display);
   glutReshapeFunc(reshape);       
   glutMouseFunc(mouse_event);

   init();                          
   glutMainLoop();    //loop
   return 0;
}
