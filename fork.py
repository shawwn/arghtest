#!/usr/bin/env python3
import argh
import builtins as py

parser = argh.ArghParser()

def command(f, *args, **kws):
  parser.add_commands([f], *args, **kws)

# declaring:

@command
def echo(text):
    "Returns given word as is."
    return text

@command
@argh.arg('text', default='hello world', nargs='+', help='The message')
def print(text):
    py.print(text)

@command
def greet(name, greeting='Hello'):
    "Greets the user with given name. The greeting is customizable."
    return greeting + ', ' + name

# assembling:


# dispatching:

if __name__ == '__main__':
    parser.dispatch()
