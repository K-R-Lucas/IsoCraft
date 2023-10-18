from settings import *

class Camera:
    def __init__(self, position, yaw, pitch):
        self.position = vec3(position)
        self.yaw = glm.radians(yaw)
        self.pitch = glm.radians(pitch)

        self.up = vec3(0, 1, 0)
        self.right = vec3(1, 0, 0)
        self.forward = vec3(0, 0, -1)

        # self.m_proj = glm.ortho(0, 100, 0, 100, NEAR, FAR)
        self.m_proj = glm.perspective(V_FOV, ASPECT_RATIO, NEAR, FAR)
        self.m_view = glm.mat4()
    
    def update(self):
        self.update_vectors()
        self.update_view()

    def update_view(self):
        self.m_view = glm.lookAt(self.position, self.position + self.forward, self.up)
    
    def update_vectors(self):
        self.forward.x = glm.cos(self.yaw) * glm.cos(self.pitch)
        self.forward.y = glm.sin(self.pitch)
        self.forward.z = glm.sin(self.yaw) * glm.cos(self.pitch)

        self.forward = glm.normalize(self.forward)
        self.right = glm.normalize(glm.cross(self.forward, vec3(0, 1, 0)))
        self.up = glm.normalize(glm.cross(self.right, self.forward))

    def move_left(self, velocity):
        self.position -= self.right * velocity
    
    def move_right(self, velocity):
        self.position += self.right * velocity

    def move_down(self, velocity):
        self.position -= self.up * velocity
    
    def move_up(self, velocity):
        self.position += self.up * velocity
    
    def move_back(self, velocity):
        self.position -= self.forward * velocity
    
    def move_forward(self, velocity):
        self.position += self.forward * velocity
    
    def rotate_yaw(self, delta):
        self.yaw += delta

    def rotate_pitch(self, delta):
        self.pitch -= delta
        self.pitch = glm.clamp(self.pitch, -PITCH_LIMIT, PITCH_LIMIT)