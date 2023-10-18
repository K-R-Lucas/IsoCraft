from settings import *

class Textures:
    def __init__(self, app):
        self.app = app
        self.ctx = app.ctx

        self.tex_0 = self.load("Test")
        self.tex_0.use(location = 0)

        self.tex_1 = self.load("grass")
        self.tex_1.use(location = 1)
    
    def load(self, textureName):
        texture = pg.image.load(BLOCK_TEXTURE.format(textureName)).convert_alpha()
        texture = pg.transform.flip(texture, False, True)

        texture = self.ctx.texture(
            size = texture.get_size(),
            components = 4,
            data = pg.image.tostring(texture, "RGBA", False)
        )

        texture.anistropy = 32.0
        texture.build_mipmaps()
        texture.filter = (mgl.NEAREST, mgl.NEAREST)

        return texture