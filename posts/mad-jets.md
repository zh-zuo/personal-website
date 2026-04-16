---
title:      Magnetically Arrested Disks and the Origin of Relativistic Jets
date:       2026-01-22
tag:        Jets
tag_class:  tag-jet
excerpt:    |
  GRMHD simulations point toward the magnetically arrested disk state as the configuration that
  most efficiently extracts black hole spin energy via the Blandford–Znajek mechanism. I look at
  the observational signatures of MAD states in nearby low-luminosity AGN.
read_time:  7 min
---

One of the outstanding puzzles of black hole astrophysics is the origin of relativistic jets:
collimated outflows that extend from sub-parsec to megaparsec scales, carry enormous kinetic
power, and are launched within a few gravitational radii of the black hole. The jet power in
the most powerful radio galaxies and quasars can rival or exceed the bolometric luminosity of
the accretion disk — in some cases by an order of magnitude.

## The Blandford–Znajek mechanism

The leading theoretical mechanism for jet power extraction is **Blandford & Znajek (1977)**
(BZ). In the BZ mechanism, large-scale poloidal magnetic field threads the spinning black hole
ergosphere. The frame-dragging of spacetime twists field lines, launching a Poynting-flux jet
with power:

$$P_{\rm BZ} \approx \frac{\kappa}{4\pi c} \Phi_{\rm BH}^2 \Omega_H^2 f(\Omega_H)$$

where $\Phi_{\rm BH}$ is the magnetic flux threading the horizon, $\Omega_H = a_* c / (2 r_H)$
is the angular velocity of the horizon, and $f(\Omega_H)$ is a correction factor of order unity.
The key point is that $P_{\rm BZ} \propto \Phi_{\rm BH}^2 a_*^2$: jet power depends on
*both* the accumulated magnetic flux on the black hole *and* the spin.

For a given spin, the jet is most powerful when $\Phi_{\rm BH}$ is maximised.

## The magnetically arrested disk

GRMHD simulations (Narayan et al. 2012; Tchekhovskoy et al. 2011) find that magnetic flux
accumulates on the black hole until the magnetic pressure near the horizon is comparable to
the ram pressure of infalling gas:

$$\phi \equiv \frac{\Phi_{\rm BH}}{\sqrt{\dot{M} r_g^2 c}} \approx 50$$

(in Gaussian units appropriate to the simulation convention). Once $\phi$ saturates at this
**magnetically arrested disk** (MAD) value, further flux accumulation is prevented — the disk
is literally arrested by the magnetic field.

In the MAD state:

- **Jet efficiency** $\eta_j = P_j / \dot{M} c^2$ can exceed 100% for near-maximal spin,
  meaning more energy is extracted from the spinning black hole than is delivered by accretion.
- The disk is intermittently disrupted by **magnetic flux eruptions** — episodes where
  concentrated flux tubes break away from the horizon and are advected outward, temporarily
  reducing $\phi$ before it builds up again.
- The accretion rate is reduced relative to the SANE (Standard and Normal Evolution) state
  because the magnetic pressure partially supports against infall.

## Observational signatures of the MAD state

Identifying MAD conditions observationally is challenging because we cannot directly image
the horizon-scale magnetic field. Indirect signatures include:

**1. High jet efficiency.** In low-luminosity AGN where the jet kinetic power can be estimated
from X-ray cavity calorimetry (e.g. Perseus A, Cygnus A), the implied $\eta_j$ sometimes
approaches or exceeds the maximum radiative efficiency $\eta_{\rm rad} \approx 0.42$ for
prograde maximal Kerr. This is only possible via BZ with a MAD-level flux.

**2. Jet power variability.** MAD flux eruptions produce transient reductions in jet power
on timescales $\sim 10^2\text{–}10^3\,t_g$ (where $t_g = r_g / c$). In M87, VLBI monitoring
shows limb-brightening and knot ejection events that may trace such episodic activity.

**3. Rotation measure and circular polarisation.** The Faraday rotation measure (RM) probes
the line-of-sight magnetic field and electron density in the inner accretion flow. In Sgr A*,
the *ALMA*-measured RM $\approx -5 \times 10^5\,\rm rad\,m^{-2}$ constrains the product
$n_e B_\parallel r$ near the Bondi radius. EHT polarimetric imaging constrains the field
topology at $\lesssim 10\,r_g$.

**4. Jet collimation profile.** In M87, *HST* and VLBI imaging resolve the jet morphology
from $\sim 10^3\,r_g$ (parabolic self-collimation) to $\sim 10^6\,r_g$ (conical, ballistic).
The collimation break radius correlates with the Bondi radius, consistent with the jet being
shaped by interaction with the ambient RIAF.

## The radio–X-ray correlation

In hard-state X-ray binaries and low-luminosity AGN, a tight correlation exists between radio
luminosity (proxy for jet power) and X-ray luminosity (proxy for accretion rate):

$$L_R \propto L_X^{0.6\text{–}0.7}$$

This **fundamental plane of black hole activity** (Merloni et al. 2003) extends over 8 decades
in mass and 12 decades in luminosity. In the context of MAD/SANE models, systems that lie
*above* the fundamental plane (radio-loud outliers) may be preferentially in the MAD state
at high spin, while radio-quiet systems at the same $L_X$ may be in the SANE state with lower
accumulated flux.

## What comes next

The distinguishing prediction of MAD models is the quasi-periodic magnetic flux eruptions.
Detecting these requires:

- Time-resolved EHT or space-VLBI monitoring at $\lesssim 10\,r_g$ resolution
- Correlated multi-wavelength flares (mm + NIR + X-ray) with the characteristic MAD timescale
  $\sim 10^3\,t_g$

For M87, $t_g \approx 9$ hours, so MAD eruptions would appear as day-to-week variability in
the VLBI structure — within reach of the current EHT programme. For Sgr A*, $t_g \approx 20$ s,
so eruptions would appear on minute-to-hour timescales, possibly connected to the observed
NIR and X-ray flares.

---

*References: Blandford & Znajek 1977 (MNRAS 179, 433); Narayan et al. 2012 (MNRAS 426, 3241);
Tchekhovskoy et al. 2011 (MNRAS 418, L79); Merloni et al. 2003 (MNRAS 345, 1057);
Event Horizon Telescope Collaboration 2019 (ApJL 875, L5).*
