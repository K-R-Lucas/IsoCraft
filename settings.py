import numpy as np, pygame as pg, glm, math, moderngl as mgl, os
from glm import vec2, vec3, vec4, make_vec2, make_vec3, make_vec4

# Window stuff
WINDOW_RES = vec2(1280, 720)
DEF_BG_COLOUR = vec4(51/255, 51/255, 51/255, 1.0)

# Path stuff
CWD = os.getcwd()
FRAGMENT_SHADER = os.path.join(CWD, "shaders", "{}.frag")
VERTEX_SHADER = os.path.join(CWD, "shaders", "{}.vert")
BLOCK_TEXTURE = os.path.join(CWD, "assets", "textures", "blocks", "{}.png")

# World stuff
WORLD_WIDTH = 2
WORLD_HEIGHT = 1
WORLD_DEPTH = 2
WORLD_AREA = WORLD_WIDTH * WORLD_HEIGHT
WORLD_VOLUME = WORLD_WIDTH * WORLD_HEIGHT * WORLD_DEPTH

# Chunk stuff
CHUNK_HEIGHT = 32
CHUNK_WIDTH = 32
CHUNK_DEPTH = 32
CHUNK_AREA = CHUNK_WIDTH * CHUNK_HEIGHT
CHUNK_VOLUME = CHUNK_WIDTH * CHUNK_HEIGHT * CHUNK_DEPTH

# Camera stuff
ASPECT_RATIO = WINDOW_RES.x / WINDOW_RES.y
FOV = 50
V_FOV = glm.radians(FOV)
H_FOV = 2*math.atan(math.tan(0.5 * V_FOV) * ASPECT_RATIO)
NEAR = 0.1
FAR = 2000

# Player Stuff
PLAYER_POS = vec3(0, 0, 5)
PLAYER_SPEED = 10
MOUSE_SENSE = 0.001
PITCH_LIMIT = 89 # Absolute