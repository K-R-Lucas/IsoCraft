#version 430 core

layout (location = 0) out vec4 fragColour;

in vec3 block_colour;

void main() {
    fragColour = vec4(block_colour, 1);
}