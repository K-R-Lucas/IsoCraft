import numpy as np
from settings import *
from meshes.base import BaseMesh

class TriangleMesh(BaseMesh):
    def __init__(self, app):
        super().__init__()
        
        self.app = app
        self.ctx = app.ctx
        self.program = app.shaders.triangle

        self.vbo_format = "3f 3f"
        self.attrs = ("in_position", "in_colour")
        self.vao = self.get_vao()

    def get_vertex_data(self):
        vertices = [
            (-0.5, -0.5, 0.0), (0.5, -0.5, 0.0), (0.0, 0.5, 0.0)
        ]

        colours = [
            (1, 0, 0), (0, 1, 0), (0, 0, 1)
        ]

        vertex_data = np.hstack([vertices, colours], dtype="float32")
        return vertex_data