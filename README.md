# Hybrid-H1: Computational Design of a Modular Nanoparticle Platform for α-Synuclein Oligomer Targeting

## Overview

Hybrid-H1 is a computational proof-of-concept platform designed for targeted recognition of α-synuclein oligomers in Parkinson's disease.

The proposed system combines:

- PLGA nanoparticle core
- Trehalose as the proposed payload
- RVG29 as a brain-targeting / BBB-oriented ligand
- F5R2_v2 as the primary α-synuclein recognition element
- P3 (QQKTGVGN) as an auxiliary recognition peptide

The repository preserves selected computational structures, docking-related inputs, molecular-dynamics scripts, system files, and supporting project material recovered from the original working directories.

---

## Repository Structure

```text
Hybrid-H1-GitHub/
├── structures/
├── docking/
├── md/
│   ├── scripts/
│   └── system/
├── results/
├── docs/
├── MANIFEST.txt
├── README.md
├── LICENSE
├── CITATION.cff
└── .gitignore
```

---

## Hybrid-H1 Architecture

The proposed platform combines a PLGA nanoparticle core with trehalose, RVG29, the engineered F5R2_v2 aptamer, and the auxiliary peptide P3.

```text
PLGA nanoparticle
│
├── Trehalose
├── RVG29
│   └── BBB-oriented targeting
├── F5R2_v2
│   └── Primary α-synuclein recognition
└── P3: QQKTGVGN
    └── Auxiliary recognition
```

The platform is a computational proof-of-concept and does not establish experimental therapeutic efficacy.

---

## F5R2 Aptamer Engineering

F5R2 was evaluated using a single-nucleotide variant strategy.

Main variants:

- WT / F5R2
- V47_G>C
- V49_A>T

Reported RNAfold minimum free-energy values:

| Variant | MFE (kcal/mol) |
|---|---:|
| WT / F5R2 | -13.0 |
| V47_G>C | -14.1 |
| V49_A>T | -16.2 |

V47_G>C was selected as the engineered F5R2_v2 candidate.

Relevant structures:

```text
structures/F5R2.pdb
structures/WT.pdb
structures/V47_G.pdb
structures/V49_A.pdb
```

---

## α-Synuclein Structures

Reference structures preserved in the repository include:

```text
structures/1xq8.model.pdb
structures/6XYO.pdb
structures/WT_6XYO.pdb
structures/V47_6XYO.pdb
```

`1xq8.model.pdb` represents the α-synuclein monomer structure used in the project.

`6XYO.pdb` represents the α-synuclein fibril/oligomer-related reference structure.

`WT_6XYO.pdb` and `V47_6XYO.pdb` are recovered complex structures associated with the F5R2/α-synuclein analysis.

The recovered structures are preserved as project evidence. Their presence does not by itself establish that the complete original docking-generation workflow is reproducible from this repository.

---

## Docking Files

```text
docking/P3.pdbqt
docking/receptor_clean.pdbqt
docking/config.txt
```

The recovered P3 docking configuration contains the following parameters:

```text
center_x = 143.704
center_y = 140.721
center_z = 144.189
size_x = 30
size_y = 30
size_z = 30
exhaustiveness = 32
num_modes = 20
energy_range = 5
```

Original working-directory paths are retained in the configuration for provenance and are not expected to work unchanged on another computer.

---

## F5R2 Docking Results

Reported manuscript-level docking values:

| Variant | 1XQ8 | 6XYO |
|---|---:|---:|
| WT / F5R2 | 14564 | 15596 |
| V47_G>C | 12726 | 18014 |
| V49_A>T | 16790 | 16136 |

Reported selectivity indices:

| Variant | Selectivity index |
|---|---:|
| WT / F5R2 | 1.07 |
| V47_G>C | 1.42 |
| V49_A>T | 0.96 |

V47_G>C was selected as F5R2_v2.

The original executable PatchDock workflow and complete raw output chain used to generate these manuscript-level values were not fully recovered.

Therefore, these numerical values are preserved as documented manuscript/project results and are not presented as newly reproduced calculations.

---

## Interface and ACE Results

Reported manuscript-level values:

| Variant | Target | Interface area (Å²) | ACE |
|---|---|---:|---:|
| WT | 1XQ8 | 2388.4 | -425.39 |
| WT | 6XYO | 2077.2 | -76.70 |
| V47_G>C | 1XQ8 | 1800.1 | -96.28 |
| V47_G>C | 6XYO | 2846.8 | +191.45 |
| V49_A>T | 1XQ8 | 2766.1 | -883.17 |
| V49_A>T | 6XYO | 2252.6 | -255.53 |

The original executable interface-area/ACE calculation workflow and complete source output were not recovered.

These values are therefore retained as manuscript-derived results and are not computationally reconstructed here.

---

## α-Synuclein Hotspot Information

Reported prioritized residues:

- LYS23
- GLN24
- THR64
- ASN65
- VAL66
- GLY67
- GLY68

Reported relevance scores:

| Residue | Score |
|---|---:|
| LYS23 | 95 |
| GLN24 | 90 |
| THR64 | 92 |
| ASN65 | 90 |
| VAL66 | 94 |
| GLY67 | 98 |
| GLY68 | 90 |

The 23–24 and 64–68 regions were described as candidate recognition hotspot regions.

The original executable analysis and complete source output used to generate these rankings were not recovered.

These values are therefore preserved as manuscript-derived results rather than independently reconstructed calculations.

---

## P3 Auxiliary Peptide

The auxiliary recognition peptide is:

```text
QQKTGVGN
```

Preserved files:

```text
structures/P3_fixed.pdb
docking/P3.pdbqt
```

The available P3 structure-preparation files and docking configuration were identified during provenance review.

However, a valid final P3 docking output/pose/score corresponding to the manuscript-level result was not recovered.

No new P3 docking score or interaction result is reconstructed or claimed in this repository.

---

## Molecular Dynamics

Recovered MD scripts:

```text
md/scripts/
├── env_bridge.py
├── ligand_bridge.py
├── minimize.py
├── heating.py
├── equilibration.py
├── production.py
├── rmsd.py
├── backbone_rmsd.py
├── complex_rmsd.py
├── dna_rmsd.py
├── protein_rmsf.py
├── protein_sasa.py
├── radius_gyration.py
└── protein_dna_hbond.py
```

Recovered MD system files:

```text
md/system/complex.inpcrd
md/system/complex.prmtop
md/system/solvated.inpcrd
md/system/solvated.prmtop
```

These files preserve the available computational workflow and system preparation material.

The repository does not claim that every manuscript-level MD result can be independently reproduced from these files alone.

---

## Provenance Policy

This repository follows a conservative provenance approach.

Where original executable code, input files, or final computational outputs were available, the corresponding project material has been preserved.

Where original execution code or final output could not be recovered, the repository preserves available input structures, prepared structures, configuration files, executable scripts, MD system files, and documented manuscript results without reconstructing undocumented calculations.

Recovered files and manuscript-derived numerical results should not be interpreted as independently reproduced results unless an executable workflow and corresponding output are available.

---

## Important Limitations

Hybrid-H1 is a computational proof-of-concept.

The available work does not establish experimental validation of:

- α-synuclein binding
- cellular uptake
- BBB transport
- nanoparticle delivery efficiency
- therapeutic efficacy
- in vivo safety
- in vivo pharmacological activity

Experimental binding studies, cellular assays, nanoparticle characterization, BBB/transport studies, and in vivo evaluation remain necessary for future validation.

---

## Reproducibility

The repository provides selected computational inputs and executable MD scripts recovered from the original project.

Complete reproduction of every reported manuscript result is not currently possible because some original analysis scripts and raw computational outputs were not recovered.

The repository therefore distinguishes between recovered computational material and manuscript-derived results.

No undocumented calculation is presented as a reproduced result.

---

## Repository Manifest

`MANIFEST.txt` records the selected files assembled into this repository.

Temporary, audit, duplicate, and failed-calculation files were intentionally excluded from the repository core.

---

## Software

Computational tools used in the project include, where applicable:

- Python
- Google Colab
- AutoDock Vina
- PatchDock-related docking workflow
- RNA secondary-structure analysis
- Biopython
- OpenMM
- Amber-format topology/coordinate files
- Molecular-dynamics analysis scripts

Specific software versions should be verified from the original computational environment before attempting exact reproduction.

---

## Citation

If you use this repository or the Hybrid-H1 computational design, please cite the associated manuscript.

Repository citation metadata is provided in `CITATION.cff`.

The final GitHub repository URL should be added to `CITATION.cff` after the repository is created.

---

## License

Original code and repository organization are released under the MIT License.

Third-party structures, databases, software, and externally sourced materials remain subject to their respective licenses and terms of use.

See `LICENSE` for the repository license.
