cmake_minimum_required(VERSION 3.10)
project(lab1)

set(CMAKE_CXX_STANDARD 11)

add_executable(lab1 src/main.cpp src/glad.c
        src/shader.cpp
        src/shader.h)

include_directories(include)
link_directories(lib)
target_link_libraries(lab1 ${PROJECT_SOURCE_DIR}/lib/libglfw3.a)