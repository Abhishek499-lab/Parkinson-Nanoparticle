import MDAnalysis as mda
from MDAnalysis.analysis import align, rms
import matplotlib.pyplot as plt

print("Loading trajectory...")

u = mda.Universe("solvated.prmtop", "production.dcd")

# Backbone par alignment
align.AlignTraj(
    u,
    u,
    select="protein and backbone",
    in_memory=True
).run()

print("Calculating Backbone RMSD...")

R = rms.RMSD(
    u,
    u,
    select="protein and backbone"
)

R.run()

time = R.results.rmsd[:,1]
rmsd = R.results.rmsd[:,2]

plt.figure(figsize=(7,5))
plt.plot(time, rmsd, lw=2)
plt.xlabel("Frame")
plt.ylabel("Backbone RMSD (Å)")
plt.title("Protein Backbone RMSD")
plt.grid(True)
plt.tight_layout()
plt.savefig("Backbone_RMSD.png", dpi=300)

print("Done.")
