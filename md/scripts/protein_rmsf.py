import MDAnalysis as mda	
from MDAnalysis.analysis import align, rms
import matplotlib.pyplot as plt

print("Loading trajectory...")

u = mda.Universe("solvated.prmtop", "production.dcd")

# Protein backbone par alignment
align.AlignTraj(
    u,
    u,
    select="protein and backbone",
    in_memory=True
).run()

print("Calculating RMSF...")

protein = u.select_atoms("protein and name CA")

R = rms.RMSF(protein).run()

plt.figure(figsize=(8,5))
plt.plot(protein.resids, R.results.rmsf, linewidth=2)
plt.xlabel("Residue Number")
plt.ylabel("RMSF (Å)")
plt.title("Protein Cα RMSF")
plt.grid(True)
plt.tight_layout()
plt.savefig("Protein_RMSF.png", dpi=300)

print("Protein RMSF completed successfully.")
