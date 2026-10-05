
import sys
import os
# Direct to 3.11 site-packages
sys.path.insert(0, '/usr/local/lib/python3.11/site-packages')

try:
    import openmm
    import openmm.app as app
    from rdkit import Chem
    from openff.toolkit.topology import Molecule
    import openmmforcefields
    
    print(f'Successfully accessed libraries in 3.11 process.')
    print(f'OpenMM: {openmm.__version__}')
    
    # Test sequence generation
    mol = Chem.MolFromSequence('TYVFF')
    print('Molecule preparation successful.')
    
except Exception as e:
    print(f'Bridge Error: {e}')
    sys.exit(1)
