all:
	g++ 2D/triangleRot.cpp -o app -lglut -lGL -lGLU -lm 
	./app
run:
	./app

clean:
	rm app
