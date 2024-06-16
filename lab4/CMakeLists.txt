cmake_minimum_required(VERSION 3.10)
project(lab4)

set(CMAKE_CXX_STANDARD 11)

add_executable(lab4 src/main.cpp src/glad.c
        src/camera.h
        src/stb_image.h
        src/shader.h
        src/shader.cpp)

include_directories(include)
link_directories(lib)
target_link_libraries(lab4 ${PROJECT_SOURCE_DIR}/lib/libglfw3.a)