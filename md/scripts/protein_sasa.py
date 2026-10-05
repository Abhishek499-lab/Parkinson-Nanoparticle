import MDAnalysis as mda
from MDAnalysis.analysis import align
from MDAnalysis.analysis import sas
import matplotlib.pyplot as plt
import numpy as np

print("Loading trajectory...")

u = mda.Universe("solvated.prmtop", "production.dcd")
	
# Protein backbone alignment
align.AlignTraj(
    u,
    u,
    select="protein and backbone",
    in_memory=True
).run()

protein = u.select_atoms("protein")

print("Calculating SASA...")

sr = sas.ShrakeRupley(
    protein,
    probe_radius=1.4,
    n_sphere_points=960
)

sasa = []

for ts in u.trajectory:
    sr.run(start=ts.frame, stop=ts.frame+1)
    sasa.append(np.sum(protein.atoms.tempfactors))

plt.figure(figsize=(7,5))
plt.plot(range(len(sasa)), sasa, linewidth=2)
plt.xlabel("Frame")
plt.ylabel("SASA ($\\AA^2$)")
plt.title("Protein SASA")
plt.grid(True)
plt.tight_layout()
plt.savefig("Protein_SASA.png", dpi=300)

print("Average SASA =", np.mean(sasa))
print("Protein SASA completed.")
