import sys
import numpy as np

from OpenGL.GL import *
from OpenGL.GL import shaders
from OpenGL.GLUT import *

vao = None
vao2 = None
vbo = None
vbo2 = None
shaderProgram = None

def readShaderFile(filename):
	with open('shader/' + filename, 'r') as myfile:
		return myfile.read()

def init():
	global shaderProgram
	global vao
	global vao2
	global vbo
	global vbo2
	
	glClearColor(0, 0, 0, 0);
	
	vertex_code = readShaderFile('test.vp')
	fragment_code = readShaderFile('test.fp')

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
	vbo = glGenBuffers(1)
	glBindBuffer(GL_ARRAY_BUFFER, vbo)
	glBufferData(GL_ARRAY_BUFFER, vertices, GL_STATIC_DRAW)
	glVertexAttribPointer(0, 3, GL_FLOAT, False, 6 * sizeof(GLfloat), ctypes.c_void_p(0))  # first 0 is the location in shader
	glVertexAttribPointer(1, 3, GL_FLOAT, False, 6 * sizeof(GLfloat), ctypes.c_void_p(3*sizeof(GLfloat)))  # first 0 is the location in shader

	glEnableVertexAttribArray(0);  # 0=location do atributo, tem que ativar todos os atributos inicialmente sao desabilitados por padrao
	glEnableVertexAttribArray(1);  # 1=location do atributo, tem que ativar todos os atributos inicialmente sao desabilitados por padrao
	
	vao2 = GLuint(0)
	glGenVertexArrays(1, vao2)
	glBindVertexArray(vao2)
	# Create and bind the Vertex Buffer Object
	vertices = np.array([[0, 1, 0, 0, 0, 1], [-1, 0, 0, 1, 0, 0], [1, 0, 0, 0, 1, 0]], dtype='f')
	vbo2 = glGenBuffers(1)
	glBindBuffer(GL_ARRAY_BUFFER, vbo2)
	glBufferData(GL_ARRAY_BUFFER, vertices, GL_STATIC_DRAW)
	glVertexAttribPointer(0, 3, GL_FLOAT, False, 6 * sizeof(GLfloat), ctypes.c_void_p(0))  # first 0 is the location in shader
	glVertexAttribPointer(1, 3, GL_FLOAT, False, 6 * sizeof(GLfloat), ctypes.c_void_p(3*sizeof(GLfloat)))  # first 0 is the location in shader

	glEnableVertexAttribArray(0);  # 0=location do atributo, tem que ativar todos os atributos inicialmente sao desabilitados por padrao
	glEnableVertexAttribArray(1);  # 1=location do atributo, tem que ativar todos os atributos inicialmente sao desabilitados por padrao
	# Note that this is allowed, the call to glVertexAttribPointer registered VBO
	# as the currently bound vertex buffer object so afterwards we can safely unbind
	glBindBuffer(GL_ARRAY_BUFFER, 0)
	# Unbind VAO (it's always a good thing to unbind any buffer/array to prevent strange bugs)
	glBindVertexArray(0)

def display():
	global shaderProgram
	global vao
	global vao2
	glEnable(GL_DEPTH_TEST)
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
	
	# load everthing back
	glUseProgram(shaderProgram)
	glBindVertexArray(vao)
	glBindBuffer(GL_ARRAY_BUFFER, vbo)
	
	# glDrawArrays( mode , first, count)
	glDrawArrays(GL_TRIANGLES, 0, 3)

	glBindVertexArray(vao2)
	glBindBuffer(GL_ARRAY_BUFFER, vbo2)
	
	# glDrawArrays( mode , first, count)
	glDrawArrays(GL_TRIANGLES, 0, 3)

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
	glutCreateWindow(b'Hello world!')
	
	glutReshapeFunc(reshape)
	glutDisplayFunc(display)

	init()
	
	glutMainLoop()
