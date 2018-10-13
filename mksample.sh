#!/bin/bash

target=$1
cp -r sample $1
{
	cd $1
	./trans.sh
}
