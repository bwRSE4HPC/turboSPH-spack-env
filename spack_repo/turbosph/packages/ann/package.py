# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.makefile import MakefilePackage

from spack.package import *


class Ann(MakefilePackage):
    """ANN: A Library for Approximate Nearest Neighbor Searching."""

    homepage = "https://www.cs.umd.edu/~mount/ANN/"
    url = "https://www.cs.umd.edu/~mount/ANN/Files/1.1.2/ann_1.1.2.tar.gz"

    maintainers("MarcelKoch")

    license("LGPL-2.1", checked_by="MarcelKoch")

    version("1.1.2", sha256="eea03f2e224b66813226d775053316675375dcec45bd263674c052d9324a49a5")

    depends_on("cxx", type="build")

    def edit(self, spec, prefix):
        # replace default Make-config with custom config that respects the spack compiler
        with open("Make-config", "w") as config:
            lines = [
                "linux-g++:",  # there needs to be a non-default target
                "\t$(MAKE) targets \\",
                "\t\"ANNLIB = libANN.a\" \\",
                f"\t\"C++ = {spack_cxx}\" \\",
                "\t\"CFLAGS = -O3\" \\",
                "\t\"MAKELIB = ar ruv\" \\",
                "\t\"RANLIB = true\" \\"
                ]
            config.write("\n".join(lines))

    @property
    def build_targets(self):
        return ["linux-g++"]

    def install(self, spec, prefix):
        install_tree("lib", prefix.lib)
        install_tree("include", prefix.include)
