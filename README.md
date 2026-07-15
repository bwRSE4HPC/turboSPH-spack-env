# turboSPH-spack-env

This repository contains the spack environment configuration and custom spack packages for building the dependencies of turboSPH

A GCC 13.x compiler is required to build the dependencies.
For best results it is important to use a cluster-specific prebuild MPI package.
This can be added to spack as an external package.
On Horeka this can be done by adding to the `$HOME/.spack/packages.yaml` file:
```yaml
packages:
  openmpi:
    externals:
    - spec: openmpi@5.0.7~cuda~java~memchecker~rocm+static~wrapper-rpath+internal-pmix fabrics=ucx schedulers=slurm
      prefix: /software/all/mpi/openmpi/5.0-gnu-13
```

The spack environment can be activated with:
```sh
spack env activate PATH/TO/turboSPH-spack-env
```

To install the dependencies use after activating the environment:
```sh
spack install
```

The dependencies are now available after activating the environment, including the external MPI package if used.

