#version 460 core

layout (location = 0) out vec4 fragColour;

const vec3 gamma = vec3(2.2);
const vec3 inv_gamma = 1 / gamma;

uniform sampler2D u_texture_0;

in vec2 uv;

void main() {
    vec4 tex_col = texture(u_texture_0, uv).rgba;
    
    fragColour = tex_col;
}