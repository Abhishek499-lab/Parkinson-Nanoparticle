from openmm.app import *
from openmm import *
from openmm.unit import *

print("1. Loading topology...")
prmtop = AmberPrmtopFile("solvated.prmtop")

print("2. Loading coordinates...")
inpcrd = AmberInpcrdFile("solvated.inpcrd")

print("3. Creating system...")
system = prmtop.createSystem(
    nonbondedMethod=PME,
    nonbondedCutoff=1*nanometer,
    constraints=HBonds
)

print("4. Creating integrator...")
integrator = LangevinMiddleIntegrator(
    300*kelvin,
    1/picosecond,
    0.002*picoseconds
)

print("5. Creating simulation...")
simulation = Simulation(
    prmtop.topology,
    system,
    integrator
)

print("6. Setting positions...")
simulation.context.setPositions(inpcrd.positions)

if inpcrd.boxVectors is not None:
    simulation.context.setPeriodicBoxVectors(*inpcrd.boxVectors)

print("7. Starting minimization...")
print("Atoms:",
system.getNumParticles())
simulation.minimizeEnergy(maxIterations=10000)

print("8. Minimization finished!")

state = simulation.context.getState(getPositions=True)

with open("minimized_solvated.pdb", "w") as f:
    PDBFile.writeFile(
        simulation.topology,
        state.getPositions(),
        f
    )

print("9. PDB saved.")

from openmm import XmlSerializer

state = simulation.context.getState(
    getPositions=True,
    getVelocities=True
)

with open("minimized.xml", "w") as f:
    f.write(XmlSerializer.serialize(state))

print("10. XML state saved.")



