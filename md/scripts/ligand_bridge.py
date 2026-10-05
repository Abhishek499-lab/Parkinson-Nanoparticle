
import sys
sys.path.insert(0, '/usr/local/lib/python3.11/site-packages')
from rdkit import Chem
from rdkit.Chem import AllChem
from openff.toolkit.topology import Molecule

sequence = 'YVFF'
rdmol = Chem.MolFromSequence(sequence)
if rdmol:
    rdmol = Chem.AddHs(rdmol)
    AllChem.EmbedMolecule(rdmol, AllChem.ETKDG())
    AllChem.UFFOptimizeMolecule(rdmol)
    offmol = Molecule.from_rdkit(rdmol, allow_undefined_stereo=True)
    print(f'Ligand atoms: {offmol.n_atoms}')
else:
    print('Failed to generate molecule.')
