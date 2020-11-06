import sys
import numpy as np
import math 
from OpenGL.GL import *
from OpenGL.GL import shaders
from OpenGL.GLUT import *

vao = None
vbo = None
shaderProgram = None
uniColor = None
# gera os vertices do circulo
# retorna um array com os vertices
def circleVertex(raio, cx, cy):
	vertices = []
	for i in range(360):
		ang = (i * math.pi) / 180
		x = cx + (math.cos(ang) * raio)
		y = cy + (math.sin(ang) * raio)
		vertices.append([x,y,0])
	
	return np.array(vertices, dtype='f')


def readShaderFile(filename):
	with open('shader/' + filename, 'r') as myfile:
		return myfile.read()

def init():
	global shaderProgram
	global vao
	global vbo
	global uniColor
	glClearColor(0, 0, 0, 0);
	
	vertex_code = readShaderFile('ice.vp')
	fragment_code = readShaderFile('ice.fp')

	# compile shaders and program
	vertexShader = shaders.compileShader(vertex_code, GL_VERTEX_SHADER)
	fragmentShader = shaders.compileShader(fragment_code, GL_FRAGMENT_SHADER)
	shaderProgram = shaders.compileProgram(vertexShader, fragmentShader)

	# Create and bind the Vertex Array Object
	vao = GLuint(0)
	glGenVertexArrays(1, vao)
	glBindVertexArray(vao)

	# Create and bind the Vertex Buffer Object
	#cria  as bolas de sorvete
	sorvete = np.concatenate((
					circleVertex(0.3,-0.3,0),
					circleVertex(0.3, 0,0.2),
					circleVertex(0.3, 0.3,0)
				))

	#cria a casquinha
	casquinha = np.array([[-0.3, 0, 0], [0, -1, 0], [0.3, 0, 0]], dtype='f')
	
	#junta os array em um so
	vertices = np.concatenate((casquinha,sorvete))
	
	vbo = glGenBuffers(1)
	glBindBuffer(GL_ARRAY_BUFFER, vbo)
	glBufferData(GL_ARRAY_BUFFER, vertices, GL_STATIC_DRAW)
	glVertexAttribPointer(0, 3, GL_FLOAT, False, 0, None)  # first 0 is the location in shader
	glBindAttribLocation(shaderProgram, 0, 'vertexPosition')  # name of attribute in shader
	glEnableVertexAttribArray(0)  # 0=location do atributo, tem que ativar todos os atributos inicialmente sao desabilitados por padrao
	
	# atribui uma variavel uniforme para cor
	uniColor = glGetUniformLocation(shaderProgram, "uColor")

	# Note that this is allowed, the call to glVertexAttribPointer registered VBO
	# as the currently bound vertex buffer object so afterwards we can safely unbind
	glBindBuffer(GL_ARRAY_BUFFER, 0)
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
	
	# glDrawArrays( mode , first, count)
	#desenha os objetos

	# desenha casquinha
	glUniform3f(uniColor, 0.9, 0.6,0.25) # muda a cor da variavel uniforme
	glDrawArrays(GL_TRIANGLES, 0, 3)
	
	# desenha bolas de sorvete
	# bola do meio
	glUniform3f(uniColor, 1, 0.3,0.3)
	glDrawArrays(GL_POLYGON, 363, 360)
	# bola da esquerda
	glUniform3f(uniColor, 1, 1,0.5)
	glDrawArrays(GL_POLYGON, 3, 360)
	# bola da direita
	glUniform3f(uniColor, 0.3, 0.5,1)
	glDrawArrays(GL_POLYGON, 363+360, 360)

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
	glutCreateWindow(b'Ice Cream!')
	
	glutReshapeFunc(reshape)
	glutDisplayFunc(display)

	init()
	
	glutMainLoop()
