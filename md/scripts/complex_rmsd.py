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

print("Calculating Protein-DNA Complex RMSD...")

R = rms.RMSD(
    u,
    u,
    select="protein or nucleic"
)

R.run()

time = R.results.rmsd[:,1]
rmsd = R.results.rmsd[:,2]

plt.figure(figsize=(7,5))
plt.plot(time, rmsd, linewidth=2)
plt.xlabel("Frame")
plt.ylabel("Complex RMSD (Å)")
plt.title("Protein-DNA Complex RMSD")
plt.grid(True)
plt.tight_layout()
plt.savefig("Complex_RMSD.png", dpi=300)

print("Protein-DNA Complex RMSD completed successfully.")

