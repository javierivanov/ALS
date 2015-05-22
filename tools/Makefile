CC=gcc
CFLAGS=-c -I../include/
SOURCES=*.c
OBDIR=build

.o:
	$(CC) $(CFLAGS) $(SOURCES)
	mv *.o $(OBDIR)
all: .o
	
clean:
	rm -f $(OBDIR)/*.o
