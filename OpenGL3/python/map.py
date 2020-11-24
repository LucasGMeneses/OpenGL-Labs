import sys
import numpy as np

from OpenGL.GL import *
from OpenGL.GL import shaders
from OpenGL.GLUT import *

vao = None
vbo = None
shaderProgram = None

colors = {
	'streets': [1.0, 1.0, 1.0], # ruas
	'blocks' : [0.8, 0.8, 0.8], # blocos
	'roof'   : [1.0, 0.0, 0.0], # telhado
	'wall'   : [0.0, 0.0, 1.0], # parede
	'bHouse'  :[0.0, 0.8, 0.0]  # bloco da casa
}
# gera quadrados
def square(x, y, w, h, vet):
	vet.append([x, y-h, 0.0])
	vet.append([x+w, y-h, 0.0])
	vet.append([x+w, y, 0.0])
	vet.append([x, y, 0.0])

# gera a figura da casa
def home(x, y, w, h, vet):
	hr = y-(h/2)
	# telhado
	vet.append([x, hr, 0.0])
	vet.append([x+w, hr, 0.0])
	vet.append([x+(w/2), y, 0.0])
	# parede
	square(x+(w/4), hr, w/2, h/3, vet)

# gera o poligono de 5 vertices
def poly(x, y, w, h, vet):
	vet.append([x+(w/2), y-h, 0.0])
	vet.append([x+w, y-h, 0.0])
	vet.append([x+w, y, 0.0])
	vet.append([x, y, 0.0])
	vet.append([x, y-(h/2), 0.0])

# gera os blocos
def blocks(vet):
	aux = 0.05
	stw = 0.93
	sth = 0.20

	temp = 0
	for i in range(4):
		temp = (-aux - sth) * i
		square(-1+aux+stw+aux,0.45+temp,stw,sth,vet)
		square(-1+aux,0.45+temp,stw,sth,vet)
	temp = (-aux - sth) * 4
	pw = 0.3
	ph = 0.3

	square((-1+aux)+pw+aux,0.45+temp, stw-aux-pw, (ph/2.5),vet)
	square((-1+aux)+pw+aux,0.45+temp-0.18, stw-aux-pw, (ph/2.5),vet)
	square(-1+aux+stw+aux,0.45+temp,stw, (ph/2.5),vet)
	square(-1+aux+stw+aux,0.45+temp-0.18,stw, (ph/2.5),vet)
	poly(-1+aux,0.45+temp,pw,ph,vet)

# le os shaders
def readShaderFile(filename):
	with open('shader/' + filename, 'r') as myfile:
		return myfile.read()

def init():
	global shaderProgram
	global vao
	global vbo
	
	glClearColor(0.7, 0.7, 0.7, 1)
	
	vertex_code = readShaderFile('map.vp')
	fragment_code = readShaderFile('map.fp')

	# compile shaders and program
	vertexShader = shaders.compileShader(vertex_code, GL_VERTEX_SHADER)
	fragmentShader = shaders.compileShader(fragment_code, GL_FRAGMENT_SHADER)
	shaderProgram = shaders.compileProgram(vertexShader, fragmentShader)
	
	# Create and bind the Vertex Array Object
	vao = GLuint(0)
	glGenVertexArrays(1, vao)
	glBindVertexArray(vao)

	# Create and bind the Vertex Buffer Object
	vertices = np.array([[0, 0, 0, 0, 0, 1], [-1, -1, 0, 1, 1, 0], [1, -1, 0, 0, 1, 0]], dtype='f')

	vet = []
	square(-1.0,0.5,2.0,1.5,vet) # streets
	blocks(vet)
	home(0.65,0.34,0.1,0.1,vet)
	vertices = np.array(vet,dtype='f')

	vbo = glGenBuffers(1)
	glBindBuffer(GL_ARRAY_BUFFER, vbo)
	glBufferData(GL_ARRAY_BUFFER, vertices, GL_STATIC_DRAW)
	glVertexAttribPointer(0, 3, GL_FLOAT, False, 3 * sizeof(GLfloat), ctypes.c_void_p(0))  # first 0 is the location in shader

	glEnableVertexAttribArray(0);  # 0=location do atributo, tem que ativar todos os atributos inicialmente sao desabilitados por padrao
	
	# Note that this is allowed, the call to glVertexAttribPointer registered VBO
	# as the currently bound vertex buffer object so afterwards we can safely unbind
	glBindBuffer(GL_ARRAY_BUFFER, 0)
	# Unbind VAO (it's always a good thing to unbind any buffer/array to prevent strange bugs)
	glBindVertexArray(0)

def display():
	global shaderProgram
	global vao
	
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
	
	# load everthing back
	glUseProgram(shaderProgram)
	glBindVertexArray(vao)
	glBindBuffer(GL_ARRAY_BUFFER, vbo)
	idColor = glGetUniformLocation(shaderProgram,'uColor')
	# desenha ruas
	glUniform3fv(idColor,1, colors['streets'])
	glDrawArrays(GL_QUADS, 0, 4)
	
	# desenha bloco da casa
	glUniform3fv(idColor,1, colors['bHouse'])
	glDrawArrays(GL_QUADS, 4, 4)

	# desenha blocos das ruas
	glUniform3fv(idColor,1, colors['blocks'])
	glDrawArrays(GL_QUADS, 8, 11 * 4)

	glUniform3fv(idColor,1, colors['blocks'])
	glDrawArrays(GL_POLYGON, 52, 5)

	# desenha a casa
	glUniform3fv(idColor,1, colors['roof'])
	glDrawArrays(GL_TRIANGLES, 57, 3)
	glUniform3fv(idColor,1, colors['wall'])
	glDrawArrays(GL_QUADS, 60, 4)

	#clean things up
	glBindBuffer(GL_ARRAY_BUFFER, 0)
	glBindVertexArray(0)
	glUseProgram(0)
	
	glutSwapBuffers()  # necessario para windows!

def reshape(width, height):
	glViewport(0, 0, width, height)

if __name__ == '__main__':
	glutInit(sys.argv)
	glutInitContextVersion(3, 0)
	glutInitContextProfile(GLUT_CORE_PROFILE);
	glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
	
	glutInitWindowSize(640, 640);
	glutCreateWindow(b'Map')
	
	glutReshapeFunc(reshape)
	glutDisplayFunc(display)

	init()
	
	glutMainLoop()
