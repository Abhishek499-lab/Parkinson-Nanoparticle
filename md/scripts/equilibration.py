from openmm.app import *
from openmm import *
from openmm.unit import *
from openmm import XmlSerializer

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

# NPT ensemble
system.addForce(MonteCarloBarostat(1*bar, 300*kelvin, 25))

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
    integrator,
    Platform.getPlatformByName("CPU")
)

print("6. Loading heated state...")
with open("heated.xml") as f:
    simulation.context.setState(XmlSerializer.deserialize(f.read()))

if inpcrd.boxVectors is not None:
    simulation.context.setPeriodicBoxVectors(*inpcrd.boxVectors)

simulation.reporters.append(
    DCDReporter("equilibration.dcd", 1000)
)

simulation.reporters.append(
    StateDataReporter(
        "equilibration.log",
        1000,
        step=True,
        temperature=True,
        potentialEnergy=True,
        kineticEnergy=True,
        totalEnergy=True,
        density=True,
        volume=True,
        speed=True
    )
)

print("7. Running NPT equilibration...")

simulation.step(5000)

print("8. Saving state...")

state = simulation.context.getState(
    getPositions=True,
    getVelocities=True
)

with open("equilibrated.xml","w") as f:
    f.write(XmlSerializer.serialize(state))

with open("equilibrated.pdb","w") as f:
    PDBFile.writeFile(
        simulation.topology,
        state.getPositions(),
        f
    )

print("NPT Equilibration completed successfully.")
