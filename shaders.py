from settings import *

class ShaderProgram:
    def __init__(self, app):
        self.app = app
        self.ctx = app.ctx
        self.player = app.player

        # ---- Shaders ----
        self.chunk = self.get_program("chunk")
        # -----------------

        self.set_init_uniforms()

    def set_init_uniforms(self):
        self.chunk["m_proj"].write(self.player.m_proj)
        self.chunk["m_model"].write(glm.mat4())
        self.chunk["u_texture_0"] = 0
        self.chunk["u_texture_1"] = 1

    def update(self):
        self.chunk["m_view"].write(self.player.m_view)

    def get_program(self, shader_name: str):
        with open(FRAGMENT_SHADER.format(shader_name), 'r') as file:
            frag = file.read()
        
        with open(VERTEX_SHADER.format(shader_name), 'r') as file:
            vert = file.read()
        
        program = self.ctx.program(vertex_shader=vert, fragment_shader=frag)
        return program