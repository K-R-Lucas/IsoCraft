#version 460 core

#define pi     3.1415926535897932384626433832795
#define pi_6   pi / 6.0
#define pi_56  5.0 * pi / 6.0
#define X      1.0/3.0
#define X2     2.0/3.0

layout (location = 0) in vec3 in_position;
layout (location = 1) in float block_id;
layout (location = 2) in float face_id;

uniform mat4 m_proj;
uniform mat4 m_view;
uniform mat4 m_model;

out vec2 uv;
out float out_face_id;
out float out_block_id;

const vec2 uv_coords[8] = vec2[8](
    vec2(0, 0), vec2(X, 0), vec2(X2, 0), vec2(1, 0),
    vec2(0, 1), vec2(X, 1), vec2(X2, 1), vec2(1, 1)
);

const int uv_indices[18] = int[18](
    0, 1, 5, 0, 5, 4, // top
    6, 5, 1, 6, 1, 2, // side
    6, 2, 3, 6, 3, 7 // front
);

void main() {
    int uv_index = int(gl_VertexID % 6 + face_id * 6);
    uv = uv_coords[uv_indices[uv_index]];
    out_face_id = face_id;
    out_block_id = block_id;

    gl_Position = m_proj * m_view * m_model * vec4(in_position, 1.0);
}