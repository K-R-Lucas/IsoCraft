import numpy as np
from meshes.base import BaseMesh
from meshes.chunk_mesh_builder import buildChunkMesh

class ChunkMesh(BaseMesh):
    def __init__(self, chunk):
        super().__init__()
        self.app = chunk.app
        self.chunk = chunk

        self.ctx = self.app.ctx
        self.program = self.app.shaders.chunk

        self.vbo_format = "3f 1f 1f"
        self.format_size = 20
        self.attrs = ("in_position", "block_id", "face_id")
        self.vao = self.get_vao()
    
    def get_vertex_data(self):
        mesh = buildChunkMesh(
            chunk_blocks = self.chunk.blocks,
            format_size = self.format_size
        )
        return mesh