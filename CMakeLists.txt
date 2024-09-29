cmake_minimum_required(VERSION 3.10)
project(DSAL C)

set(CMAKE_C_STANDARD 99)
set(CMAKE_C_STANDARD_REQUIRED ON)

if (CMAKE_C_COMPILER_ID MATCHES "GNU|Clang")
    add_compile_options(-Wall -Wextra -pedantic)
elseif (MSVC)
    add_compile_options(/W4)
endif()

set(SRC_DIR "${CMAKE_SOURCE_DIR}/src")
set(INCLUDE_DIR "${CMAKE_SOURCE_DIR}/include")

file(GLOB SOURCES "${SRC_DIR}/*.cpp")
add_executable(${PROJECT_NAME} ${SOURCES}
        src/main.c)

target_include_directories(${PROJECT_NAME} PRIVATE ${INCLUDE_DIR})