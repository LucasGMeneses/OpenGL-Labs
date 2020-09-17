/*
 * Estrela de 5 a 20 pontas
 * To compile with windows -lfreeglut -lglu32 -lopengl32
 * To compile linux -lglut -lGL -lGLU -lm 
 */
#include <GL/freeglut.h>
#include <math.h>
#include <stdio.h>

float color[] = {1,1,0};   // amarelo
int p = 5;                // numeros de pontas 
bool start = false;      // flag de controle da animacao (5 a 20 pontas)

// seleciona a cor
void set_color(float color[]){
   glColor3f(color[0], color[1], color[2]);
}

void star(float raio, float cx, float cy, int pt){
   float ang, x, y, ang1;

  set_color(color);
   pt = 360 / pt;
   
   glBegin(GL_POLYGON);
      for(int i=0; i<=360-pt; i+=pt){
         ang = (i * M_PI) / 180.0; //tranforma em radianos o angulo
         x = cx + (cos(ang) * raio);
         y = cy + (sin(ang) * raio);
         glVertex2f(x,y);
         
         // encontra o proximo ponto do poligono interno da estrela
         ang1 = ((i + pt) * M_PI) / 180.0; 
         
         float px = cx + (cos(ang1) * raio);
         float py = cy + (sin(ang1) * raio);
         // calculando o ponto medio
         float pmx = (x + px) / 2.0; 
         float pmy = (y + py) / 2.0;
         
         //angulo medio
         ang = (ang + ang1) / 2.0;
         
         pmx = pmx + (cos(ang) * raio);
         pmy = pmy + (sin(ang) * raio);
         glVertex2f(pmx,pmy);
      }
   glEnd();

}
void init() {
   
    glClearColor(0, 0, 0, 1);
}

void display() {

   glClear(GL_COLOR_BUFFER_BIT);

   star(0.2f,0,0,p);
   if(start == true){
       if(p < 20){
         p++;
      }
   }
   glFlush();
   //sleep(1);
}

void reshape(GLsizei width, GLsizei height) {  
   
}

void key_press(unsigned char key, int x, int y){
   // ENTER
   if(key == 13){
      start = true;
   }
   // ESC 
   if (key == 27){
      exit(0);
   }
}
 
int main(int argc, char** argv) {
   glutInit(&argc, argv);          
   
   glutInitWindowSize(480, 480);  
   glutInitWindowPosition(50, 50); 
   glutCreateWindow("Window");  
   
   glutDisplayFunc(display);       
   glutIdleFunc(display);
   glutReshapeFunc(reshape);       
   glutKeyboardFunc(key_press);

   init();                        
   glutMainLoop();                 
   return 0;
}
