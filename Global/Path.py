import os

CWD = os.getcwd()

FRAGMENT_SHADER = os.path.join(CWD, "shaders", "{}.frag")
VERTEX_SHADER = os.path.join(CWD, "shaders", "{}.vert")