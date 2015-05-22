CC=gcc
CFLAGS=-c -Iinclude/
EXECUTABLE=test
SOURCES= src/levenshtein.c src/main.c
.o:
	$(CC) $(CFLAGS) $(SOURCES)
all: .o
	$(CC) *.o -o $(EXECUTABLE)
clean:
	rm -f *.o $(EXECUTABLE)
