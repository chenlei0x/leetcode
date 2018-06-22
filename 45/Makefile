CFILES = $(wildcard *.c)
OBJS = $(patsubst %.c, %,$(CFILES))
#OBJS = $(subst .c,.o,$(CFILES))


all:
	@gcc $(CFILES) -o $(OBJS)

.PHONY: all
#45: 45.c
#	gcc -g -o 45 45.c
#
#gcc  $< -o $@
