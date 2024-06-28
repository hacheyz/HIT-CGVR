#ifndef LAB1_SHADER_H
#define LAB1_SHADER_H

#include <glm/glm.hpp>
#include <string>

class Shader
{
public:
	unsigned int ID;  // OpenGL ID

	Shader(const char *vertexPath, const char *fragmentPath);  // Constructor reads and builds the shader
	void use();  // Use/activate the shader

	// Utility uniform functions
	void setBool(const std::string& name, bool value) const;
	void setInt(const std::string& name, int value) const;
	void setFloat(const std::string& name, float value) const;
	void setMat4(const std::string& name, glm::mat4 value) const;
	void setVec3(const std::string& name, glm::vec3 value) const;
	void setVec3(const std::string& name, float x, float y, float z) const;
	void setVec2(const std::string& name, float x, float y) const;
};

#endif //LAB1_SHADER_H
