from settings import *
from meshes.chunk_mesh import ChunkMesh

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

        for z in range(CHUNK_DEPTH):
            for y in range(CHUNK_HEIGHT):
                for x in range(CHUNK_WIDTH):
                    blocks[x + y*CHUNK_WIDTH + z*CHUNK_AREA] = x + y + z + 1
        
        return blocks