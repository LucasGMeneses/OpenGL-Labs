import sys
import numpy as np
import math 
from OpenGL.GL import *
from OpenGL.GL import shaders
from OpenGL.GLUT import *

vao = None
vbo = None
shaderProgram = None
uMat = None            # variavel uniforme
matTrans = None        # matriz de transformação

# gera a matriz de Translação
def matrixTranslate(x,y,z):
	matId = np.eye(4, dtype='f')
	matId[0][3] = x
	matId[1][3] = y
	matId[2][3] = z
	#print(matId)
	return matId

# gera a matriz de Escala
def matrixScale(x,y,z):
	matId = np.eye(4, dtype='f')
	matId[0][0] = x
	matId[1][1] = y
	matId[2][2] = z
	return matId

# gera a matriz de Rotacao em relação a um dos eixos (x, y ou z)
def matrixRotate(ang, axis='z'):
	rad = (ang/180) * math.pi
	matId = np.eye(4, dtype='f')
	
	if axis == 'z':
		matId[0][0] =   math.cos(rad)
		matId[1][1] =   math.cos(rad)

		matId[0][1] = - math.sin(rad)
		matId[1][0] =   math.sin(rad)

	elif axis == 'x':
		matId[1][1] =   math.cos(rad)
		matId[2][2] =   math.cos(rad)

		matId[1][2] = - math.sin(rad)
		matId[2][1] =   math.sin(rad)

	elif axis == 'y':
		matId[0][0] =   math.cos(rad)
		matId[2][2] =   math.cos(rad)

		matId[2][0] = - math.sin(rad)
		matId[0][2] =   math.sin(rad)
	else:
		print("Eixo invalido!!!")
	return matId 

# le os arquivos do shaders
def readShaderFile(filename):
	with open('shader/' + filename, 'r') as myfile:
		return myfile.read()

def init():
	global shaderProgram
	global vao
	global vbo
	global matTrans
	global uMat

	matT = matrixTranslate(0, 0, 0.5)
	matR = matrixRotate(30,'x')
	print(matR)
	matS = matrixScale(0.3,0.3,0.3)

	# cria a matriz de transformação
	matTrans = np.dot(matR,matS)
	matTrans = np.dot(matTrans,matT)
	print(matTrans)

	glClearColor(0, 0, 0, 0)
	
	vertex_code = readShaderFile('cube.vp')
	fragment_code = readShaderFile('cube.fp')

	# compile shaders and program
	vertexShader = shaders.compileShader(vertex_code, GL_VERTEX_SHADER)
	fragmentShader = shaders.compileShader(fragment_code, GL_FRAGMENT_SHADER)
	shaderProgram = shaders.compileProgram(vertexShader, fragmentShader)
	
	# Create and bind the Vertex Array Object
	vao = GLuint(0)
	glGenVertexArrays(1, vao)
	glBindVertexArray(vao)

	# Create and bind the Vertex Buffer Object (CUBE 3D)
	vertices = np.array(
		[[-1.0,-1.0,-1.0],
		[-1.0,-1.0, 1.0],
		[-1.0, 1.0, 1.0],
		[1.0, 1.0,-1.0],
		[-1.0,-1.0,-1.0],
		[-1.0, 1.0,-1.0],
		[1.0,-1.0, 1.0],
		[-1.0,-1.0,-1.0],
		[1.0,-1.0,-1.0],
		[1.0, 1.0,-1.0],
		[1.0,-1.0,-1.0],
		[-1.0,-1.0,-1.0],
		[-1.0,-1.0,-1.0],
		[-1.0, 1.0, 1.0],
		[-1.0, 1.0,-1.0],
		[1.0,-1.0, 1.0],
		[-1.0,-1.0, 1.0],
		[-1.0,-1.0,-1.0],
		[-1.0, 1.0, 1.0],
		[-1.0,-1.0, 1.0],
		[1.0,-1.0, 1.0],
		[1.0, 1.0, 1.0],
		[1.0,-1.0,-1.0],
		[1.0, 1.0,-1.0],
		[1.0,-1.0,-1.0],
		[1.0, 1.0, 1.0],
		[1.0,-1.0, 1.0],
		[1.0, 1.0, 1.0],
		[1.0, 1.0,-1.0],
		[-1.0, 1.0,-1.0],
		[1.0, 1.0, 1.0],
		[-1.0, 1.0,-1.0],
		[-1.0, 1.0, 1.0],
		[1.0, 1.0, 1.0],
		[-1.0, 1.0, 1.0],
		[1.0,-1.0, 1.0]], dtype='f')

	vbo = glGenBuffers(1)
	glBindBuffer(GL_ARRAY_BUFFER, vbo)
	glBufferData(GL_ARRAY_BUFFER, vertices, GL_STATIC_DRAW)
	glVertexAttribPointer(0, 3, GL_FLOAT, False, 0, None)  # first 0 is the location in shader
	glBindAttribLocation(shaderProgram, 0, 'vertexPosition')  # name of attribute in shader
	glEnableVertexAttribArray(0);  # 0=location do atributo, tem que ativar todos os atributos inicialmente sao desabilitados por padrao
	
	# atribui uma variavel uniforme para matriz de transformacao
	uMat = glGetUniformLocation(shaderProgram, "matTrans")

	# Note that this is allowed, the call to glVertexAttribPointer registered VBO
	# as the currently bound vertex buffer object so afterwards we can safely unbind
	glBindBuffer(GL_ARRAY_BUFFER, 0);
	# Unbind VAO (it's always a good thing to unbind any buffer/array to prevent strange bugs)
	glBindVertexArray(0);

def display():
	global shaderProgram
	global vao
	
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
	
	# load everthing back
	glUseProgram(shaderProgram)
	glBindVertexArray(vao)
	glBindBuffer(GL_ARRAY_BUFFER, vbo)
	glUniformMatrix4fv(uMat, 1, GL_FALSE, matTrans)
	#glDrawArrays( mode , first, count)
	#glDrawArrays(GL_LINES, 0, 36)
	glDrawArrays(GL_TRIANGLE_FAN, 0, 36)

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
	glutCreateWindow(b'cube 3D!')
	
	glutReshapeFunc(reshape)
	glutDisplayFunc(display)

	init()
	
	glutMainLoop()
