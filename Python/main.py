from settings import *
from Utils.Timing import Timer
from shaders import ShaderProgram
from scene import Scene
from player import Player
import sys

class IsoCraft:
    def __init__(self):
        pg.init()
        pg.display.gl_set_attribute(pg.GL_CONTEXT_MAJOR_VERSION, 4)
        pg.display.gl_set_attribute(pg.GL_CONTEXT_MINOR_VERSION, 3)
        pg.display.gl_set_attribute(pg.GL_CONTEXT_PROFILE_MASK, pg.GL_CONTEXT_PROFILE_CORE)
        
        pg.display.set_mode(WINDOW_RES, pg.OPENGL | pg.DOUBLEBUF | pg.RESIZABLE)
        self.ctx = mgl.create_context()

        self.ctx.enable(mgl.CULL_FACE | mgl.BLEND)
        self.ctx.gc_mode = "auto"
        self.mouse_cap = False

        self.clock = pg.time.Clock()
        self.dt = 0
        self.ft = 0
        self.t = 0

        self.main_timer = Timer(165)
        self.debug_timer = Timer(4)

        self.is_running = True
        self.title = "IsoCraft - {}"
        self.re_init()
    
    def re_init(self):
        self.player = Player(self)
        self.shaders = ShaderProgram(self)
        self.scene = Scene(self)

    def report(self):
        pg.display.set_caption(self.title.format(round(1.0/self.ft if self.ft else 0)))

    def update(self):
        self.player.update()
        self.shaders.update()
        self.scene.update()
    
    def tick(self):
        pass
    
    def render(self):
        self.ctx.clear(color = DEF_BG_COLOUR)
        
        self.update()
        self.scene.render()

        pg.display.flip()
    
    def handle_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                self.is_running = False
            
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_LALT:
                    self.mouse_cap = not self.mouse_cap

                    pg.mouse.set_visible(not self.mouse_cap)
                    pg.event.set_grab(self.mouse_cap)
            
            # if event.type == pg.WINDOWRESIZED:
            #     WINDOW_RES = vec2(event.x, event.y)
            #     ASPECT_RATIO = WINDOW_RES.x / WINDOW_RES.y
            #     H_FOV = 2*math.atan(math.tan(0.5 * V_FOV) * ASPECT_RATIO)

    def run(self):
        while self.is_running:
            self.handle_events()

            while self.main_timer.tick():
                self.tick()

            while self.debug_timer.tick():
                self.report()

            self.render()

            self.ft = self.clock.tick(165) * 0.001
            self.main_timer.accumulate(self.ft)
            self.debug_timer.accumulate(self.ft)
            self.t += self.ft
        
        pg.quit()
        return 0

if __name__ == "__main__":
    app = IsoCraft()
    sys.exit(app.run())