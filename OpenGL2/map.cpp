
#include <GL/freeglut.h> 
#include <stdio.h>


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
   glColor3f(1,0,0);
   //telhado
   glBegin(GL_POLYGON);
      glVertex2f(x, hr);
      glVertex2f(x+w,hr);
      glVertex2f(x+(w/2), y); 
   glEnd();

   //parede
   glColor3f(0,0,1);
   square(x+(w/4),hr,w/2,h/3);
}
//poligono                  //largura  altura
void poly(float x, float y, float w, float h){
   glBegin(GL_POLYGON);
      glVertex2f(x+(w/2), y-h);
      glVertex2f(x+w,y-h);
      glVertex2f(x+w, y); 
      glVertex2f(x, y);
      glVertex2f(x, y-(h/2));
   glEnd();
}
//ruas
void streets(){
   
   glColor3f(1, 1, 1);
   square(-1.0f,0.5f,2.0f,1.5f);
}

void blocks(){
   float aux = 0.05f;
   float stw = 0.93f; 
   float sth = 0.20f;

   glColor3f(0.8,0.8,0.8);
   float temp;
   for (int i = 0; i < 4; i++){
     temp =(-aux - sth) * i;
     square(-1+aux,0.45f+temp,stw,sth);
     if(i == 0){
        glColor3f(0,0.8,0);
     }
     square(-1+aux+stw+aux,0.45f+temp,stw,sth);
     glColor3f(0.8,0.8,0.8);
   }
   
   temp = (-aux - sth) * 4;
   float pw = 0.3f; //poly largura
   float ph = 0.3f;// poly altura
   poly(-1+aux,0.45f+temp,pw,ph);
   
   square((-1+aux)+pw+aux,0.45f+temp, stw-aux-pw, (ph/2.5f));
   square((-1+aux)+pw+aux,0.45f+temp-0.18f, stw-aux-pw, (ph/2.5f));

   square(-1+aux+stw+aux,0.45f+temp,stw, (ph/2.5f));
   square(-1+aux+stw+aux,0.45f+temp-0.18f,stw, (ph/2.5f));

}
void init() {
   float temp = 0.7f;
    glClearColor(temp, temp, temp, 1); // Black and opaque
}


void display() {
   glClear(GL_COLOR_BUFFER_BIT);        
   
   streets();
   blocks();
   home(0.65f,0.34f,0.1f,0.1f);
   glFlush(); 
}



void reshape(GLsizei width, GLsizei height) {
   
}
 

int main(int argc, char** argv) {
   glutInit(&argc, argv);          
   
   glutInitWindowSize(480, 480);   
   glutInitWindowPosition(50, 50); 
   glutCreateWindow("Window");  
   
   glutDisplayFunc(display);      
   glutIdleFunc(display);
   glutReshapeFunc(reshape); 

   init();                  
   glutMainLoop();                 
   return 0;
}
