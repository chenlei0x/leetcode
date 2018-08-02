#!/bin/bash
towards=$PWD
towards=${towards##*/}
mv *.py $towards.py
mv *.c $towards.c
