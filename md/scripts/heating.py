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
    0*kelvin,
    1/picosecond,
    0.001*picoseconds
)

print("5. Creating simulation...")
simulation = Simulation(
    prmtop.topology,
    system,
    integrator,
    Platform.getPlatformByName("CPU")
)

print("6. Loading minimized state...")
with open("minimized.xml") as f:
    state = XmlSerializer.deserialize(f.read())

simulation.context.setState(state)

if inpcrd.boxVectors is not None:
    simulation.context.setPeriodicBoxVectors(*inpcrd.boxVectors)

state = simulation.context.getState(getEnergy=True)
print("Potential Energy =", state.getPotentialEnergy())

simulation.reporters.append(
    DCDReporter("heating.dcd",1000)
)

simulation.reporters.append(
    StateDataReporter(
        "heating.log",
        1000,
        step=True,
        temperature=True,
        potentialEnergy=True,
        kineticEnergy=True,
        totalEnergy=True,
        speed=True
    )
)

print("7. Heating...")

for T in [0,25,50,75,100,125,150,175,200,225,250,275,300]:
    print("Temperature =",T,"K")
    integrator.setTemperature(T*kelvin)
    simulation.step(250)

print("8. Saving state...")

state=simulation.context.getState(
    getPositions=True,
    getVelocities=True
)

with open("heated.xml","w") as f:
    f.write(XmlSerializer.serialize(state))

with open("heated.pdb","w") as f:
    PDBFile.writeFile(
        simulation.topology,
        state.getPositions(),
        f
    )

print("Heating completed successfully.")
