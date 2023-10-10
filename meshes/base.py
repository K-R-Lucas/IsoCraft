import numpy as np

class BaseMesh:
    def __init__(self):
        # GL Context
        self.ctx = None
        
        # Shader program
        self.program = None

        # Eg: "3f 3f"
        self.vbo_format = None
        
        # Eg: ("in_position", "in_colour")
        self.attrs: tuple[str, ...] = None

        # Vertex array
        self.vao = None

    def get_vertex_data(self) -> np.array: ...

    def get_vao(self):
        vertex_data = self.get_vertex_data()
        vbo = self.ctx.buffer(vertex_data)
        vao = self.ctx.vertex_array(
            self.program, [(vbo, self.vbo_format, *self.attrs)], skip_errors = True
        )
        return vao

    def render(self):
        self.vao.render()