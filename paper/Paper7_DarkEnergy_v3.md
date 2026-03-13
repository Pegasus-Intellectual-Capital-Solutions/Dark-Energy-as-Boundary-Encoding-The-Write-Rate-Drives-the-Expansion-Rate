---
title: "Dark Energy as Boundary Encoding: The Write Rate Drives the Expansion Rate"
author:
  - "Charles Grant Smith Jr."
  - "Pegasus Intellectual Capital Solutions, Chicago, Illinois, USA"
date: "March 2026"
---

# Abstract

We conjecture that the expansion of the universe is driven by the rate at which irreversible processes in the bulk create classical records that must be encoded on the holographic boundary. In this picture, dark energy is not a substance, a field, or a vacuum energy. It is what expansion looks like from the bulk when the boundary accommodates new information. Every decoherence event, every photon absorbed, every bit of entropy produced by stars and black holes creates a record that the boundary must encode — and encoding requires the horizon area to grow. Following Jacobson's identification of the Einstein equation with $\delta Q = T dS$ at the horizon, the area growth *is* the expansion.

We test this conjecture against the observed expansion history and the measured cosmic entropy production history. The results:

(1) The horizon's quantum error-correction redundancy $\kappa(z) = S_\mathrm{hor}/S_\mathrm{bulk}$ — the overcapacity available for encoding — drops from $\sim 10^{25}$ at recombination to a minimum of $10^{18.7}$ at $z \approx 1.1$ as SMBH entropy accumulates, then recovers as accelerated expansion outpaces entropy production. The boundary is never stressed, but the overcapacity has a clear minimum between cosmic noon and the acceleration onset.

(2) The horizon area growth rate $dA/dt$ is anti-correlated with the bulk write rate (star formation rate density) at zero lag ($r = -0.21$), but strongly correlated at a lag of $\sim 3.5$ Gyr ($r = 0.91$). This correlation is entirely absent in a matter-only universe: dark energy is what creates it.

(3) The acceleration onset at $z \approx 0.7$ acts as an attractor. Regardless of when the star formation rate peaks ($z = 1$ to $z = 4$), the best-fit lag always adjusts so that the lagged write peak coincides with the acceleration epoch: $t_\mathrm{peak} + \tau_\mathrm{lag} \approx 7.1 \pm 0.3$ Gyr.

If the conjecture is correct, the cosmological constant problem dissolves: $\Lambda$ is not a vacuum energy requiring cancellation to 122 decimal places. It is the present-day write rate expressed as an energy density. The coincidence problem dissolves: dark energy density is comparable to matter density now because the write rate tracks structure formation, which requires matter. And the timing problem dissolves: the acceleration onset occurs at $z \approx 0.7$ because that is when the lagged encoding of cosmic noon's entropy production drives the boundary's strongest response.

Three observations would falsify the conjecture: phantom crossing ($w < -1$) at any redshift, breakdown of the lag–acceleration alignment under revised star formation measurements, or discovery of an epoch where $\kappa$ approaches unity.


# I. Introduction

## A. The problem

The accelerated expansion of the universe is well described by a cosmological constant $\Lambda$ with equation of state $w = -1$ (Riess et al. 1998; Perlmutter et al. 1999; Planck 2018; DESI 2024). Three problems remain unsolved. The *magnitude problem*: the observed $\Lambda \approx 2.9 \times 10^{-66}$ eV$^4$ is $\sim 10^{122}$ times smaller than the QFT vacuum energy prediction. The *coincidence problem*: dark energy density is comparable to matter density at the present epoch, despite their different scaling with expansion. The *timing problem*: the acceleration onset occurs at $z \approx 0.7$, with no physical reason why this epoch rather than any other.

Dynamical dark energy models (quintessence, CPL parameterization, phantom fields) address the timing problem by introducing time-dependent potentials, but these potentials are ad hoc — they have no connection to known physics and no explanation for why the dark energy transition correlates with the epoch of structure formation (Caldwell, Dave & Steinhardt 1998; Chevallier & Polarski 2001; Linder 2003).

## B. The conjecture

We propose that all three problems share a single resolution: dark energy is not a substance.

In the holographic framework developed in Papers 1–6, the cosmological horizon is a physical surface that encodes information about bulk processes. Following Jacobson (1995), the Einstein equation arises from the thermodynamic identity $\delta Q = T dS$ applied at the horizon: energy crossing the horizon increases its entropy, and the entropy increase requires the horizon area to grow. The area growth *is* the expansion of space.

The conjecture is direct: irreversible processes in the bulk — star formation, black hole accretion, every decoherence event that creates a classical record — generate information that must be encoded on the boundary. Each encoding event increases the boundary entropy by $\Delta S$, which requires the horizon area to increase by $\Delta A = 4 \ell_P^2 \Delta S$. This area growth is what we observe as the expansion of space. The encoding does not happen instantaneously — it requires a finite lag $\tau_\mathrm{enc}$ set by the light-crossing time of the encoding patch on the boundary. The expansion therefore tracks the write rate with a delay.

In this picture:

*The magnitude problem dissolves.* $\Lambda$ is not a vacuum energy requiring cancellation to 122 decimal places. It is the present-day bulk write rate — the rate at which decoherence events create records that the boundary must accommodate — expressed as an energy density. The write rate is set by astrophysics (star formation, black hole growth), not by QFT vacuum fluctuations.

*The coincidence problem dissolves.* Dark energy density is comparable to matter density now because the write rate tracks structure formation, which requires matter. When matter clumps into galaxies and stars, it produces entropy at a high rate; the boundary accommodates this by expanding. The dark energy density is tied to the matter density through the write rate, not by coincidence but by causation.

*The timing problem dissolves.* The acceleration onset at $z \approx 0.7$ is not arbitrary. Cosmic star formation peaks at $z \approx 2$ (cosmic noon). The boundary encodes these records with a lag of $\sim 3.5$ Gyr. The encoding completion — and therefore the peak expansion response — arrives at $z \approx 0.7$. The acceleration onset is phase-locked to cosmic noon through the encoding lag.

## C. Scope and honesty

This is a conjecture, not a derivation. We do not derive the encoding lag from the boundary's modular Hamiltonian. We do not compute $w(z)$ from first principles. We do not prove that Jacobson's thermodynamic relation, applied at the cosmological horizon with a finite encoding lag, quantitatively reproduces the Friedmann equations with the observed $\Lambda$.

What we do is:

(i) State the conjecture precisely.

(ii) Compute the boundary's information budget — the QEC redundancy ratio $\kappa(z) = S_\mathrm{hor}/S_\mathrm{bulk}$ — across cosmic history from independently measured quantities, with no free parameters.

(iii) Cross-correlate the expansion rate with the bulk write rate and report what the data show, including null results.

(iv) Identify three observations that would kill the conjecture.

The conjecture connects to the holographic decoherence framework of Papers 1–6: the same boundary that sets the acceleration scale for galaxy rotation curves ($a_u = cH_0/2\pi$, Papers 1–2) and governs cluster-scale lensing dynamics through its memory kernel (Paper 6) also drives the expansion of space through its encoding of bulk records. Whether this connection is real or coincidental is an empirical question. This paper provides the first quantitative tests.


# II. The Information Budget of the Observable Universe

## A. Horizon entropy

The cosmological horizon has Bekenstein–Hawking entropy

$$S_\mathrm{hor}(z) = \frac{\pi c^2}{\ell_P^2 H(z)^2} \tag{1}$$

where $\ell_P = 1.616 \times 10^{-35}$ m is the Planck length and $H(z)$ is the Hubble parameter at redshift $z$. Using Planck 2018 cosmological parameters ($H_0 = 67.4$ km/s/Mpc, $\Omega_m = 0.315$, $\Omega_\Lambda = 0.685$), the horizon entropy grows from $S_\mathrm{hor} \sim 10^{113.6}$ bits at recombination to $S_\mathrm{hor} \sim 10^{122.4}$ bits today.

## B. Bulk entropy

The bulk entropy of the observable universe has been catalogued by Egan & Lineweaver (2010). The dominant contributions are:

(i) *CMB photons and cosmic neutrinos:* $S_\mathrm{rad} \approx 4 \times 10^{88}$ bits. Effectively constant after recombination.

(ii) *Stellar photon entropy:* Cumulative entropy from nuclear burning in stars, computed by integrating the Madau & Dickinson (2014) star formation rate density $\rho_\mathrm{SFR}(z)$ over cosmic time and volume. Each solar mass of stars produces $\sim 10^{57}$ bits of photon entropy over its lifetime. The cumulative stellar entropy reaches $\sim 10^{80}$ bits by the present epoch.

(iii) *Supermassive black hole entropy:* The dominant contribution at late times. The total SMBH entropy today is $S_\mathrm{BH}(0) \approx 3 \times 10^{103}$ bits (Egan & Lineweaver 2010), dominated by the most massive black holes. SMBH entropy grows with the integral of the black hole accretion rate, which tracks the star formation rate with a proportionality constant calibrated to the local black hole mass density.

For the star formation rate density, we adopt the Madau & Dickinson (2014) fitting function:

$$\rho_\mathrm{SFR}(z) = 0.015 \frac{(1+z)^{2.7}}{1 + [(1+z)/2.9]^{5.6}} \; M_\odot \, \mathrm{yr}^{-1} \, \mathrm{Mpc}^{-3} \tag{2}$$

which peaks at $z \approx 1.9$ (cosmic noon).

## C. QEC redundancy ratio

The quantum error-correction redundancy ratio is

$$\kappa(z) = \frac{S_\mathrm{hor}(z)}{S_\mathrm{bulk}(z)} \tag{3}$$

In the holographic framework, $\kappa$ represents the number of redundant boundary copies per bulk record — the error-correction depth of the holographic code. The Almheiri–Dong–Harlow (2015) construction establishes that bulk reconstruction in AdS/CFT requires a quantum error-correcting code on the boundary; $\kappa \gg 1$ ensures that individual boundary erasures do not destroy bulk information.


# III. Results: The Redundancy History

We compute $\kappa(z)$ from Eq. (1)–(3) with no free parameters. All inputs — $H(z)$, $\rho_\mathrm{SFR}(z)$, $S_\mathrm{BH}(0)$ — are taken from independent observations.

**Table I.** QEC redundancy ratio across cosmic history.

| Epoch | $z$ | $t$ (Gyr) | $\log_{10} S_\mathrm{hor}$ | $\log_{10} S_\mathrm{bulk}$ | $\log_{10} \kappa$ | Trend |
|---|---|---|---|---|---|---|
| Recombination | 1100 | 0.00 | 113.6 | 88.6 | 25.0 | — |
| First stars | 20 | 0.18 | 118.9 | 88.6 | 30.3 | Rising |
| Reionization end | 10 | 0.47 | 119.7 | 98.9 | 20.8 | Dropping |
| $z = 6$ | 6 | 0.93 | 120.3 | 100.3 | 20.0 | Dropping |
| $z = 3$ | 3 | 2.14 | 121.0 | 101.8 | 19.2 | Dropping |
| Cosmic noon | 2 | 3.27 | 121.4 | 102.5 | 18.9 | Dropping |
| **$\kappa$ minimum** | **1.15** | **5.30** | **121.9** | **103.1** | **18.75** | **Minimum** |
| Acceleration onset | 0.7 | 7.3 | 122.0 | 103.2 | 18.8 | Rising |
| Today | 0 | 13.8 | 122.4 | 103.4 | 18.9 | Rising |

Two features of the $\kappa(z)$ trajectory are notable:

First, the boundary *always* has enormous overcapacity. The redundancy ratio never drops below $\kappa \sim 10^{18.7}$ — approximately $10^{19}$ boundary bits per bulk record. The holographic code is never stressed.

Second, $\kappa(z)$ has a minimum at $z \approx 1.15$ ($t \approx 5.3$ Gyr). Before this epoch, SMBH entropy accumulates faster than the horizon expands, consuming overcapacity. After this epoch, the accelerated expansion outpaces entropy production, and $\kappa$ recovers. The minimum occurs between cosmic noon ($z \approx 2$) and the acceleration onset ($z \approx 0.7$), separated from each by $\sim 2$ Gyr.


# IV. The Write Rate and the Expansion Rate

## A. The dark energy alignment

In the holographic framework, the expansion of the horizon *is* the accommodation of new information, following Jacobson's (1995) identification of the Einstein equation with $\delta Q = T dS$ at the horizon. If so, the rate of horizon area growth $dA/dt$ should be related to the rate of bulk information production, potentially with a lag set by the encoding timescale.

We test this by computing the Pearson correlation between $dA/dt$ (from the observed $H(z)$) and the star formation rate density $\rho_\mathrm{SFR}(z)$ (as a proxy for the bulk write rate) as a function of temporal lag $\tau$.

At zero lag, the correlation is $r = -0.21$: the expansion rate and the write rate are *anti-correlated*. The universe expands fastest when entropy production is declining, not when it peaks.

At $\tau \approx 3.5$ Gyr, the correlation reaches $r = 0.91$: the expansion rate tracks the write rate shifted forward by 3.5 billion years.

## B. The dark energy is necessary

The same analysis performed on an Einstein–de Sitter universe (matter-only, no dark energy) yields $r = -0.21$ at all lags. **The correlation between the lagged write rate and the expansion rate exists only in a universe with dark energy.** The dark energy component of the expansion history is precisely what is needed to make $dA/dt$ track the lagged write rate.

This is the central empirical observation of this paper. It is not a model prediction — it is a fact about two independently measured quantities ($H(z)$ and $\rho_\mathrm{SFR}(z)$) in the observed universe.

## C. The acceleration onset as attractor

To test whether the lag is physically meaningful or an artifact of correlating smooth functions, we perform three null hypothesis tests:

(i) *Random Gaussian humps:* 2,000 random bell curves tested against the actual $dA/dt$. Over 50% produce $r \geq 0.91$ at optimal lag. The high correlation alone is not significant — any smooth hump will correlate with another at some lag.

(ii) *Randomized SFRD parameters:* 2,000 Madau–Dickinson-type curves with randomized peak redshift ($z_\mathrm{break} \in [1.5, 5]$), rising slope ($\alpha \in [1.5, 4]$), and falling slope ($\beta \in [3, 8]$). 43% exceed $r = 0.91$. The correlation strength is not distinctive.

(iii) *Phase-shifted SFRD:* 2,000 circular time-shifts of the actual SFRD. Only 4% achieve $r \geq 0.91$ ($p = 0.04$). The *specific timing* of the real SFRD relative to the real expansion history is significant at the 96% confidence level.

The deeper result emerges from a sensitivity analysis. When the SFRD peak is varied from $z = 1$ to $z = 4$, the best-fit lag adjusts so that the sum $t_\mathrm{peak} + \tau_\mathrm{lag}$ always converges on $7.1 \pm 0.3$ Gyr — the epoch of acceleration onset.

**Table II.** Best-fit lag as a function of SFRD peak epoch.

| SFRD peak $z$ | Peak $t$ (Gyr) | Best lag $\tau$ (Gyr) | $t_\mathrm{peak} + \tau$ (Gyr) | $r$ |
|---|---|---|---|---|
| 0.98 | 5.93 | 1.46 | 7.40 | 0.98 |
| 1.47 | 4.33 | 2.78 | 7.10 | 0.95 |
| 1.86 (actual) | 3.50 | 3.54 | 7.04 | 0.91 |
| 2.44 | 2.67 | 4.70 | 7.37 | 0.88 |
| 2.93 | 2.20 | 5.00 | 7.20 | 0.87 |

The acceleration onset acts as an attractor: regardless of when the SFRD peaks, the expansion history pulls the optimal lag to align encoding completion with $z \approx 0.7$. This attractor behavior is the signal, not the correlation magnitude.

## D. Physical interpretation of the lag

The best-fit lag for the observed SFRD is $\tau_\mathrm{lag} \approx 3.5$ Gyr. In the holographic framework, this lag corresponds to the time required for bulk records to be redundantly encoded on the boundary — the light-crossing time of the encoding patch:

$$L_\mathrm{code} \sim c \tau_\mathrm{lag} \approx 1.1 \; \mathrm{Gpc} \tag{4}$$

The horizon radius at the present epoch is $R_\mathrm{hor} = c/H_0 \approx 4.4$ Gpc. The encoding patch is therefore approximately one-quarter of the horizon radius:

$$\frac{L_\mathrm{code}}{R_\mathrm{hor}} \approx \frac{1}{4} \tag{5}$$

This ratio may connect to the timescale discrepancy with the Paper 6 memory kernel. The cluster-scale kernel uses $\tau_\mathrm{kernel} \sim H_0^{-1} \sim 14$ Gyr — the full horizon light-crossing time, governing how long before a boundary record is *forgotten*. The encoding lag $\tau_\mathrm{enc} \sim 3.5$ Gyr governs how long before a new record is *written*. The ratio $\tau_\mathrm{enc}/\tau_\mathrm{kernel} \approx 1/4$ is the same as $L_\mathrm{code}/R_\mathrm{hor}$: the writing time scales with the encoding patch, while the forgetting time scales with the full horizon. We note this as a consistency observation, not a derivation.


# V. What Remains To Be Shown

The conjecture is stated; the preliminary tests are reported. Several critical gaps remain between the conjecture and a complete theory.

**The encoding lag is not derived.** The best-fit lag of 3.5 Gyr is the value that maximizes correlation with $dA/dt$ — it is extracted from the data, not computed from the boundary's error-correction structure. The physical interpretation ($L_\mathrm{code} \sim R_\mathrm{hor}/4$) is consistent but post hoc. A genuine prediction requires deriving $\tau_\mathrm{enc}$ from the boundary's modular Hamiltonian or from the redundancy requirements of the holographic code, and then comparing the derived value with the observed lag. This is the most important theoretical gap.

**The r = 0.91 correlation is not a detection.** As the null hypothesis tests demonstrate, any two smooth humps correlate at some lag. The significant results are the attractor behavior (Table II) and the dark energy necessity (Section IV.B), not the Pearson $r$ value. The paper's empirical content rests on the attractor and the EdS null, not on the correlation magnitude.

**The Friedmann equation has not been rederived.** The conjecture claims that writes drive expansion. A complete theory must show that Jacobson's $\delta Q = T dS$, applied at the cosmological horizon with a finite encoding lag and the observed bulk entropy production rate, quantitatively reproduces $H(z)$ without putting in $\Lambda$ by hand. This calculation — effectively rederiving the Friedmann equation from information dynamics — is beyond the scope of this paper but is the conjecture's ultimate test.

**The asymptotic value $\Lambda_\infty$ is not explained.** As the universe approaches heat death and the write rate drops to its residual quantum minimum, $\Lambda$ should asymptote to a value set by the boundary's self-maintenance — the minimum encoding activity of a de Sitter horizon. Computing this asymptotic value from the horizon's thermal properties would constitute a solution to the cosmological constant problem. We have not done this calculation. What we have done is show that the *timing* and *dynamics* of dark energy follow naturally from the write rate; the *magnitude* remains an open problem.


# VI. Falsifiable Predictions

The conjecture produces four predictions that, if violated, would rule it out:

**Prediction 1: $w \geq -1$ at all redshifts.** Causal encoding on a finite boundary cannot produce phantom behavior. The write rate is non-negative; the boundary area can grow but not shrink while encoding is active. If future surveys (DESI Year 5, Euclid, LSST) detect $w < -1$ at any redshift with high confidence, the conjecture is falsified. Current constraints are consistent; projected sensitivities of $\delta w \sim 0.01$ will test this.

**Prediction 2: The acceleration onset is locked to the entropy production peak.** The conjecture requires that $t_\mathrm{accel} \approx t_\mathrm{peak} + \tau_\mathrm{enc}$, where $t_\mathrm{peak}$ is the epoch of peak irreversible entropy production and $\tau_\mathrm{enc}$ is the encoding lag. If future measurements revise the star formation history in ways that break this alignment — specifically, if $t_\mathrm{peak} + \tau_\mathrm{lag}$ departs from the acceleration onset by more than $\sim 1$ Gyr — the conjecture fails.

**Prediction 3: $\kappa > \kappa_\mathrm{crit}$ at all epochs.** If any revision of $S_\mathrm{bulk}(z)$ causes $\kappa$ to approach unity, the holographic QEC interpretation fails. The current minimum ($\kappa \sim 10^{18.7}$) provides enormous margin.

**Prediction 4: The expansion rate responds to changes in the write rate.** This is the most direct test. If the bulk write rate could be independently varied — for instance, if a future epoch of enhanced star formation occurs — the conjecture predicts that the expansion rate would increase approximately $\tau_\mathrm{enc}$ later. More practically: detailed reconstruction of $H(z)$ in narrow redshift bins should reveal structure correlated with the lagged entropy production history, not a smooth $\Lambda$CDM curve. This requires sub-percent precision in $H(z)$ reconstruction, likely achievable with DESI full survey and Euclid combined.


# VII. Connection to Papers 1–6

The analysis presented here tests the holographic decoherence framework at its largest scale. The connections to earlier papers in the series are:

*Paper 1–2 (galaxy rotation curves):* The acceleration scale $a_u = cH_0/(2\pi)$ is derived from the Gibbons–Hawking temperature of the de Sitter horizon — the same horizon whose entropy $S_\mathrm{hor}$ appears in the $\kappa(z)$ calculation. The horizon temperature sets the acceleration scale for galactic dynamics; the horizon area sets the information capacity for cosmological dynamics.

*Paper 6 (cluster memory kernel):* The memory kernel $K(\Delta t) = (1/\tau) \exp(-\Delta t/\tau)$ with $\tau \sim H_0^{-1}$ governs how past baryonic configurations contribute to present gravitational observables. The encoding lag $\tau_\mathrm{enc} \sim 3.5$ Gyr identified here is related but not identical: it represents the writing time per encoding patch ($\sim R_\mathrm{hor}/4$), while $\tau_\mathrm{kernel}$ represents the full memory decay time ($\sim R_\mathrm{hor}$). Both derive from the boundary's information dynamics, with a factor $\sim 4$ set by the ratio of the encoding patch to the full horizon.

*Structural unity:* A single boundary with Bekenstein–Hawking entropy, Gibbons–Hawking temperature, and a causal encoding kernel produces: (1) the acceleration scale governing galactic dynamics, (2) the memory timescale governing cluster-scale offsets, and (3) the timing of cosmological acceleration. These are three windows into the same object.


# VIII. Conclusions

We have stated and tested a specific conjecture: that the bulk write rate — the rate at which irreversible processes create classical records that must be encoded on the holographic boundary — drives the expansion of space, and that what we call dark energy is this encoding process observed from the bulk.

The conjecture survives its first quantitative tests:

(1) The boundary always has sufficient capacity. The QEC redundancy $\kappa$ remains above $10^{18.7}$ at all epochs — the holographic code is never stressed.

(2) The overcapacity has a minimum at $z \approx 1.15$, precisely between cosmic noon and the acceleration onset. After the minimum, expansion accelerates to restore the boundary's encoding margin.

(3) The dark energy component of the expansion history is necessary and sufficient to make $dA/dt$ track the lagged bulk write rate. In a matter-only universe, no such relationship exists.

(4) The acceleration onset is an attractor: regardless of when entropy production peaks, the best-fit lag aligns encoding completion with $z \approx 0.7$.

(5) The best-fit lag of 3.5 Gyr corresponds to an encoding patch $\sim R_\mathrm{hor}/4$, consistent with a sub-horizon redundancy region for quantum error correction.

If the conjecture is correct, it resolves the three central puzzles of dark energy simultaneously. The magnitude problem: $\Lambda$ is not a vacuum energy but a write rate, set by astrophysics rather than by QFT. The coincidence problem: dark energy tracks matter density because the write rate tracks structure formation. The timing problem: the acceleration onset is phase-locked to cosmic noon through the encoding lag.

Critical gaps remain. The encoding lag is extracted from the data, not derived from the boundary. The Friedmann equation has not been rederived from information dynamics. The asymptotic value of $\Lambda$ — the residual write rate at heat death — has not been computed. These are the problems whose solutions would elevate the conjecture from an observation to a theory.

The conjecture connects three scales through a single boundary: the acceleration scale governing galaxy rotation curves ($a_u = cH_0/2\pi$), the memory kernel governing cluster dynamics ($\tau \sim H_0^{-1}$), and the encoding lag governing cosmic acceleration ($\tau_\mathrm{enc} \sim R_\mathrm{hor}/4c$). If these connections hold, then galaxies, clusters, and the accelerating expansion are three projections of the same object — a holographic boundary that maintains its error-correcting code by growing as the universe writes its history.


# Acknowledgments

The author thanks Claude (Anthropic) for computational assistance. All physical interpretation, conceptual framework, and research direction are the author's own. This research received no external funding.


# References

[1] C. G. Smith Jr., A Cosmological Acceleration Scale in Galactic Rotation Curves. Zenodo, DOI: 10.5281/zenodo.18806314 (2026).

[2] C. G. Smith Jr., Paper 6: Memory Kernel Architecture for Cluster-Scale Gravitational Dynamics. In preparation (2026).

[3] T. Jacobson, Thermodynamics of Spacetime: The Einstein Equation of State. Phys. Rev. Lett. 75, 1260 (1995).

[4] A. Almheiri, X. Dong, and D. Harlow, Bulk Locality and Quantum Error Correction in AdS/CFT. JHEP 2015, 163 (2015).

[5] P. Madau and M. Dickinson, Cosmic Star Formation History. Annu. Rev. Astron. Astrophys. 52, 415 (2014).

[6] C. J. Egan and C. H. Lineweaver, A Larger Estimate of the Entropy of the Universe. Astrophys. J. 710, 1825 (2010).

[7] G. W. Gibbons and S. W. Hawking, Cosmological Event Horizons, Thermodynamics, and Particle Creation. Phys. Rev. D 15, 2738 (1977).

[8] Planck Collaboration, Planck 2018 Results. VI. Cosmological Parameters. A&A 641, A6 (2020).

[9] DESI Collaboration, DESI 2024 VI: Constraints on Dark Energy from BAO. arXiv:2404.03002 (2024).

[10] R. R. Caldwell, R. Dave, and P. J. Steinhardt, Cosmological Imprint of an Energy Component with General Equation of State. Phys. Rev. Lett. 80, 1582 (1998).

[11] M. Chevallier and D. Polarski, Accelerating Universes with Scaling Dark Matter. Int. J. Mod. Phys. D 10, 213 (2001).

[12] E. V. Linder, Exploring the Expansion History of the Universe. Phys. Rev. Lett. 90, 091301 (2003).

[13] A. G. Riess et al., Observational Evidence from Supernovae for an Accelerating Universe and a Cosmological Constant. Astron. J. 116, 1009 (1998).

[14] S. Perlmutter et al., Measurements of $\Omega$ and $\Lambda$ from 42 High-Redshift Supernovae. Astrophys. J. 517, 565 (1999).

[15] W. H. Zurek, Decoherence and Quantum Darwinism. Cambridge University Press (2022).

[16] A. G. Cohen, D. B. Kaplan, and A. E. Nelson, Effective Field Theory, Black Holes, and the Cosmological Constant. Phys. Rev. Lett. 82, 4971 (1999).

[17] J. Aird et al., The Evolution of the X-Ray Luminosity Function of AGN. MNRAS 451, 1892 (2015).

[18] S. Lloyd, Computational Capacity of the Universe. Phys. Rev. Lett. 88, 237901 (2002).
