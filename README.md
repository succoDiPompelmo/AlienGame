# AlienGame
A simple Game mad by the library PyGame

This is a very simple project that helps me to undestand 
how the pygame environment works and at the same time learn some
python


# Initialization

First of all to run this project you need to have installed python (version 2.7) 
on your device, here is the link to download it [PYTHON 2.7](https://www.python.org/download/releases/2.7/)

Next you have to install the pygame library to run the game, but first you need to check
if you have pip installed, to check so you need to run on your terminal (Linux, OS):

```sh
$ pip --version
```

if the output is somethin like this:

```sh
pip 7.0.3 from /usr/local/lib/python3.5/dist-packages (python 3.5)
$
```

then you have pip installed on your device an you can move on the section installing pygame. 
If you get an erro message you can move on this site and follow the instructions to install pip

# Installing PyGame on OS X

You’ll need Homebrew to install some packages that Pygame depends on.
To install the libraries that Pygame depends on, enter the following:
```sh
$ brew install hg sdl sdl_image sdl_ttf
```
If you also want to enable more advanced functionality, 
such as includ- ing sound in games, you can install two additional libraries:
```sh
$ brew install sdl_mixer portmidi
```
Use the following command to install Pygame:
```sh
$ pip install --user hg+http://bitbucket.org/pygame/pygame
```
Check wether the installation was successful:
```sh
$ python3
>>> import pygame 
>>>
```
if the impoer statement work, you have finished the initialization procedure and 
you can run the game



