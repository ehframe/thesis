
from ZrO2_structure import ZirconiaCrystal
from ase.visualize import view

structure = ZirconiaCrystal().initialize_structure()
print(len(structure.positions))
del structure[34]
#print(structure.positions)
view(structure)
print(len(structure.positions))