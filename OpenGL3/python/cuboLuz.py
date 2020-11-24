import sys
import numpy as np
import math 

import pywavefront as obj
from pyrr import matrix44, Vector3

from OpenGL.GL import *
from OpenGL.GL import shaders
from OpenGL.GLUT import *

vao = None
vbo = None
shaderProgram = None
model = None			# a matriz model
idMod = None            # id matriz model shaders
view = None			   	# a matriz view
idView = None           # id matriz view shaders
projection = None		# a matriz projection
idProj = None           # id matriz projection shaders

posCam = None
# iluminação
idColor = None
idLight = None
idLightPos = None
idViewPos = None

def readObjFile(path):
	return obj.Wavefront(path)

def readVertexData():
	aux = readObjFile('python/cube.obj')
	aux.parse()
	for name, material in aux.materials.items():
		return material.vertices

# le os arquivos do shaders
def readShaderFile(filename):
	with open('shader/' + filename, 'r') as myfile:
		return myfile.read()

def init():
	global shaderProgram
	global vao
	global vbo
	global model
	global idMod
	global view			   	
	global idView           
	global projection
	global idProj 
	global idColor
	global idLight
	global idLightPos
	global idViewPos
	global posCam

	glClearColor(0, 0, 0, 0)
	
	vertex_code = readShaderFile('cuboLuz.vp')
	fragment_code = readShaderFile('cuboLuz.fp')

	# compile shaders and program
	vertexShader = shaders.compileShader(vertex_code, GL_VERTEX_SHADER)
	fragmentShader = shaders.compileShader(fragment_code, GL_FRAGMENT_SHADER)
	shaderProgram = shaders.compileProgram(vertexShader, fragmentShader)
	
	# cria um vao
	vao = GLuint(0)
	glGenVertexArrays(1, vao)
	glBindVertexArray(vao)

	# dados do objeto q serao passados para o shaders (vertices e vetores normais)
	vertices = np.array(readVertexData(), dtype='f')
	print("vertices:", len(vertices)//6)
	print(vertices)

	vbo = glGenBuffers(1) # gera vbos
	glBindBuffer(GL_ARRAY_BUFFER, vbo)
	glBufferData(GL_ARRAY_BUFFER, vertices, GL_STATIC_DRAW)
	glVertexAttribPointer(0, 3, GL_FLOAT, False, 6 * sizeof(GLfloat), ctypes.c_void_p(3*sizeof(GLfloat)))  # vertices
	glVertexAttribPointer(1, 3, GL_FLOAT, False, 6 * sizeof(GLfloat), ctypes.c_void_p(0))  # vertores normais
	
	# habilita os atributos
	glEnableVertexAttribArray(0) 
	glEnableVertexAttribArray(1)
	  
	# cria a matriz de transformação
	model = matrix44.create_identity()

	#ratacoes
	rotY = matrix44.create_from_y_rotation(math.radians(45))
	rotx = matrix44.create_from_x_rotation(math.radians(45))
	rotT = matrix44.multiply(rotY,rotx)

	model = matrix44.multiply(model,rotT) 

	posCam = [0.0, 0.0, 0.0]
	view = matrix44.create_look_at(posCam, [0.0, 0.0,-0.1], [0.0, 1.0, 0.0])
	projection = matrix44.create_orthogonal_projection(-2.0, 2.0, -2.0, 2.0, 2.0, -2.0) # amplia a visao
	print(f'Model:\n{model}\n')
	print(f'View:\n{view}\n')
	print(f'Projection:\n{projection}\n')

	# atribui uma variavel uniforme para cada matriz
	idMod = glGetUniformLocation(shaderProgram, "model")
	idView = glGetUniformLocation(shaderProgram, "view")
	idProj = glGetUniformLocation(shaderProgram, "projection")

	# iluminação
	idColor = glGetUniformLocation(shaderProgram, "objectColor")
	idLight = glGetUniformLocation(shaderProgram, "lightColor")
	idLightPos = glGetUniformLocation(shaderProgram, "lightPos")
	idViewPos = glGetUniformLocation(shaderProgram, "viewPos")

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
	
	lightPos = [2.0, 0.0, 0.0] # posicao da luz
	glUniform3fv(idLightPos, 1,lightPos)
	glUniform3fv(idColor,1,[1.0,0.0,0.0])
	glUniform3fv(idLight,1,[1.0,1.0,1.0])
	glUniform3fv(idViewPos,1,posCam)
	
	glUniformMatrix4fv(idMod, 1, GL_FALSE, model)
	glUniformMatrix4fv(idView, 1, GL_FALSE, view)
	glUniformMatrix4fv(idProj, 1, GL_FALSE, projection)
	glDrawArrays(GL_TRIANGLE_STRIP, 0, 42)

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
	glutCreateWindow(b'cubo Iluminado!')
	
	glutReshapeFunc(reshape)
	glutDisplayFunc(display)

	init()
	
	glutMainLoop()
