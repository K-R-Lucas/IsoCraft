from settings import *
from meshes.hexagon import HexagonMesh
from world_objects.chunk import Chunk

class Scene:
    def __init__(self, app):
        self.app = app
        self.chunks = []

        for i in range(1):
            self.chunks.append(
                Chunk(self.app)
            )

    def update(self):
        pass

    def render(self):
        for chunk in self.chunks:
            chunk.render()