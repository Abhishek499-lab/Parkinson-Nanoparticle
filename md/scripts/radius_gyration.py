import MDAnalysis as mda
from MDAnalysis.analysis import align	
import matplotlib.pyplot as plt
import numpy as np

print("Loading trajectory...")

u = mda.Universe("solvated.prmtop", "production.dcd")

# Protein backbone par alignment
align.AlignTraj(
    u,
    u,
    select="protein and backbone",
    in_memory=True
).run()

protein = u.select_atoms("protein")

rg = []

print("Calculating Radius of Gyration...")

for ts in u.trajectory:
    rg.append(protein.radius_of_gyration())

plt.figure(figsize=(7,5))
plt.plot(np.arange(len(rg)), rg, linewidth=2)
plt.xlabel("Frame")
plt.ylabel("Radius of Gyration (Å)")
plt.title("Protein Radius of Gyration")
plt.grid(True)
plt.tight_layout()
plt.savefig("Radius_of_Gyration.png", dpi=300)

print("Radius of Gyration completed successfully.")
