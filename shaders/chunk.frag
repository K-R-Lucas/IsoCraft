#version 460 core

layout (location = 0) out vec4 fragColour;

const vec3 gamma = vec3(2.2);
const vec3 inv_gamma = 1 / gamma;

layout (location = 0) uniform sampler2D u_texture_0;
layout (location = 1) uniform sampler2D u_texture_1;

in vec2 uv;
in float out_face_id;
in float out_block_id;

void main()
{
    vec4 tex_col = vec4(0, 0, 0, 0);

    if (out_block_id == 0) {
        tex_col = texture(u_texture_0, uv).rgba;
    }

    if (out_block_id == 1) {
        tex_col = texture(u_texture_1, uv).rgba;
    }

    vec4 tex_shade = vec4(vec3(1.0 - out_face_id/4.0), 1);
    tex_col *= tex_shade;
    
    fragColour = tex_col;
}