from settings import *
from camera import Camera

class Player(Camera):
    def __init__(self, app, position=PLAYER_POS, yaw=-90, pitch=0):
        self.app = app
        super().__init__(position, yaw, pitch)
    
    def update(self):
        if self.app.mouse_cap:
            self.keyboard_control()
            self.mouse_control()
        super().update()

    def keyboard_control(self):
        key_state = pg.key.get_pressed()
        v = PLAYER_SPEED * self.app.main_timer.ft

        if key_state[pg.K_e]:
            self.move_up(v)
        
        if key_state[pg.K_q]:
            self.move_down(v)
        
        if key_state[pg.K_a]:
            self.move_left(v)
        
        if key_state[pg.K_d]:
            self.move_right(v)

        if key_state[pg.K_s]:
            self.move_back(v)

        if key_state[pg.K_w]:
            self.move_forward(v)
    
    def mouse_control(self):
        dx, dy = pg.mouse.get_rel()

        if dx:
            self.rotate_yaw(delta = dx*MOUSE_SENSE)
        
        if dy:
            self.rotate_pitch(delta = dy*MOUSE_SENSE)