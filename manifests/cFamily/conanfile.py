from conans import ConanFile, CMake


class HelloConan(ConanFile):
    name = "soos-conan-test"
    version = "1.2.3"
    description = """This is a Hello World library.
                    A fully featured, portable, C++ library to say Hello World in the stdout,
                    with incredible iostreams performance"""
    homepage = "http://eigen.tuxfamily.org"
    url = "https://github.com/conan-io/hello.git"
    license = "MIT"
    author = "John J. Smith (john.smith@company.com)"
    settings = "os", "compiler", "arch"
    options = {"shared": [True, False]}
    default_options = "shared=False"
    generators = "cmake"
    exports_sources = "src/*"

    def build(self):
        for bt in ("Debug", "Release"):
            cmake = CMake(self, build_type=bt)
            cmake.configure(source_folder="src")
            cmake.build()
            cmake.install()

    def requirements(self):
        self.requires("poco/[>1.0,<1.9]")
        self.requires('zlib/1.2.11')

    def build_requirements(self):
        self.tool_requires('7zip/19.00')
        self.tool_requires("cmake/3.22.6")
