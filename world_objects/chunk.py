from settings import *
from meshes.chunk_mesh import ChunkMesh
from random import randint

class Chunk:
    def __init__(self, app):
        self.app = app
        self.blocks: np.array = self.buildTerrain()
        self.mesh: ChunkMesh = None
        self.buildMesh()
    
    def buildMesh(self):
        self.mesh = ChunkMesh(self)
    
    def render(self):
        self.mesh.render()
    
    def buildTerrain(self):
        blocks = np.zeros(CHUNK_VOLUME, dtype="uint8")

        for y in range(CHUNK_HEIGHT):
            for z in range(CHUNK_DEPTH):
                for x in range(CHUNK_WIDTH):
                    blocks[x + z*CHUNK_WIDTH + y*CHUNK_AREA] = (-1 if not randint(0, 1) else 1) if y == CHUNK_HEIGHT -1 else randint(-1, 0)
        
        return blocks