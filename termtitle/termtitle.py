#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

def change_title():
    title = ""
    if len(sys.argv) >= 2:
        title = sys.argv[1]
    # http://tldp.org/HOWTO/Xterm-Title-3.html xterm escape sequences
    # \033]0; "\033 is an escape code (ESC)". But \u001b or \x1b represent ESC too.
    # \007 bell char
    cmd = "\033]0;{}\007".format(title)
    sys.stdout.write(cmd)
