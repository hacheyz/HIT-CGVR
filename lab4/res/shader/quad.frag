#version 330 core
out vec4 FragColor;

in vec2 TexCoords;

uniform sample2D screenTexture;

void main()
{
    FragColor = texture(screenTexture, TexCoords);
}