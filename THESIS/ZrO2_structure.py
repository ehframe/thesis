from ase import Atoms
from ase.spacegroup import crystal


class ZirconiaCrystal: # 4H SiC
    def __init__(self, lattice_constant=00, temperature=00, other_params = "vals"):
        #-------------------------------lattice parameters------------------------------
        self.a = 3.64381100 #Angstrom
        self.b = 3.64381100 #Angstrom
        self.c = 5.31456000 #Angstrom
        self.alpha = 90 #degrees
        self.beta = 90 #degrees
        self.gamma = 90 #degrees
        #-------------------------------------------------------------------------------------------
        #------------------------------Wyckoff-----------------------------------------------------
        self.wyckoff_positions = [
            ('Zr', (0, 0, 0), '2a'),
            ('O', (0, 1/2, 0.301775), '4d')
        ]
        #------------------------------------------------------------------------------------------
        #-------------------space group------------------------------------------------------------
        self.spacegroup = 137 #P6_3mc
        #------------------------------------------------------------------------------------------
        #------------------Other Parameters, Group when necessary----------------------------------
        #-------------------------------------------------------------------------------------------


    def initialize_structure(self):
        # Initialize positions of Si and C atoms in the unit cell
        """
        SAMPLE USE:
        
        crystal(('Co', 'Sb'),
                       basis=[(0.25, 0.25, 0.25), (0.0, 0.335, 0.158)],
                       spacegroup=204,
                       cellpar=[a, a, a, 90, 90, 90])
        """
        
        structure = crystal(
            symbols = [atom[0] for atom in self.wyckoff_positions],
            basis = [atom[1] for atom in self.wyckoff_positions],
            spacegroup = self.spacegroup,
            cellpar = [self.a, self.b, self.c, self.alpha, self.beta, self.gamma]
        )*(2, 4, 2)

        return structure