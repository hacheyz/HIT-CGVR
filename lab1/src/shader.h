#ifndef LAB1_SHADER_H
#define LAB1_SHADER_H

class Shader
{
public:
	unsigned int ID;  // OpenGL ID

	Shader(const char *vertexPath, const char *fragmentPath);  // Constructor reads and builds the shader
	void use();  // Use/activate the shader
};

#endif //LAB1_SHADER_H
