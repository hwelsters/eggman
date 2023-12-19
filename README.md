Powered by ... the EGG ENGINE.
A small game engine(?) I made for making games about Eggs that platform.

# Setting up
Requirements:
CMake



# Linting:
`cpplint --recursive src include`

# Building:
1. Configure
`cmake -B out/build -G "Visual Studio 17 2022"`

2. Build
`cmake --build out/build --config Release`

Both in one script

Excuse the Copyright 2023 hwelsters at the top of each file. I'm just trying to please cpplint