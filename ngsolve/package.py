import os
import sys
from spack import *

class Ngsolve(CMakePackage):
    """NGSolve is a Finite Element library based on Netgen."""

    homepage = "https://ngsolve.org/"
    git = "https://github.com/NGSolve/ngsolve.git"

    maintainers = ['mhochsteger']

    version('6.2.2504', tag='v6.2.2504', submodules=True)

    depends_on('netgen')

    variant('native', default=True, description='Build/optimize for native CPU architecture')
    variant('python', default=True, description='Enable Python support')
    variant('mpi', default=True, description='Enable MPI support')

    extends('python', when='+python')

    depends_on('netgen+native', when='+native')
    depends_on('netgen~native', when='~native')
    depends_on('netgen+python', when='+python')
    depends_on('netgen~python', when='~python')
    depends_on('netgen+mpi', when='+mpi')
    depends_on('netgen~mpi', when='~mpi')

    def cmake_args(self):
        spec = self.spec
        print(spec['netgen'].to_dict())
        check_spec = lambda s: 'ON' if '+'+s in spec else 'OFF'

        cmake_args = [
            '-DUSE_SUPERBUILD=OFF',
            '-DNETGEN_DIR='+spec['netgen'].prefix,
            ]

        return cmake_args
