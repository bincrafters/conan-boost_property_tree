from conans import ConanFile, tools, os

class BoostProperty_TreeConan(ConanFile):
    name = "Boost.Property_Tree"
    version = "1.64.0"
    generators = "txt"
    url = "https://github.com/boostorg/property_tree"
    description = "For a description of this library, please visit http://boost.org/property_tree "
    license = "www.boost.org/users/license.html"
    lib_short_name = "property_tree"

    def source(self):
        self.run("git clone --depth=50 --branch=boost-{0} {1}.git"
                 .format(self.version, self.url))

    def package(self):
        include_dir = src=os.path.join(os.getcwd(), self.lib_short_name, "include")
        self.copy(pattern="*", dst="", src=include_dir)
