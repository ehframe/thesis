from pymatgen.core import Structure
from ase.visualize import view
from pymatgen.io.cif import CifWriter
from gpaw import GPAW, PW
from ase.optimize import BFGS
from ase.io import write

# Load the CIF file
structure = Structure.from_file('ZrO2_mp-2574_computed.cif')

# Create a 2x2x2 supercell
supercell = structure * [2, 2, 2]

# Convert the supercell to an ASE Atoms object
ase_atoms = supercell.to(fmt='ase')

# View the 3D diagram using ASE
view(ase_atoms)

# Set up GPAW calculator for relaxation
calc = GPAW(
    mode=PW(400),  # Plane wave cutoff energy
    xc='PBE',  # Exchange-correlation functional
    kpts=(3, 3, 3),  # k-points grid for sampling the Brillouin zone
    maxiter=150,  # Maximum number of SCF iterations
    convergence={'energy': 1e-5, 'density': 1e-5},  # Convergence criteria
    txt='relaxation_output.txt'  # Output file for GPAW log
)

# Assign the calculator to the ASE atoms object
ase_atoms.set_calculator(calc)

# Perform structure relaxation using BFGS algorithm
relax = BFGS(ase_atoms)
relax.run(fmax=0.05)  # Force tolerance of 0.05 eV/Å

# Save the relaxed structure in different formats
write('relaxed_supercell.xyz', ase_atoms)  # Save in XYZ format
write('relaxed_supercell.cif', ase_atoms)  # Save as CIF

# Add labels to the supercell and save it as CIF
for i, site in enumerate(supercell):
    site.label = f"{site.specie}{i}"

# Write the relaxed supercell as a CIF file using Pymatgen
CifWriter(supercell).write_file('relaxed_supercell.cif')


