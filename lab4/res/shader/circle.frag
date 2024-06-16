#version 330 core
out vec4 FragColor;

in vec2 TexCoords;

uniform float w_div_h;

float step(float distance)
{
    if (distance < 0.99) return 0; // [0.99,1] is the border
    else if (distance <= 1) return 1;
    else return 0;
}

void main()
{
    vec2 uv = TexCoords * 2.0 - 1.0;
    uv.x *= w_div_h;
    float distance = sqrt(dot(uv, uv));
    vec3 color = vec3(step(distance));
    FragColor = vec4(color, 1.0);
}