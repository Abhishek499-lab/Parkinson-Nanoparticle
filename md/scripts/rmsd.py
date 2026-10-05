import mdtraj as md
import matplotlib.pyplot as plt

print("Loading trajectory...")

traj = md.load(
    "production.dcd",
    top="solvated.prmtop"
)

print("Calculating RMSD...")

rmsd = md.rmsd(traj, traj, 0)

plt.figure(figsize=(8,5))
plt.plot(rmsd*10)
plt.xlabel("Frame")
plt.ylabel("RMSD (Å)")
plt.title("Protein-DNA Complex RMSD")
plt.grid(True)
plt.savefig("RMSD.png", dpi=300)

print("Done.")
