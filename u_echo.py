#!/usr/bin/env python
from shlex import join as shx_join
from sys import argv, exit, stderr

def echo_basic():

    cmds = f"{shx_join(argv[1:])}"
    print(cmds)


def echo_enabled():
    
    try:
            
        if "-e" in argv:
            e_index = argv.index("-e")
            args = argv[e_index + 1:]
            cmds = ' '.join(args)
            decoded = bytes(cmds, 'utf-8').decode('unicode_escape')

            decoded = decoded.replace(r'\a', '\a')
            decoded = decoded.replace(r'\b', '\b')
            decoded = decoded.replace(r'\v', '\v')
            decoded = decoded.replace(r'\f', '\f')

            print(decoded)
        else:
            echo_basic()

    except (ValueError, IndexError) as e:
        print(f"{e} Invalid option", file=stderr)
        exit(1)


if __name__ == '__main__':

    if len(argv) < 2:
        print("Usage: echo <string>")
        exit(1)

    echo_enabled()