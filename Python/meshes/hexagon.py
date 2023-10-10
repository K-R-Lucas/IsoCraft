import numpy as np
from settings import *
from meshes.base import BaseMesh

class HexagonMesh(BaseMesh):
    def __init__(self, app):
        super().__init__()
        
        self.app = app
        self.ctx = app.ctx
        self.program = app.shaders.hexagon

        self.vbo_format = "3f 3f"
        self.attrs = ("in_position", "in_colour")
        self.vao = self.get_vao()

    def get_vertex_data(self):
        vertices = []
        colours = []

        for a1 in range(0, 360, 60):
            A1 = glm.radians(a1)
            A2 = glm.radians(a1 + 60)

            vertices.append(
                (0, 0, 0)
            )

            vertices.append(
                (0.5*glm.cos(A1), 0.5*glm.sin(A1), 0)
            )

            vertices.append(
                (0.5*glm.cos(A2), 0.5*glm.sin(A2), 0)
            )

        palette = [
            (1, 0, 0),
            (0, 1, 0),
            (0, 0, 1),
            (1, 1, 0),
            (1, 0, 1),
            (0, 1, 1)
        ]

        for i in range(6):
            for j in range(3):
                colours.append(palette[i])

        vertex_data = np.hstack([vertices, colours], dtype="float32")
        return vertex_data