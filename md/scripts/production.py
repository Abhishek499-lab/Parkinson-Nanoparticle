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

print("6. Loading equilibrated state...")
with open("equilibrated.xml") as f:
    simulation.context.setState(
        XmlSerializer.deserialize(f.read())
    )

simulation.reporters.append(
    DCDReporter("production.dcd", 1000)
)

simulation.reporters.append(
    StateDataReporter(
        "production.log",
        1000,
        step=True,
        time=True,
        potentialEnergy=True,
        kineticEnergy=True,
        totalEnergy=True,
        temperature=True,
        speed=True,
        progress=True,
        remainingTime=True,
        totalSteps=500000,
        separator=","
    )
)

print("7. Running 1 ns Production MD...")
simulation.step(500000)

print("8. Saving final structure...")

state = simulation.context.getState(
    getPositions=True,
    getVelocities=True
)

with open("final_1ns.pdb", "w") as f:
    PDBFile.writeFile(
        simulation.topology,
        state.getPositions(),
        f
    )

with open("production.xml", "w") as f:
    f.write(XmlSerializer.serialize(state))

print("Production MD completed successfully.")
