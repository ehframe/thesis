from pymatgen.core import Structure
from ase.visualize import view
from pymatgen.io.cif import CifWriter

# Load the CIF file into a pymatgen structure object
structure = Structure.from_file('ZrO2_mp-2574_computed.cif')

# Create a 2x2x2 supercell from the base structure
supercell = structure * [2, 2, 2]

# Convert the supercell to an ASE Atoms object for visualization
ase_atoms = supercell.to(fmt='ase')  # Convert the pymatgen structure to ASE format

# Remove the atom at index 34 to create a vacancy (likely an oxygen atom)
del ase_atoms[34]

# Visualize the modified structure with the vacancy
view(ase_atoms)

# Remove the atom from the pymatgen supercell as well to reflect the vacancy
del supercell[34]

# Add labels to the sites in pymatgen for exporting a CIF file
for i, site in enumerate(supercell):
    site.label = f"{site.specie}{i}"

# Write the modified supercell (with the vacancy) to a CIF file
CifWriter(supercell).write_file('ZrO2_mp-2574_supercell_with_vacancy.cif')
