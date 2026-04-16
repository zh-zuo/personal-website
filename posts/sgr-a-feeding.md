---
title:      Feeding the Monster: Gas Dynamics at the Galactic Centre
date:       2026-02-07
tag:        SMBH
tag_class:  tag-smbh
excerpt:    |
  Sgr A* sits inside a dense stellar cluster with a ready supply of hot gas from stellar winds —
  yet it accretes at roughly $10^{-9}$ of its Eddington rate. Why the Galactic Centre black hole
  is so underluminous is one of the central puzzles of low-luminosity AGN physics.
read_time:  6 min
---

Our Galactic Centre hosts a supermassive black hole of mass $M \approx 4 \times 10^6\,M_\odot$,
known as Sgr A* from its compact radio source coincident with the dynamical centre traced by
stellar orbits. Despite sitting inside a dense young stellar cluster — the S-stars — whose
strong winds provide a plentiful supply of hot gas, Sgr A* is strikingly underluminous:
its bolometric luminosity is $L \sim 10^{36}$ erg s$^{-1}$, roughly nine orders of magnitude
below the Eddington limit $L_{\rm Edd} \approx 5 \times 10^{44}$ erg s$^{-1}$.

## The Bondi accretion problem

Naive application of the Bondi (1952) formula for spherically symmetric accretion gives an
accretion rate at the Bondi radius $r_B \approx GM/c_s^2$:

$$\dot{M}_B \approx \pi \lambda r_B^2 \rho_\infty c_s$$

where $c_s$ is the sound speed of the ambient medium and $\lambda$ is a factor of order unity.
*Chandra* observations resolve the diffuse X-ray emission from the Bondi sphere (Baganoff et al.
2003), yielding $\dot{M}_B \sim 10^{-5}\,M_\odot\,\rm yr^{-1}$. At the observed luminosity and
an assumed radiative efficiency of $\eta \sim 0.1$, the implied accretion rate onto the black
hole is $\dot{M}_{\rm BH} \sim 10^{-11}\,M_\odot\,\rm yr^{-1}$ — four orders of magnitude
smaller than the Bondi value.

Something between the Bondi radius ($\sim 10^5\,r_g$) and the event horizon removes or
expels most of the inflowing gas.

## Radiatively inefficient accretion

The standard solution invokes a **radiatively inefficient accretion flow** (RIAF). In the
RIAF paradigm (Ichimaru 1977; Narayan & Yi 1994), the accretion rate is low enough that
Coulomb coupling between ions and electrons is inefficient: ions are heated by compression
but cannot transfer energy rapidly to electrons, which radiate. The result is a geometrically
thick, hot, two-temperature plasma:

- **Ions:** $T_i \sim 10^{11}$ K (virial temperature)
- **Electrons:** $T_e \sim 10^{9\text{–}10}$ K (set by Coulomb coupling and synchrotron losses)

At each radius, a large fraction of the binding energy is stored in the ions rather than
radiated. This naturally produces low luminosities. Furthermore, RIAFs are subject to strong
winds — the convective and magnetocentrifugal instabilities drive outflows that carry away
a large fraction of the inflowing mass, so $\dot{M}(r) \propto r^s$ with $s \approx 0.3$–0.5
(Yuan & Narayan 2014 review).

## What GRAVITY+ sees

The GRAVITY interferometer at the VLTI has transformed our empirical picture of the inner
accretion flow. The key results:

**Astrometric S2 orbit.** The most precise measurement of $M_{\rm BH}$ and the distance to
the Galactic Centre $R_0 = 8.277 \pm 0.009$ kpc (GRAVITY Collaboration 2022).

**NIR flare astrometry.** Hot spots orbiting within $\sim 10\,r_g$ during bright infrared
flares trace clockwise motion consistent with orbital periods of $\sim 45$ min — implying
radii of $\sim 6\text{–}10\,r_g$ and providing the first geometric constraint on the ISCO
region of Sgr A* (Gravity Collaboration 2018).

**Closure phases.** At 2.2 µm, the source appears marginally resolved during flares at
the level of $\sim 50\,\mu$as, constraining the size of the emitting region.

## The millimetre picture from the EHT

The first 230 GHz Event Horizon Telescope image of Sgr A* (EHT Collaboration 2022) shows
a ring of emission with angular diameter $\sim 51\,\mu$as, consistent with the expected shadow
diameter $\theta_{\rm sh} \approx 10\,r_g / D \approx 50\,\mu$as for $D = R_0$. The ring
is asymmetric, with a brightness excess in the south consistent with relativistic beaming of
clockwise-orbiting plasma. The source variability is rapid (timescale $\sim r_g/c \approx 20$ s),
which complicates imaging compared to M87*.

The EHT data are broadly consistent with GRMHD models in the MAD and SANE (Standard and Normal
Evolution) states, though distinguishing between them requires:

1. Multi-frequency polarisation closure quantities
2. Longer baseline space-VLBI
3. Better time-resolved imaging during flares

## Open questions

- What fraction of the Bondi-sphere gas actually reaches $r \lesssim 100\,r_g$?
- What drives the NIR/X-ray flares — magnetic reconnection events, orbital hot spots, or jet instabilities?
- Is Sgr A* in the SANE or MAD state? The answer constrains how efficiently the jet extracts spin energy.
- Has the Galactic Centre been more active in the recent past? The Fermi Bubbles and the
  X-ray reflection nebulae in the Central Molecular Zone suggest activity $\sim 10^6$ years ago
  at a level $\sim 10^{4\text{–}6}$ times the current luminosity.

---

*References: Baganoff et al. 2003 (ApJ 591, 891); Narayan & Yi 1994 (ApJ 428, L13);
Yuan & Narayan 2014 (ARA&A 52, 529); GRAVITY Collaboration 2018 (A&A 618, L10);
EHT Collaboration 2022 (ApJL 930, L12).*
