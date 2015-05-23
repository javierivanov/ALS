CC=gcc
CFLAGS=-Iinclude/
EXEC=test
tools:
	cd tools &&  make
main: tools
	$(CC) $(CFLAGS) tools/build/*.o main.c -o $(EXEC)
clean:
	rm $(EXEC)
