all:
	g++ 2D/transforms.cpp -o app -lglut -lGL -lGLU -lm 
	./app
run:
	./app

clean:
	rm app
