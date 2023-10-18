#version 460 core

layout (location = 0) out vec4 fragColour;

const vec3 gamma = vec3(2.2);
const vec3 inv_gamma = 1 / gamma;

uniform sampler2D u_texture_0;

in vec2 uv;
flat in int out_face_id;

float alpha = 1.0f;

void main() {
    vec4 tex_col = texture(u_texture_0, uv).rgba;
    vec4 tex_shade = vec4(vec3(1.0 - out_face_id/4.0), 1);

    tex_col *= tex_shade;
    
    fragColour = tex_col;
}