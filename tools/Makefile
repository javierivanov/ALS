CC=gcc
CFLAGS=-c -I../include/
EXECUTABLE=test
SOURCES=levenshtein.c
.o:
	$(CC) $(CFLAGS) $(SOURCES)
all: .o
	$(CC) *.o -o $(EXECUTABLE)
clean:
	rm -f *.o $(EXECUTABLE)
