#!/bin/sh

QTILE=$HOME/.qtile

setxkbmap de -variant colemakde

exec qtile -c $QTILE/config.py
