CC=gcc
CFLAGS=-c -I../include/
SOURCES=*.c
OBDIR=build

.o:
	$(CC) $(CFLAGS) $(LIBS) $(SOURCES)
	mv *.o $(OBDIR)
all: .o
	
clean:
	rm -f $(OBDIR)/*.o
