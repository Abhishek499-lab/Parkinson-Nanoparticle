import MDAnalysis as mda
from MDAnalysis.analysis import hydrogenbonds
import matplotlib.pyplot as plt
import numpy as np

print("Loading trajectory...")

u = mda.Universe("solvated.prmtop", "production.dcd")

print("Calculating Protein–DNA Hydrogen Bonds...")

hbonds = hydrogenbonds.HydrogenBondAnalysis(
    universe=u,
    donors_sel="protein",
    acceptors_sel="nucleic",
    update_selections=True
)

hbonds.run()

hb = hbonds.results.hbonds

frames = hb[:,0].astype(int)

unique_frames = np.unique(frames)
counts = [np.sum(frames == i) for i in unique_frames]

plt.figure(figsize=(7,5))
plt.plot(unique_frames, counts, linewidth=2)
plt.xlabel("Frame")
plt.ylabel("Number of Hydrogen Bonds")
plt.title("Protein–DNA Hydrogen Bonds")
plt.grid(True)
plt.tight_layout()
plt.savefig("Protein_DNA_HBonds.png", dpi=300)

print("Average H-bonds =", np.mean(counts))
print("Maximum H-bonds =", np.max(counts))
print("Protein–DNA Hydrogen Bond analysis completed.")
