---
title:      The Relativistically Blurred Iron Kα Line as a Spin Diagnostic in X-ray Binaries
date:       2026-03-14
tag:        Stellar-mass BH
tag_class:  tag-bh
excerpt:    |
  The broad, skewed Fe Kα fluorescence feature carries a clean imprint of gravitational
  redshift and Lense–Thirring frame-dragging near the ISCO. Here I discuss what reflection
  spectroscopy is actually measuring, and where the systematic uncertainties live.
read_time:  8 min
---

The Fe K$\alpha$ emission line at rest energy 6.4 keV (neutral iron) to 6.97 keV (He-like Fe XXVI)
has become one of the most productive spectral diagnostics in X-ray binary astronomy. When the
hard X-ray corona illuminates the optically thick accretion disk, iron fluorescence returns photons
whose line profile encodes the kinematics and gravitational potential of the disk from which they
originate.

## The physical picture

In a flat spacetime, a narrow emission line from a rotating disk would appear double-peaked: one
horn from the approaching limb (blueshifted), one from the receding limb (redshifted). In the strong
gravity near a black hole, two additional effects distort this profile:

- **Gravitational redshift** deepens the red wing. Photons climbing out of the potential well
  lose energy as $\Delta E / E \approx r_g / r$.
- **Transverse Doppler effect** (time dilation) adds a further redshift even at 90° to the line
  of sight.
- **Relativistic beaming** brightens the approaching side, boosting the blue horn.
- **Light bending** brings photons from behind and below the disk into the line of sight,
  producing the extended red tail.

The net result is the classic skewed, broad profile first clearly detected by *ASCA* in MCG−6-30-15
by Tanaka et al. (1995) and subsequently in dozens of X-ray binary systems.

## Connecting to spin

The key quantity extracted from the line profile is the inner disk radius $r_{\rm in}$. Under the
standard thin-disk assumption (Novikov–Thorne), the disk terminates at the innermost stable circular
orbit (ISCO):

$$r_{\rm ISCO} = f(a_*) \, r_g, \qquad r_g \equiv GM/c^2$$

where $a_* \equiv Jc/GM^2 \in [-1, 1]$ is the dimensionless spin parameter and $f(a_*)$ ranges
from 9 (retrograde maximal spin) to 1 (prograde maximal spin). A smaller $r_{\rm in}$ means a
more compact ISCO, which means higher spin.

This is the basis of **reflection spectroscopy**: fit a relativistically blurred disk-reflection model
(e.g. `relxill`, `reflionx`) to the broadband X-ray spectrum and extract $r_{\rm in}$.

## What the model actually fits

A modern reflection fit simultaneously constrains:

| Parameter | Physical meaning |
|-----------|-----------------|
| $a_*$ | Black hole spin |
| $i$ | Disk inclination |
| $\Gamma$ | Coronal photon index |
| $\xi$ | Disk ionisation parameter $L/nR^2$ |
| $A_{\rm Fe}$ | Iron abundance relative to solar |
| $R_f$ | Reflection fraction |

The degeneracy between $i$ and $a_*$ is real and can be partially broken by the shape of
the Compton hump near 20–30 keV, which is why *NuSTAR*'s hard X-ray coverage above 10 keV
has been transformative.

## Systematic uncertainties

The dominant systematics are:

**1. Disk density.** The standard `reflionx` model assumes a fixed density of
$n_e = 10^{15}\,\rm cm^{-3}$. High-density reflection models (García et al. 2016, `relxillD`)
show that soft X-ray excess emission can be partly attributable to high-density disk reflection
rather than a warm Comptonisation component, shifting inferred parameters.

**2. Coronal geometry.** The lamppost assumption (point source on the spin axis) is convenient
but unrealistic. Extended corona models (e.g. Wilkins & Fabian 2012) change the emissivity
weighting across the disk, directly affecting $r_{\rm in}$.

**3. Returning radiation.** Photons emitted by the disk can be bent back onto it, reprocessing
some fraction of the disk flux. This is important for high spin ($a_* > 0.9$) and changes the
effective emissivity profile at small radii.

**4. Non-zero disk thickness.** The Novikov–Thorne ISCO assumes a razor-thin disk.
At $\dot{m} \gtrsim 0.1 \dot{m}_{\rm Edd}$, the disk scale height becomes significant and
material may continue to spiral in past the ISCO before accreting, shifting $r_{\rm in}$ inward
relative to the ISCO.

## Where things stand for canonical sources

For **Cygnus X-1**, spin constraints from reflection and from continuum-fitting both find
$a_* > 0.95$ (prograde, rapidly spinning). For **GX 339−4**, fits across multiple outbursts
consistently find $r_{\rm in} \lesssim 3\,r_g$, implying high spin, though the exact value is
sensitive to the choice of iron abundance. **4U 1630−47** shows one of the most compact line
profiles observed, with $r_{\rm in} \approx 1.5\,r_g$ in the soft state — consistent with
near-maximal Kerr.

## What XRISM will change

The *XRISM*/Resolve microcalorimeter (energy resolution $\sim 7$ eV at 6 keV, vs. $\sim 200$ eV
for CCD detectors) is beginning to spectrally resolve the line complex in bright X-ray binaries.
This will:

- Separate the narrow, distant reflection component from the broad relativistic wing
- Directly measure the blue-edge velocity of the disk wind absorption lines, constraining $r_{\rm launch}$
- Resolve multiple ionisation stages of the Fe K complex that are currently blended

The next few years of *XRISM* observations of bright Galactic X-ray binaries are likely to
significantly tighten spin constraints and clarify the systematic picture described above.

---

*References: Tanaka et al. 1995 (Nature 375, 659); Reynolds 2021 (ARA&A 59, 117);
García et al. 2016 (ApJ 820, 75); Draghis et al. 2023 (ApJ 946, 19).*
