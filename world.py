from settings import *
from world_objects.chunk import Chunk
from math import sqrt

c30 = (glm.cos(glm.radians(30)) + 0)
s30 = (glm.sin(glm.radians(30)) + 0)

class World:
    def __init__(self, app):
        self.app = app
        self.ctx = app.ctx
        self.chunks: list[Chunk] = [None for _ in range(WORLD_VOLUME)]
        self.blocks = np.empty([WORLD_VOLUME, CHUNK_VOLUME], dtype="uint8")
        self.build_chunks()
        self.build_chunk_mesh()
    
    def build_chunks(self):
        for z in range(WORLD_DEPTH):
            for y in range(WORLD_HEIGHT):
                for x in range(WORLD_WIDTH):
                    X = c30 * (z + x)
                    Y = y + s30 * (x - z)
                    Z = 0 # sqrt(x**2 + y**2 + z**2)

                    chunk = Chunk(self, position=(X, Y, Z))

                    chunk_index = x + y*WORLD_WIDTH + z*WORLD_AREA
                    self.chunks[chunk_index] = chunk

                    self.blocks[chunk_index] = chunk.build_blocks()
                    chunk.blocks = self.blocks[chunk_index]


    def build_chunk_mesh(self):
        for chunk in self.chunks:
            chunk.build_mesh()

    def update(self):
        pass

    def render(self):
        for chunk in self.chunks:
            chunk.render()