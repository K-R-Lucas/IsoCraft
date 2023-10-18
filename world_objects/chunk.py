from settings import *
from meshes.chunk_mesh import ChunkMesh
from random import randint

class Chunk:
    def __init__(self, world, position):
        self.app = world.app
        self.position = position
        self.blocks: np.array = None
        self.mesh: ChunkMesh = None
        self.m_model = self.get_model_matrix()
    
    def get_model_matrix(self):
        m_model = glm.translate(glm.mat4(), glm.vec3(self.position[0] * CHUNK_WIDTH, self.position[1] * CHUNK_HEIGHT, self.position[2] * CHUNK_DEPTH))
        return m_model
    
    def set_uniform(self):
        self.mesh.program["m_model"].write(self.m_model)

    def build_mesh(self):
        self.mesh = ChunkMesh(self)
    
    def render(self):
        self.set_uniform()
        self.mesh.render()
    
    def build_blocks(self):
        blocks = np.zeros(CHUNK_VOLUME, dtype="uint8")

        for z in range(CHUNK_DEPTH):
            for y in range(CHUNK_HEIGHT):
                for x in range(CHUNK_WIDTH):
                    blocks[x + y*CHUNK_WIDTH + z*CHUNK_AREA] = 1 if y == CHUNK_HEIGHT - 1 else 0# (-1 if not randint(0, 1) else 1) if y == CHUNK_HEIGHT -1 else randint(-1, 0)
        
        return blocks