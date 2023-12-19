import platform
import os

os.system("conan profile detect")

if platform.system() == "Windows":
    os.system("SET CONAN_USER_HOME=c:\\data")
    os.system("conan install .")

os.system("conan install . -c tools.system.package_manager:mode=install "
    "-c tools.system.package_manager:sudo=True --build=missing")

if platform.system() == "Windows":
    os.system("cmake --preset conan-default")
    os.system("cmake --build --preset conan-release")
else:
    os.system("cmake --preset conan-release")
    os.system("cmake --build --preset conan-release")

if platform.system() == "Windows":
    os.system("rd /s /q build")
else:
    os.system("rm -rf build")

os.system("conan install . -c tools.system.package_manager:mode=install "
    "-c tools.system.package_manager:sudo=True")

if platform.system() == "Windows":
    os.system("cmake . -G \"Visual Studio 17 2022\" -B build -DCMAKE_TOOLCHAIN_FILE=./build/generators/conan_toolchain.cmake -DCMAKE_POLICY_DEFAULT_CMP0091=NEW")
    os.system("cmake --build build --config Release")
else:
    os.system("cmake . -G \"Unix Makefiles\" -B build -DCMAKE_TOOLCHAIN_FILE=build/Release/generators/conan_toolchain.cmake -DCMAKE_POLICY_DEFAULT_CMP0091=NEW -DCMAKE_BUILD_TYPE=Release")
    os.system("cmake --build build --config Release")

# I don't like the way these files clog up the root directory, so I am removing them
os.remove('./conan.lock')
os.remove('./conanbuildinfo.txt')
os.remove('./conaninfo.txt')
os.remove('./graph_info.json')
os.remove('./CMakeUserPresets.json')