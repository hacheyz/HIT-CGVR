#include <iostream>

#include "glad/glad.h"
#include "GLFW/glfw3.h"
#include "camera.h"
#include "shader.h"

#define STB_IMAGE_IMPLEMENTATION

#include "stb_image.h"

void framebuffer_size_callback(GLFWwindow *window, int width, int height);
void processInput(GLFWwindow *window);
void mouse_callback(GLFWwindow *window, double xposIn, double yposIn);
void scroll_callback(GLFWwindow *window, double xoffset, double yoffset);
unsigned int loadTexture(const char *path);

// window size
const unsigned int SCR_WIDTH = 2560;
const unsigned int SCR_HEIGHT = 1600;

Camera camera(glm::vec3(0.0f, 0.5f, 3.0f));
float lastX = (float)SCR_WIDTH/2.0;
float lastY = (float)SCR_HEIGHT/2.0;
bool firstMouse = true;
float deltaTime = 0.0f;  // 两帧的时间差
float lastFrame = 0.0f;  // 上一帧的时间

int main()
{
	// glfw: initialize and configure
	glfwInit();
	// set OpenGL version as 3.3
	glfwWindowHint(GLFW_CONTEXT_VERSION_MAJOR, 3);
	glfwWindowHint(GLFW_CONTEXT_VERSION_MINOR, 3);
	// set OpenGL profile as core (use a subset of OpenGL features)
	glfwWindowHint(GLFW_OPENGL_PROFILE, GLFW_OPENGL_CORE_PROFILE);

#ifdef __APPLE__
	glfwWindowHint(GLFW_OPENGL_FORWARD_COMPAT, GL_TRUE);
#endif

	// glfw window creation
	GLFWwindow *window = glfwCreateWindow(SCR_WIDTH, SCR_HEIGHT, "Diamond", NULL, NULL);
	if (window == NULL) {
		std::cout << "Failed to create GLFW window" << std::endl;
		glfwTerminate();
		return -1;
	}
	glfwMakeContextCurrent(window);
	glfwSetFramebufferSizeCallback(window, framebuffer_size_callback);
	glfwSetCursorPosCallback(window, mouse_callback);
	glfwSetScrollCallback(window, scroll_callback);
	glfwSetInputMode(window, GLFW_CURSOR, GLFW_CURSOR_DISABLED); // todo

	// glad: load all OpenGL function pointers
	if (!gladLoadGLLoader((GLADloadproc)glfwGetProcAddress)) {
		std::cout << "Failed to initialize GLAD" << std::endl;
		return -1;
	}

	// set up vertex data (and buffer(s)) and configure vertex attributes
	float diamondVertices[] = {
			// vertex pos // texture pos
			0.5f, 0.0f, 0.0f, 0.0f, 0.0f,
			0.0f, 0.5f, 0.0f, 1.0f, 0.0f,
			0.0f, 0.0f, 0.5f, 1.0f, 1.0f,
			-0.5f, 0.0f, 0.0f, 0.0f, 0.0f,
			0.0f, -0.5f, 0.0f, 1.0f, 0.0f,
			0.0f, 0.0f, -0.5f, 1.0f, 1.0f,
	};

	unsigned int diamondIndices[] = {
			1, 0, 2,
			3, 1, 2,
			4, 3, 2,
			0, 4, 2,
			4, 0, 5,
			0, 1, 5,
			1, 3, 5,
			3, 4, 5,
	};

	glEnable(GL_DEPTH_TEST);

	// create Shader
	Shader shader_diamond("res/expr2.vs", "res/expr2.fs");
	unsigned int texture = loadTexture("res/diamond.jpg");
	shader_diamond.use();
	shader_diamond.setInt("texture1", 0);

	unsigned int VBO, VAO, EBO;
	glGenVertexArrays(1, &VAO);
	glGenBuffers(1, &VBO);
	glGenBuffers(1, &EBO);
	glBindVertexArray(VAO);
	glBindBuffer(GL_ARRAY_BUFFER, VBO);
	glBufferData(GL_ARRAY_BUFFER, sizeof(diamondVertices), diamondVertices, GL_STATIC_DRAW);
	glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, EBO);
	glBufferData(GL_ELEMENT_ARRAY_BUFFER, sizeof(diamondIndices), diamondIndices, GL_STATIC_DRAW);

	// position attribute
	glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 5*sizeof(float), (void *)0);
	glEnableVertexAttribArray(0);

	// texture coord attribute
	glVertexAttribPointer(1, 2, GL_FLOAT, GL_FALSE, 5*sizeof(float), (void *)(3*sizeof(float)));
	glEnableVertexAttribArray(1);

	// render loop
	while (!glfwWindowShouldClose(window)) {
		float currentFrame = static_cast<float>(glfwGetTime());
		deltaTime = currentFrame - lastFrame;
		lastFrame = currentFrame;
		processInput(window);

		// render (clear the color buffer)
		glClearColor(0.1f, 0.1f, 0.15f, 1.0f);  // set background color
		glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);

		// render diamond
		shader_diamond.use();
		shader_diamond.setMat4("model", glm::mat4(1.0f));
		shader_diamond.setMat4("view", camera.GetViewMatrix());
		shader_diamond.setMat4("projection",
				glm::perspective(glm::radians(camera.Zoom), (float)SCR_WIDTH/(float)SCR_HEIGHT, 0.1f, 100.0f));
		glActiveTexture(GL_TEXTURE0);
		glBindTexture(GL_TEXTURE_2D, texture);
		glBindVertexArray(VAO);
		glDrawElements(GL_TRIANGLES, 24, GL_UNSIGNED_INT, 0);

		// glfw: swap buffers and poll IO events (keys pressed/released, mouse moved etc.)
		glfwSwapBuffers(window);
		glfwPollEvents();
	}

	// optional: de-allocate all resources once they've outlived their purpose:
	glDeleteVertexArrays(1, &VAO);
	glDeleteBuffers(1, &VBO);

	// glfw: terminate, clearing all previously allocated GLFW resources.
	glfwTerminate();
	return 0;
}

// process all input: query GLFW whether relevant keys are pressed/released this frame and react accordingly
void processInput(GLFWwindow *window)
{
	if (glfwGetKey(window, GLFW_KEY_ESCAPE) == GLFW_PRESS)
		glfwSetWindowShouldClose(window, true);
	if (glfwGetKey(window, GLFW_KEY_W) == GLFW_PRESS)
		camera.ProcessKeyboard(FORWARD, deltaTime);
	if (glfwGetKey(window, GLFW_KEY_S) == GLFW_PRESS)
		camera.ProcessKeyboard(BACKWARD, deltaTime);
	if (glfwGetKey(window, GLFW_KEY_A) == GLFW_PRESS)
		camera.ProcessKeyboard(LEFT, deltaTime);
	if (glfwGetKey(window, GLFW_KEY_D) == GLFW_PRESS)
		camera.ProcessKeyboard(RIGHT, deltaTime);
}

// glfw: whenever the window size changed (by OS or user resize) this callback function executes
void framebuffer_size_callback(GLFWwindow *window, int width, int height)
{
	// make sure the viewport matches the new window dimensions; note that width and
	// height will be significantly larger than specified on retina displays.
	glViewport(0, 0, width, height);
}

void mouse_callback(GLFWwindow *window, double xposIn, double yposIn)
{
	float xpos = static_cast<float>(xposIn);
	float ypos = static_cast<float>(yposIn);
	if (firstMouse) {
		lastX = xpos;
		lastY = ypos;
		firstMouse = false;
	}
	float xoffset = xpos - lastX;
	float yoffset = lastY - ypos; // reversed since y-coordinates go from bottom to top
	lastX = xpos;
	lastY = ypos;
	camera.ProcessMouseMovement(xoffset, yoffset);
}

void scroll_callback(GLFWwindow *window, double xoffset, double yoffset)
{
	camera.ProcessMouseScroll(static_cast<float>(yoffset));
}

unsigned int loadTexture(const char *path)
{
	unsigned int textureID;
	glGenTextures(1, &textureID);

	int width, height, nrComponents;
	unsigned char *data = stbi_load(path, &width, &height, &nrComponents, 0);
	if (data) {
		GLenum format;
		if (nrComponents == 1)
			format = GL_RED;
		else if (nrComponents == 3)
			format = GL_RGB;
		else if (nrComponents == 4)
			format = GL_RGBA;

		glBindTexture(GL_TEXTURE_2D, textureID);  // so that we can just operate on GL_TEXTURE_2D
		glTexImage2D(GL_TEXTURE_2D, 0, format, width, height, 0, format, GL_UNSIGNED_BYTE, data);
		glGenerateMipmap(GL_TEXTURE_2D);

		// set the texture wrapping/filtering options (on the currently bound texture object)
		glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT);
		glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT);
		if (format == GL_RGBA) {
			glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP_TO_EDGE);
			glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP_TO_EDGE);
		}
		glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR_MIPMAP_LINEAR);
		glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR);

		stbi_image_free(data);
	} else {
		std::cout << "Texture failed to load at path: " << path << std::endl;
		stbi_image_free(data);
	}

	return textureID;
}
