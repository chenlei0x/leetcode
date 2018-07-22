CFILES = $(wildcard *.c)
OBJS = $(patsubst %.c, %,$(CFILES))
#OBJS = $(subst .c,.o,$(CFILES))


all:
	gcc -Wall $(CFILES) -g -o $(OBJS)

clean:
	rm -rf $(OBJS)
.PHONY: all clean
#45: 45.c
#	gcc -g -o 45 45.c
#
#gcc  $< -o $@
