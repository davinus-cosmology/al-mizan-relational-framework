# The Al-Mizan Al-Mutakamil Relational Framework

**Author:** Davinus Masire Ochanda  
**Affiliation:** Faculty of Science and Technology, University of Nairobi  
**Email:** davinusmasire4@gmail.com  
**ORCID:** [0009-0003-1769-8951](https://orcid.org/0009-0003-1769-8951)

---

## 📌 Overview
This repository contains the computational implementation, kinematic calibration scripts, and theoretical derivations for the **Al-Mizan Al-Mutakamil Relational Framework**. The framework replaces continuous particle dark matter halos and a fine-tuned cosmological constant with a discrete relational scale-step operator acting on baryonic angular-momentum flux tensors.

---

## 🧮 Core Theoretical Formulations

### The Mizan Master Equation
$$\Xi_k = M \cdot \left[ \Xi_{k-1} \otimes \mathcal{R}\left( \frac{K_{\text{Global}}}{k} \right) \right]$$

### Operational Acceleration Modification
$$g_{\text{mizan}}(r) = g_{\text{bar}}(r) \cdot \left[ 1 + A_0 \left( \frac{M_{\text{bar}}}{M_*} \right)^\gamma \left( \frac{r}{k \cdot R_c} \right)^{K_{\text{Global}}} \right]$$

---

## 📊 Key Results & Parameters

- **Global SPARC Calibration:** Calibrated against 175 galaxies (~3,400 radial points) from the SPARC database using strictly 3 global scalar constants:
  - $A_0 = 5.234951$ ($\log_{10} A_0 = 0.7189$)
  - $\gamma = -0.138325$ (Sub-linear mass-scaling exponent)
  - $K_{\text{Global}} = 0.978294$ (Scale-step ratio exponent)
- **Kinematic Fit Quality:** Median galaxy-by-galaxy RMS residual of **0.1157 dex** and global mean residual bias of **-0.0079 dex**.
- **Cosmological Transition:** Rectified dual-trace acceleration transition redshift $z_{\text{acc}} \approx 2.15$.
- **Structure Growth:** Suppressed peak $f\sigma_8(z) \approx 0.2954$ evaluated against DESI BAO/RSD observations.

---

## 📂 Repository Layout

```text
├── data/              # SPARC galaxy rotation curve datasets
├── pipelines/         # Kinematic loss evaluation & cosmology pipelines
├── paper/             # Manuscript LaTeX files & figures
├── LICENSE            # License terms
└── README.md          # Project documentation


## 📄 Citation

If you utilize this theoretical framework, codebase, or data pipeline in your research, please cite:

```bibtex
@article{ochanda2026almizan,
  title={The Al-Mizan Al-Mutakamil Relational Framework: Discrete Scale Operators, Galactic Kinematics, and Cosmological Expansion},
  author={Ochanda, Davinus Masire},
  institution={University of Nairobi, Faculty of Science and Technology},
  year={2026}
}

