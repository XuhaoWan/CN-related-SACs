#!/usr/bin/env python
# -*- coding:utf-8 -*-
#author: xhwan

import ase.io
from ase.visualize import view
from dscribe.descriptors import SOAP
from ase.build import molecule
from ase import atom

species = ["C",  "N", 'Fe', ]
rcut = 6.0
nmax = 1
lmax = 0

# Setting up the SOAP descriptor
soap = SOAP(
    species=species,
    periodic=False,
    rcut=rcut,
    nmax=nmax,
    lmax=lmax,
)


# Molecule created as an ASE.Atoms

#C2N = ase.io.read(filename='C2N', format='vasp')
#C3N = ase.io.read(filename='C3N', format='vasp')
#C3N3 = ase.io.read(filename='C3N3', format='vasp')
#C3N4 = ase.io.read(filename='C3N4', format='vasp')
#C3N5 = ase.io.read(filename='C3N5', format='vasp')
#C4N3 = ase.io.read(filename='C4N3', format='vasp')
Pc = ase.io.read(filename='Pch', format='vasp')
NC = ase.io.read(filename='NC', format='vasp')


# Create SOAP output for the system
#soap_C2N = soap.create(C2N, positions=[-1])
#soap_C3N = soap.create(C3N, positions=[-1])
#soap_C3N3 = soap.create(C3N3, positions=[-1])
#soap_C3N4 = soap.create(C3N4, positions=[-1])
#soap_C3N5 = soap.create(C3N5, positions=[-1])
#soap_C4N3 = soap.create(C4N3, positions=[256])
soap_Pc = soap.create(Pc, positions=[-1])
soap_NC = soap.create(NC, positions=[66])

# print(soap_C2N)
# print(soap_C2N.shape)
# print(soap_C3N)
# print(soap_C3N.shape)
# print(soap_C3N3)
# print(soap_C3N3.shape)
# print(soap_C3N4)
# print(soap_C3N4.shape)
# print(soap_C3N5)
# print(soap_C3N5.shape)
# print(soap_C4N3)
# print(soap_C4N3.shape)
print(soap_Pc)
print(soap_Pc.shape)
print(soap_NC)
print(soap_NC.shape)

# print(C2N[-1])
# print(C3N[-1])
# print(C3N3[-1])
# print(C3N4[-1])
# print(C3N5[-1])
# print(C4N3[256])
print(Pc[-1])
print(NC[66])








