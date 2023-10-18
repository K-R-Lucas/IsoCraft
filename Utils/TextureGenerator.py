from math import cos, sin, pi, radians, ceil, floor, sqrt
from pygame import Vector2 as vec
import pygame as pg
scale = 0.5

def createTextureFrom(side: pg.Surface, front: pg.Surface, top: pg.Surface, output_file: str = "iso_block.png"):
    temp = pg.Surface((16 * 3, 16), pg.SRCALPHA, 32)

    temp.blit(top, (0, 0))
    temp.blit(side, (16, 0))
    temp.blit(front, (32, 0))

    pg.image.save(temp, output_file)

# def createTextureFrom(left: pg.Surface, right: pg.Surface, top: pg.Surface, output_file: str = "iso_block.png"):
#     temp = pg.Surface((32, 31), pg.SRCALPHA, 32)

#     offset = 0
    
#     for y in range(16):
#         for x in range(16):
#             X = x
#             Y = y + int((x/2) % 16) + 8
#             temp.set_at((X + offset, Y + offset), left.get_at((x, y)))

#     for y in range(16):
#         for x in range(16):
#             X = x + 16
#             Y = y - int((x/2) % 16) + 15
#             temp.set_at((X + offset, Y + offset), right.get_at((x, y)))
    
#     for y in range(0, 16, 2):
#         for x in range(16):
#             X = 1 + x + y
#             Y = 7 + y//2 - int((x/2) % 16)
#             temp.set_at((X + offset, Y + offset), top.get_at((x, y)))

#     for y in range(1, 15, 2):
#         for x in range(1, 16):
#             X = 0 + x + y
#             Y = 8 + y//2 - int((x/2) % 16)
#             temp.set_at((X + offset, Y + offset), top.get_at((x, y)))
    
#     for y in range(15, 16):
#         for x in range(3, 16, 2):
#             X = x + 12 + 2
#             Y = 15 - x//2
#             temp.set_at((X + offset, Y + offset), top.get_at((x, y)))

#     pg.image.save(temp, output_file)


if __name__ == "__main__":
    pg.display.set_mode((1, 1), 0, 32)

    # # Grass Block
    # img_side = pg.image.load("assets/minecraft/grass_block_side.png").convert_alpha()
    # img_front = pg.image.load("assets/minecraft/grass_block_side.png").convert_alpha()
    # img_top = pg.image.load("assets/minecraft/grass_block_top.png").convert_alpha()

    # # Dirt Block
    # img_side = pg.image.load("assets/minecraft/dirt.png").convert_alpha()
    # img_front = pg.image.load("assets/minecraft/dirt.png").convert_alpha()
    # img_top = pg.image.load("assets/minecraft/dirt.png").convert_alpha()

    # Furnace
    img_front = pg.image.load("assets/minecraft/furnace_front.png").convert_alpha()
    img_side = pg.image.load("assets/minecraft/furnace_side.png").convert_alpha()
    img_top = pg.image.load("assets/minecraft/furnace_top.png").convert_alpha()

    createTextureFrom(img_side, img_front, img_top, "assets/textures/blocks/furnace_off.png")

# python3 Texgen.py --front "furnace_front" --side "furnace_side" --top "furnace_top"
from argparse import ArgumentParser
import sys
import pygame as pg

parser = ArgumentParser()

parser.add_argument(
    "-t", "--top",
    dest = "top_texture"
)

parser.add_argument(
    "-s", "--side",
    dest = "side_texture"
)

parser.add_argument(
    "-f", "--front",
    dest = "front_texture"
)

parser.add_argument(
    "-o", "--output",
    dest = "output_path"
)

args = parser.parse_args()

# Load images first
top = pg.image.load(args.top_texture)
side = pg.image.load(args.side_texture)
front = pg.image.load(args.front_texture)

# Get sizes and check they are the same
top_res = top.get_size()
side_res = side.get_size()
front_res = front.get_size()

if not ((top_res == side_res) and (side_res == front_res)):
    raise ValueError("The provided images are different resolutions. All faces of one block must have the same resolution texture.")

# Load textures onto one surface
temp = pg.Surface((top_res[0] * 3, top_res[1]), 0, 32)
temp.blit(top, (0, 0))
temp.blit(side, (top_res[0], 0))
temp.blit(front, (2*top_res[0], 0))

pg.image.save(temp, args.output_path)