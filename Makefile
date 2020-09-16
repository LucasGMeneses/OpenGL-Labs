all:
	g++ *.cpp -o app -lglut -lGL -lGLU -lm

run:
	./app

clean:
	rm app
