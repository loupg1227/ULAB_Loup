# first line: 23
@cache_memory.cache()
def parallax_in_direction(RA, Dec, mjd, obsLocation='earth'):
    """
    | R.A. in degrees. (J2000)
    | Dec. in degrees. (J2000)
    | MJD

    Equations following MulensModel.
    """
    #print('parallax_in_direction: len(t) = ', len(mjd))

    # Munge inputs into astropy format.
    times = Time(mjd + 2400000.5, format='jd', scale='tdb')
    coord = SkyCoord(RA, Dec, unit=(units.deg, units.deg))

    direction = coord.cartesian.xyz.value
    north = np.array([0., 0., 1.])
    _east_projected = np.cross(north, direction) / np.linalg.norm(np.cross(north, direction))
    _north_projected = np.cross(direction, _east_projected) / np.linalg.norm(np.cross(direction, _east_projected))

    obs_pos = get_observer_barycentric(obsLocation, times)
    sun_pos = get_body_barycentric(body='sun', time=times)

    sun_obs_pos = sun_pos - obs_pos

    pos = sun_obs_pos.xyz.T.to(units.au)

    e = np.dot(pos, _east_projected)
    n = np.dot(pos, _north_projected)

    pvec = np.array([e.value, n.value]).T

    return pvec
