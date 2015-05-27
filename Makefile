CC=gcc
CFLAGS=-g -Iinclude/
EXEC=test
LIBS=-lm

main:
	cd tools && make && cd ..
	$(CC) $(CFLAGS) $(LIBS) tools/build/*.o main.c -o $(EXEC)
clean:
	rm $(EXEC)
	cd tools && make clean
