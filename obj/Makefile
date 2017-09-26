CC = g++
OBJ = $(wildcard *.o)
EXE = $(patsubst %.x, ../%.cgi, $(wildcard *.x))
gtkmmLIB = $(shell pkg-config gtkmm-3.0 --libs)

all : $(EXE)

../%.cgi : %.x $(OBJ)
	$(CC) -o $@ $< $(OBJ) -lzezeon -lmysqlcppconn $(gtkmmLIB)


