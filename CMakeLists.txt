cmake_minimum_required(VERSION 3.15)

# Name our project
project(eggman)

# Use C++17
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

# ===========================================
# GAME ENGINE
# ===========================================
add_subdirectory(libs/egg)

# ===========================================
# GAME
# ===========================================
file(GLOB_RECURSE SOURCES src/*.cc)
add_executable(${PROJECT_NAME} ${SOURCES})

target_include_directories(${PROJECT_NAME} PUBLIC "${PROJECT_SOURCE_DIR}/src")

target_link_libraries(${PROJECT_NAME} PUBLIC egg)