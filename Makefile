CC=gcc
CFLAGS=-Iinclude/
EXEC=test

main:
	cd tools && make && cd ..
	$(CC) $(CFLAGS) tools/build/*.o main.c -o $(EXEC)
clean:
	rm $(EXEC)
	cd tools && make clean
