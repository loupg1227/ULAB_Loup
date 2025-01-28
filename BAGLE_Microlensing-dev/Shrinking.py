class PSBL_PhotAstrom_EllOrbs_Param4(PSBL_PhotAstromParam4):
    """
    Point source binary lens.
    It has 3 more parameters than PSPL (additional mass term, separation,
    and angle of approach). Note that this is a non-STATIC binary lens, i.e.
    there is orbital motion.

    Attributes
    ----------
    t0_com : float
        Time of closest approach between the source and the CoM of the lenses, as seen from Earth (MJD.DDD)
    u0_amp_com : float
        Angular distance between the source and the binary lens COM
        on the plane of the sky at closest approach in units of thetaE. Can be
          * positive (u0_amp > 0 when u0_hat[0] > 0) or
          * negative (u0_amp < 0 when u0_hat[0] < 0).

    tE : float
        Einstein crossing time (days).
    thetaE : float
        The size of the Einstein radius in (mas).
    piS : float
        Amplitude of the parallax (1AU/dS) of the source. (mas)
    piE_E : float
        The microlensing parallax in the East direction in units of thetaE
    piE_N : float
        The microlensing parallax in the North direction in units of thetaE

    xS0_E : float
        R.A. of source position on sky at t = t0_com (arcsec) in an
        arbitrary ref. frame.
    xS0_N : float
        Dec. of source position on sky at t = t0_com (arcsec) in an
        arbitrary ref. frame.

    omega: float
        The argument of periastron of the primary lens's orbit in degrees.
        The secondary source will be directly 180 degrees across the primary
        source's argument of periastron.
    big_omega: float
        The longitude of the ascending node of the secondary lens's orbit
        in degrees. Since the primary and secondary sources share the same
        inclination angle for their orbital planes, they also share the same
        big_omega
    i: float
        Inclination angle of the system in degrees.
    e: float
        Eccentricity of the System
    tp: float
        This is the time of the periastron of the system in days.
    muS_E : float
        RA Source proper motion (mas/yr)
    muS_N : float
        Dec Source proper motion (mas/yr)
    sep: float
        Distance between lenses in mas
    arat: float
        Ratio of semi-major axis with current separation between lenses at time of measurement.

    q : float
        Mass ratio (M2 / M1)
    alpha : float
        Angle made between the binary axis and North;
        measured in degrees East of North.
    b_sff : numpy array or list
        The ratio of the source flux to the total (source + neighbors + lenses). One
        for each filter.
    mag_src : numpy array or list
        Source magnitude, unlensed. One in each filter.
    root_tol : float
        Tolerance in comparing the polynomial roots to the physical solutions. Default = 1e-8
    """
    fitter_param_names = ['t0', 'u0_amp', 'tE', 'thetaE', 'piS',
                          'piE_E', 'piE_N', 'xS0_E', 'xS0_N',
                          'omega', 'big_omega', 'i', 'e', 'tp', 'sep', 'arat',
                          'muS_E', 'muS_N',
                          'q', 'alpha']
    phot_param_names = ['b_sff', 'mag_src']
    additional_param_names = ['mL', 'piL', 'piRel',
                              'muL_E', 'muL_N',
                              'muRel_E', 'muRel_N']

    paramAstromFlag = True
    paramPhotFlag = True
    orbitFlag = 'Keplerian'

    def __init__(self, t0_com, u0_amp_com, tE, thetaE, piS,
                 piE_E, piE_N, xS0_E, xS0_N, omega, big_omega, i, e, tp, sep, arat, muS_E, muS_N,
                 q, alpha,
                 b_sff, mag_src,
                 raL=None, decL=None, obsLocation='earth', root_tol=1e-8):
        super().__init__(t0_com, u0_amp_com, tE, thetaE, piS,
                         piE_E, piE_N, xS0_E, xS0_N, muS_E, muS_N,
                         q, sep, alpha,
                         b_sff, mag_src,
                         raL=raL, decL=decL, obsLocation=obsLocation, root_tol=root_tol)

        # Orbital parameters
        self.beta_com = self.u0_amp_com * self.thetaE_amp
        self.u0_hat_com = u0_hat_from_thetaE_hat(self.thetaE_hat, self.beta_com)
        self.u0_com = np.abs(self.u0_amp_com) * self.u0_hat_com
        self.thetaS0_com = self.u0_com * self.thetaE_amp  # mas
        self.xL0_com = self.xS0 - (self.thetaS0_com * 1e-3) #arcseconds
        self.arat = arat

        self.omega = omega
        self.big_omega = big_omega
        self.i = i
        self.e = e
        self.tp = tp

         # Calculate period, and semi-major axes
        self.sep = sep #mas
        self.a = self.arat * self.sep #mas
        self.aleph_sec = (self.mLp/(self.mLp+self.mLs))*self.a #mas
        self.aleph = self.a - self.aleph_sec #mas
        self.al_AU = self.dL * (self.a *1e-3) * units.AU
        mL = self.mL * units.Msun
        p = (2 * np.pi * np.sqrt(self.al_AU ** 3 / (const.G * mL))).to('day')
        self.p = p.value  # Period in Days

        PSPL_Param().__init__()
        return
