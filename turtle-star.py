#!/usr/bin/env python3
# Importing turtle library to draw a star

from turtle import *
title("You are the star!")
color('red', 'orange')
begin_fill()
while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()
done()