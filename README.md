# Overview

This software is a 20-questions game, aimed to guess what character the user chooses from the game
Super Smash Bros. Ultimate. The software only needs on average 7-8 questions to figure it out,
as long as the user does not deviate from expected answers. Meaning the yes/no answers must match my
character info csv file. I have programmed 23 questions, and the software chooses the best question
to ask each time based on which question has the closest yes/no split to 50/50.

My purpose for writing this software is to take a step towards more machine learning software. This software
is not a huge step, but it uses statistical analysis on the questions to find the most reliable path to the
answer, which is why it consistantly finds the answer in the 7-8 range. I enjoyed programming this very much.

[Software Demo Video](http://youtube.link.goes.here)

# Development Environment

I used visual studio to write and test the code. Excel was used to create the csv file containing
all the needed character information

I used the python programming language, pandas module, numpy module

# Useful Websites

* [sololearn, machine learning](https://www.sololearn.com/)
* [smash bros website](https://www.smashbros.com/en_US/fighter/index.html)

# Future Work

* Add a gui to allow the user to press yes/no buttons
* Have the program throw out a random guess once or twice based on possible characters left over
* 
