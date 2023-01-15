## Installation

Before beginning, it is recommended to make a virtual environment. 

To install, navigate to the root directory. Install all dependencies and the command line tool in one line with
`pip install -r requirements.txt && python3 setup.py install`. Then the application may be invoked as `reddittools arg1 arg2
...`.

Tested on Ubuntu 20.04.2 LTS and Mac OSX TODO.

The full install, starting from Git, then making a virtual environment, installing dependencies and the library, and then running the program, is as follows:

## Command Line Invocation
To use the postfinder tool, use the `-p` flag with a secondary parameter that specifies a file of usernames. For example:
```
reddittools -p <filename>
```
Here the specified file should contain a list of usernames, one per line. As the program runs, processed usernames will be placed in a local `processed.log` file in the order that they are processed, removed from the input file in the same order.