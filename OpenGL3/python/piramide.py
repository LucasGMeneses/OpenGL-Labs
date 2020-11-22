import sys
import numpy as np
import math 
from pyrr import matrix44, Vector3
from OpenGL.GL import *
from OpenGL.GL import shaders
from OpenGL.GLUT import *

vao = None
vbo = None
shaderProgram = None
piramide = {
	'vertices': np.array([
		[0.0, -0.5, -1.0,   0, 0, 1], 
		[0.0, 0.5, 0.0,     1, 0, 0], 
		[0.8, -0.5, 0.5,    0, 1, 0],
		[-0.8, -0.5, 0.5,   1, 0, 1]],
		dtype='f'),
	'faces': np.array([
		[0, 1, 2],
		[2, 1, 3],
		[3, 1, 0],
		[0, 1, 3],
		], dtype='i')
}
mvp = {
	'model': None,
	'view' : None,
	'projection': None,
	'idProj': None,
	'idView': None,
	'idMod': None,
}

def readShaderFile(filename):
	with open('shader/' + filename, 'r') as myfile:
		return myfile.read()

def init():
	global shaderProgram
	global vao
	global vbo	
	global mvp

	glClearColor(0, 0, 0, 0)
	
	vertex_code = readShaderFile('piramide.vp')
	fragment_code = readShaderFile('piramide.fp')

	# compile shaders and program
	vertexShader = shaders.compileShader(vertex_code, GL_VERTEX_SHADER)
	fragmentShader = shaders.compileShader(fragment_code, GL_FRAGMENT_SHADER)
	shaderProgram = shaders.compileProgram(vertexShader, fragmentShader)
	
	# Create and bind the Vertex Array Object
	vao = GLuint(0)
	glGenVertexArrays(1, vao)
	glBindVertexArray(vao)

	# Create and bind the Vertex Buffer Object
	vbo = glGenBuffers(1)
	glBindBuffer(GL_ARRAY_BUFFER, vbo)
	glBufferData(GL_ARRAY_BUFFER, piramide['vertices'], GL_STATIC_DRAW)
	glVertexAttribPointer(0, 3, GL_FLOAT, False, 6 * sizeof(GLfloat), ctypes.c_void_p(0))  # first 0 is the location in shader
	glVertexAttribPointer(1, 3, GL_FLOAT, False, 6 * sizeof(GLfloat), ctypes.c_void_p(3*sizeof(GLfloat)))  # first 0 is the location in shader

	glEnableVertexAttribArray(0);  # 0=location do atributo, tem que ativar todos os atributos inicialmente sao desabilitados por padrao
	glEnableVertexAttribArray(1);  # 1=location do atributo, tem que ativar todos os atributos inicialmente sao desabilitados por padrao
	
	# cria a matriz de transformação
	mvp['model'] = matrix44.create_identity()

	# rotacao
	rot = matrix44.create_from_y_rotation(math.radians(10))

	mvp['model'] = matrix44.multiply(mvp['model'],rot) # matrix model
	mvp['view'] = matrix44.create_identity()		   # matrix view
	mvp['projection'] = matrix44.create_identity()     # matrix projection
	

	# atribui uma variavel uniforme para cada matriz
	mvp['idMod'] = glGetUniformLocation(shaderProgram, "model")
	mvp['idView'] = glGetUniformLocation(shaderProgram, "view")
	mvp['idProj'] = glGetUniformLocation(shaderProgram, "projection")

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
	
	glUniformMatrix4fv(mvp['idMod'], 1, GL_FALSE, mvp['model'])
	glUniformMatrix4fv(mvp['idView'], 1, GL_FALSE, mvp['view'])
	glUniformMatrix4fv(mvp['idProj'], 1, GL_FALSE, mvp['projection'])

	# glDrawArrays( mode , first, count)
	#glDrawArrays(GL_TRIANGLES, 0, 4)
	glDrawElements(GL_TRIANGLE_STRIP, 12, GL_UNSIGNED_INT, piramide['faces'])

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
	glutCreateWindow(b'Piramide 3D')
	
	glutReshapeFunc(reshape)
	glutDisplayFunc(display)

	init()
	
	glutMainLoop()
