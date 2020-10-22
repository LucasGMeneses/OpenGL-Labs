all:
	g++ ex3.cpp -o app -lglut -lGL -lGLU -lm 
	./app
run:
	./app

clean:
	rm app
